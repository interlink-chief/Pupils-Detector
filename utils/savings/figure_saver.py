import os

class FigureSaver:
    def __init__(self, output_folder):
        self.output_folder = output_folder

    def save_figure(self, video_name, ax):
        details_folder = os.path.join(self.output_folder, f'details_for_{video_name}')
        os.makedirs(details_folder, exist_ok=True)

        graphic_coords_folder = os.path.join(details_folder, f'graphic&coords_{video_name}')
        os.makedirs(graphic_coords_folder, exist_ok=True)

        graphic_folder = os.path.join(graphic_coords_folder, 'graphic')
        os.makedirs(graphic_folder, exist_ok=True)
        graphic_path = os.path.join(graphic_folder, f'graphic_{video_name}.png')

        ax.figure.savefig(graphic_path)
