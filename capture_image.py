import cv2
import os

# Define the folder where the image will be saved
def capture_image():
    save_folder = 'captured_images'
    os.makedirs(save_folder, exist_ok=True)
    
    # Initialize the webcam (0 is usually the default camera)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break
        
        # Display the live video feed
        cv2.imshow('Webcam Feed - Press SPACE to capture, ESC to exit', frame)
    
        # Wait for key press
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC key to exit
            break
        elif key == 32:  # SPACE key to capture image
            # Define the path to save the image
            img_name = os.path.join(save_folder, 'captured_image.jpg')
            # Save the captured image
            cv2.imwrite(img_name, frame)
            print(f"Image saved to {img_name}")
            break
        
    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()