import os
import yt_dlp
import flet as ft

class YouTubeDownloader(ft.UserControl):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.base_dir = ""
        self.video_dir = ""
        self.audio_dir = ""
        self.video_formats = []
        self.selected_format = None

    def build(self):
        # Initialize storage folders
        self.init_storage()

        self.url_input = ft.TextField(label="Enter YouTube Video URL", hint_text="Paste URL here", width=300)
        self.fetch_btn = ft.ElevatedButton(text="Fetch Available Qualities", on_click=self.fetch_formats)
        self.quality_spinner = ft.Dropdown(label="Select Quality", width=300)
        self.download_btn = ft.ElevatedButton(text="Download Video", on_click=self.download_video, disabled=True)
        self.status_label = ft.Text()

        return ft.Column(
            [
                self.url_input,
                self.fetch_btn,
                self.quality_spinner,
                self.download_btn,
                self.status_label,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def init_storage(self):
        # Initialize base directory and subfolders
        self.base_dir = os.path.join(ft.storage_path(), "Damtube")
        self.video_dir = os.path.join(self.base_dir, "Video")
        self.audio_dir = os.path.join(self.base_dir, "Audio")

        os.makedirs(self.video_dir, exist_ok=True)
        os.makedirs(self.audio_dir, exist_ok=True)

    def fetch_formats(self, e):
        url = self.url_input.value.strip()
        if not url:
            self.status_label.value = "Error: URL cannot be empty!"
            self.update()
            return

        try:
            with yt_dlp.YoutubeDL() as ydl:
                info = ydl.extract_info(url, download=False)
                formats = info.get('formats', [])

            self.video_formats = formats
            self.quality_spinner.options = [
                f"{fmt.get('resolution', 'Audio Only')} - {fmt['format_id']}" for fmt in formats
            ]
            self.status_label.value = "Qualities fetched successfully!"
            self.download_btn.disabled = False
            self.update()

        except Exception as e:
            self.status_label.value = f"Error: {e}"
            self.update()

    def download_video(self, e):
        url = self.url_input.value.strip()
        selected_quality = self.quality_spinner.value
        selected_format_id = selected_quality.split('-')[-1].strip()

        if not selected_format_id or selected_quality == 'Select Quality':
            self.status_label.value = "Error: Please select a quality!"
            self.update()
            return

        save_path = self.audio_dir if "Audio Only" in selected_quality else self.video_dir

        try:
            ydl_opts = {
                'format': selected_format_id,
                'outtmpl': f"{save_path}/%(title)s.%(ext)s",
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            self.status_label.value = f"Download successful! File saved in {save_path}"
            self.update()

        except Exception as e:
            self.status_label.value = f"Error: {e}"
            self.update()


def main(page):
    page.title = "Damtube"
    page.add(YouTubeDownloader())


ft.app(target=main)
