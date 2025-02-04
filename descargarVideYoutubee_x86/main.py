import tkinter as tk
from tkinter import ttk, messagebox
import threading
import queue
import os
import yt_dlp

class ProgressDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Descargando Video")
        self.geometry("300x100")
        self.progress_bar = ttk.Progressbar(self, orient="horizontal", length=280, mode="determinate")
        self.progress_bar.pack(pady=20)
        self.progress_bar["value"] = 0

    def update_progress(self, value):
        if self.winfo_exists():
            self.progress_bar["value"] = value
            self.update_idletasks()  # Forzar actualización de la UI

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Descargar Video de YouTube")
        self.geometry("400x200")
        self.progress_dialog = None
        self.queue = queue.Queue()

        # Widgets
        self.label = tk.Label(self, text="Ingresa el enlace de YouTube:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self, width=50)
        self.entry.pack(pady=10)

        self.download_button = tk.Button(self, text="Descargar", command=self.iniciar_descarga)
        self.download_button.pack(pady=10)

        self.close_button = tk.Button(self, text="Cerrar", command=self.destroy)
        self.close_button.pack(pady=10)

        # Verificar actualizaciones más frecuentes
        self.after(50, self.verificar_cola)

    def iniciar_descarga(self):
        link = self.entry.get()
        if not link:
            messagebox.showwarning("Advertencia", "Por favor, ingresa un enlace de YouTube.")
            return

        self.progress_dialog = ProgressDialog(self)
        self.progress_dialog.grab_set()

        self.download_thread = threading.Thread(target=self.descargar_video, args=(link,))
        self.download_thread.start()

    def descargar_video(self, link):
        def progress_hook(d):
            if d["status"] == "downloading":
                # Calcular porcentaje manualmente
                total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
                if total_bytes and d.get('downloaded_bytes'):
                    percent = (d['downloaded_bytes'] / total_bytes) * 100
                    self.queue.put(("progress", percent))
            
            elif d["status"] == "finished":
                self.queue.put(("progress", 100))

        try:
            opciones = {
                "format": "bestvideo+bestaudio/best",
                "outtmpl": "%(title)s.%(ext)s",
                "merge_output_format": "mp4",
                "ffmpeg_location": ffmpeg_path,
                "progress_hooks": [progress_hook],
                "noprogress": True,
                "verbose": False,  # Reducir logs
                "socket_timeout": 30,
            }

            with yt_dlp.YoutubeDL(opciones) as ydl:
                ydl.download([link])

        except Exception as e:
            self.queue.put(("error", str(e)))
        finally:
            self.queue.put(("finish", None))

    def verificar_cola(self):
        try:
            while True:
                tipo, valor = self.queue.get_nowait()
                if tipo == "progress":
                    self.progress_dialog.update_progress(valor)
                elif tipo == "error":
                    messagebox.showerror("Error", f"Ocurrió un error: {valor}")
                    if self.progress_dialog.winfo_exists():
                        self.progress_dialog.destroy()
                elif tipo == "finish":
                    if self.progress_dialog and self.progress_dialog.winfo_exists():
                        self.progress_dialog.destroy()
        except queue.Empty:
            pass
        self.after(50, self.verificar_cola)  # Verificar cada 50ms

if __name__ == "__main__":
    ffmpeg_path = os.path.join(os.path.dirname(__file__), 'ffmpeg','ffmpeg.exe')
    
    app = App()
    app.mainloop()