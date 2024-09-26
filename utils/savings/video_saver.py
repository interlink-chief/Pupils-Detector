import os
import cv2


class VideoSaver:
    def __init__(self, output_folder):
        self.output_folder = output_folder
        self.video_writer = None
        self.left_video_writer = None
        self.right_video_writer = None

    def initialize_video_writer(self, output_folder, frame_width, frame_height, frame_rate, video_name):
        details_folder = os.path.join(output_folder, f'details_for_{video_name}', 'screen_frames')
        os.makedirs(details_folder, exist_ok=True)

        screen_main_frame_folder = os.path.join(details_folder, 'main_screen_frame')
        os.makedirs(screen_main_frame_folder, exist_ok=True)
        screen_main_frame_path = os.path.join(screen_main_frame_folder, f'main_frame_{video_name}.mp4')

        left_folder = os.path.join(details_folder, f'left_screen_frame')
        os.makedirs(left_folder, exist_ok=True)
        left_video_path = os.path.join(left_folder, f'left_eye_{video_name}.mp4')

        right_folder = os.path.join(details_folder, f'right_screen_frame')
        os.makedirs(right_folder, exist_ok=True)
        right_video_path = os.path.join(right_folder, f'right_eye_{video_name}.mp4')

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # XVID

        video_writer = cv2.VideoWriter(screen_main_frame_path, fourcc, frame_rate, (frame_width, frame_height))
        left_video_writer = cv2.VideoWriter(left_video_path, fourcc, frame_rate, (frame_width // 2, frame_height))
        right_video_writer = cv2.VideoWriter(right_video_path, fourcc, frame_rate, (frame_width // 2, frame_height))

        return video_writer, left_video_writer, right_video_writer

    def record_frame(self, video_writer, left_video_writer, right_video_writer, frame):
        if video_writer is not None:
            video_writer.write(frame)

        if left_video_writer is not None:
            left_frame = frame[:, :frame.shape[1] // 2]
            left_video_writer.write(left_frame)

        if right_video_writer is not None:
            right_frame = frame[:, frame.shape[1] // 2:]
            right_video_writer.write(right_frame)

    def release_video_writer(self, video_writer, left_video_writer, right_video_writer):
        if video_writer is not None:
            video_writer.release()

        if left_video_writer is not None:
            left_video_writer.release()

        if right_video_writer is not None:
            right_video_writer.release()
