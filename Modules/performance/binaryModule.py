import cv2
import numpy as np
from concurrent import futures


def binaryModule(frame, initial_threshold=0):
    threshold_value = initial_threshold

    def process_region(region):
        nonlocal threshold_value
        gray_frame = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

        brightness = np.mean(gray_frame)
        threshold = threshold_value + int((brightness - 77) / 2)

        _, threshold = cv2.threshold(gray_frame, threshold, 255, cv2.THRESH_BINARY_INV, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)

        kernel = np.ones((3, 3), np.uint8)
        opened = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)
        closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)
        frame_threshold = cv2.medianBlur(closed, 7)

        return frame_threshold

    height, width = frame.shape[:2]
    num_threads = cv2.getNumberOfCPUs()
    blocks = []

    for i in range(num_threads):
        start_y = int(i * height / num_threads)
        end_y = int((i + 1) * height / num_threads)

        block = frame[start_y:end_y, :]
        blocks.append(block)

    with futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(process_region, blocks))

    return np.vstack(results)
