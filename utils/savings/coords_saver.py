import os
import csv


class CoordinatesSaver:
    def __init__(self, output_folder):
        self.output_folder = output_folder

    def save_coordinates(self, video_name, left_eye_coords, right_eye_coords):
        details_folder = os.path.join(self.output_folder, f'details_for_{video_name}')
        os.makedirs(details_folder, exist_ok=True)

        graphic_coords_folder = os.path.join(details_folder, f'graphic&coords_{video_name}')
        os.makedirs(graphic_coords_folder, exist_ok=True)

        coordinates_folder = os.path.join(graphic_coords_folder, 'coordinates')
        os.makedirs(coordinates_folder, exist_ok=True)
        coordinates_file_path = os.path.join(coordinates_folder, f'coordinates_{video_name}.csv')

        with open(coordinates_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            for i in range(len(left_eye_coords)):
                if left_eye_coords[i] is not None:
                    x1, y1, r1 = left_eye_coords[i]
                    writer.writerow(['Left eye\'s coordinates: ' + f'X: {x1}', f' Y: {y1}', f' R: {r1}'])
                else:
                    writer.writerow(['No eye detected...'])
            
            for i in range(len(right_eye_coords)):
                if right_eye_coords[i] is not None:
                    x2, y2, r2 = right_eye_coords[i]
                    writer.writerow(['Right eye\'s coordinates: ' + f'X: {x2}', f' Y: {y2}', f' R: {r2}'])
                else:
                    writer.writerow(['No eye detected...'])
