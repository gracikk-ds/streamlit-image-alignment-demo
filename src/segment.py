"""Segmentor"""
from typing import Tuple, Optional

import cv2
import numpy as np


# pylint: disable=too-many-locals
def align_and_process_image(input_image: np.ndarray) -> Tuple[Optional[np.ndarray], Optional[np.ndarray]]:
    """
    Align and process an input image to extract the metal element.

    Args:
        input_image (PIL.Image): The input image to be processed.

    Returns:
        tuple: A tuple containing the following:
            - numpy.ndarray: The processed image with the metal element extracted.
            - numpy.ndarray: Statistics related to the processed image.
            These statistics represent the sum of pixel values along each row of the processed image.
            It helps identify the length and width of the metal element.
    """
    # Load the image
    image = input_image.astype(np.uint8)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise and improve edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform edge detection using Canny
    edges = cv2.Canny(blurred, threshold1=50, threshold2=150)

    # Find contours in the edges
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a mask for the metal element
    mask = np.zeros_like(image)

    # Filter and draw the largest contour (assuming it's the metal element)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        cv2.drawContours(mask, [largest_contour], -1, (255, 255, 255), thickness=cv2.FILLED)

        # Apply the mask to the original image
        result = cv2.bitwise_and(image, mask)
        result[result > 1] = 255

        # Get the bounding ellipse of the bolt
        ellipse = cv2.fitEllipse(largest_contour)

        # Extract the angle of the major axis of the ellipse
        angle = ellipse[2]

        # Rotate the image
        height, width = result.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
        rotated_image = cv2.warpAffine(result, rotation_matrix, (width, height))

        stats = np.sum(rotated_image // 255, axis=1)
        stats = stats[stats > 0]

        if stats[50] > stats[-50]:
            rotated_image = cv2.rotate(rotated_image, cv2.ROTATE_180)

        return rotated_image, stats
    return (None, None)
