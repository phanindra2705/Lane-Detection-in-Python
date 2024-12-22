import cv2
import numpy as np
import pygame

# Initialize PyGame for sound alerts
pygame.init()
pygame.mixer.init()
alert_sound = pygame.mixer.Sound('/Users/phanindranaiduguntamukkala/Desktop/boop-741-mhz-39314.wav')  # Place an alert.wav file in the same directory

def play_alert():
    """Play an alert sound."""
    alert_sound.play()

def region_of_interest(img, vertices):
    """Applies an image mask."""
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_lines(img, lines):
    """Draw lines on the image."""
    if lines is None:
        return

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 5)

def process_frame(frame):
    """Processes a single video frame."""
    height, width = frame.shape[:2]

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection using Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Region of interest
    vertices = np.array([[(50, height), (width // 2 - 50, height // 2 + 50),
                          (width // 2 + 50, height // 2 + 50), (width - 50, height)]], dtype=np.int32)
    roi = region_of_interest(edges, vertices)

    # Detect lines using Hough Transform
    lines = cv2.HoughLinesP(roi, 1, np.pi / 180, threshold=50, minLineLength=40, maxLineGap=150)

    # Create a blank image to draw lines on
    line_image = np.zeros_like(frame)
    draw_lines(line_image, lines)

    # Combine the original frame with the line image
    combined = cv2.addWeighted(frame, 0.8, line_image, 1, 1)

    # Check for lane deviation
    if lines is None:
        play_alert()

    return combined

def main():
    """Main function to run the lane detection."""
    cap = cv2.VideoCapture(0)  # Use webcam or replace with video file path

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame = process_frame(frame)

        cv2.imshow('Lane Detection', processed_frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
