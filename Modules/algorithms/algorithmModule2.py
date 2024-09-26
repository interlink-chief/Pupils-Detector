import cv2


def algorithmModule2(threshold, frame, circle_color=(255, 0, 0)) -> int:
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    left_eye_coords2 = None
    right_eye_coords2 = None

    for cnt in contours:
        if len(cnt) < 3:
            continue

        (x, y), r = cv2.minEnclosingCircle(cnt)
        center = (int(x), int(y))
        radius = int(r)

        if x < frame.shape[1] / 2:
            cv2.circle(frame, center, radius, circle_color, 2)
            left_eye_coords2 = (x, y, r)
        else:
            cv2.circle(frame, center, radius, circle_color, 2)
            right_eye_coords2 = (x, y, r)

    return left_eye_coords2, right_eye_coords2