import cv2.cv2 as cv2
import numpy as np
from pyzbar import pyzbar
from typing import (
    Union,
    Iterable,
)


def get_isbn(image: Union[str, np.ndarray], dsize=(640, 480), morph_ksize: tuple[int, int] = (3, 3),
             top_k: int = 3) -> Iterable[np.ndarray]:
    if isinstance(image, str):
        image = cv2.imread(image)
        image = cv2.resize(image, dsize)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gradX = cv2.Sobel(gray, cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradY = cv2.Sobel(gray, cv2.CV_32F, dx=0, dy=1, ksize=-1)

    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)

    blurred = cv2.blur(gradient, (4, 4))
    _, thresh = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, morph_ksize)
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    closed = cv2.erode(closed, kernel, iterations=4)

    cnts, *_ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

    for cnt in cnts[:top_k]:
        rect = cv2.minAreaRect(cnt)
        box = np.int0(cv2.boxPoints(rect))
        yield box


def decode_isbn(image: np.ndarray, boxes: Iterable[np.ndarray]) -> Iterable[pyzbar.Decoded]:
    for box in boxes:
        x_min, x_max, y_min, y_max = np.min(box[:, 0]), np.max(box[:, 0]), np.min(box[:, 1]), np.max(box[:, 1])
        yield from pyzbar.decode(image[y_min:y_max, x_min:x_max])


"""
+________|
| Item A
|--------|
|          <--
|--------|
| Item C
+--------|

            +---+
            |   |
            +---+
Item B

1) Robot waits for webcam input
2) Once the robot gets the webcam input, identify the ISBN
3) Lookup the ISBN and find where the book should be 
4) Get the book to the right box
"""