import os
import tempfile
import zipfile
import tornado.ioloop
import tornado.web
from mainModule import MainModule
from utils.exceptions.exceptions import InvalidVideoFile, NoVideoFileSelected

class ProcessVideoHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            video_files = self.request.files.get('video')
            if not video_files:
                raise NoVideoFileSelected('No video file selected.')

            video_file = video_files[0]
            video_filename = video_file['filename']

            if not video_filename.endswith('.mp4'):
                raise InvalidVideoFile('Invalid video file. Only .mp4 files are allowed.')

            input_videos_folder = './input_videos'
            os.makedirs(input_videos_folder, exist_ok=True)

            video_path = os.path.join(input_videos_folder, video_filename)
            with open(video_path, 'wb') as f:
                f.write(video_file['body'])

            video_player = MainModule(video_path, 1, output_folder='./tmp/output_videos')
            video_player.play()

            processed_video_folder = video_player.output_folder

            temp_folder = tempfile.mkdtemp()

            zip_path = os.path.join(temp_folder, f'details_for_{video_player.video_name}.zip')
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(processed_video_folder):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, processed_video_folder)
                        zipf.write(file_path, arcname)

            self.set_header('Content-Type', 'application/octet-stream')
            self.set_header('Content-Disposition', 'attachment; filename=output_folder.zip')

            with open(zip_path, 'rb') as f:
                while True:
                    chunk = f.read(4096)
                    if not chunk:
                        break
                    self.write(chunk)
                    self.flush()

            self.finish()

            os.remove(temp_folder)

        except NoVideoFileSelected as e:
            self.set_status(e.status_code)
            self.write({'error': e.message})

        except InvalidVideoFile as e:
            self.set_status(e.status_code)
            self.write({'error': e.message})

        except Exception as e:
            self.set_status(500)
            self.write({'error': 'An unexpected error occurred.'})


def make_app():
    return tornado.web.Application([
        (r"/process_video", ProcessVideoHandler),
    ])


if __name__ == "__main__":
    PORT = 5001
    app = make_app()
    app.listen(PORT)
    print(f'Server has been started on port: {PORT}')
    tornado.ioloop.IOLoop.current().start()
