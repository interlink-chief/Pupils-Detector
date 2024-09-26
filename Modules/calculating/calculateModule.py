import numpy as np
import time


def calculateModule(left_eye_coords1, right_eye_coords1, left_eye_coords2, right_eye_coords2) -> int:
    left_eye_average_X = None
    left_eye_average_Y = None
    left_eye_average_R = None
    right_eye_average_X = None
    right_eye_average_Y = None
    right_eye_average_R = None
    # timestamp = time.ctime(time.time())

    if left_eye_coords1 is not None and left_eye_coords2 is not None:
        left_eye_average_X = np.array([left_eye_coords1[0], left_eye_coords2[0]]).mean()
        left_eye_average_Y = np.array([left_eye_coords1[1], left_eye_coords2[1]]).mean()
        left_eye_average_R = np.array([left_eye_coords1[2], left_eye_coords2[2]]).mean()
        # print('\033[96m' + f'Left eye average coordinates: (X: {left_eye_average_X}, Y: {left_eye_average_Y}, R: {left_eye_average_R}) - {timestamp}')
    # else:
        # print('\033[93mNo eye detected...\033[0m')

    if right_eye_coords1 is not None and right_eye_coords2 is not None:
        right_eye_average_X = np.array([right_eye_coords1[0], right_eye_coords2[0]]).mean()
        right_eye_average_Y = np.array([right_eye_coords1[1], right_eye_coords2[1]]).mean()
        right_eye_average_R = np.array([right_eye_coords1[2], right_eye_coords2[2]]).mean()
        # print('\033[94m' + f'Right eye average coordinates: (X: {right_eye_average_X}, Y: {right_eye_average_Y}, R: {right_eye_average_R}) - {timestamp}')
    # else:
        # print('\033[93mNo eye detected...\033[0m')
    
    return left_eye_average_X, left_eye_average_Y, right_eye_average_X, right_eye_average_Y, left_eye_average_R, right_eye_average_R