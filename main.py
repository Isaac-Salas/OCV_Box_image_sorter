import cv2
import glob
import shutil
import os
import matplotlib.pyplot as plt

# Path to images folder
path = "images/2026-10-22/*.jpg"



# Load base image and images list in grayscale
base = cv2.imread("base.jpeg", 0)
images = [[f,cv2.imread(f,0)] for f in glob.glob(path) if cv2.imread(f,0) is not None]

# Initialize folder structure
def init_folders():
    os.makedirs("single_box", exist_ok=True)
    os.makedirs("not_single_box", exist_ok=True)

# Calculate percentage and return -> difference and difference percentage
def calculate_percentage(base_image, current_image):
    
    #Resize to make sure size is the same as base_image
    current_image = cv2.resize(current_image, (base_image.shape[1], base_image.shape[0]))
    
    # Calculate absolute difference
    diff = cv2.absdiff(base_image, current_image)
    
    # Threshold to remove noise (e.g., compression artifacts)
    # Pixels with difference > 25 become white (255), others black (0)
    _, mask = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    
    # Calculate percentage of changed pixels
    total_pixels = base_image.size  # width * height
    changed_pixels = cv2.countNonZero(mask)
    percentage_change = (changed_pixels / total_pixels) * 100
    
    return diff, percentage_change

# Use 'Calculate percentage' to evaluate what folder to put the images onto
def sort_images_in_folders():
    for path,image in images:
        diff_img, ch_per = calculate_percentage(base, image)
        print(f"Percentage of image changed: {ch_per:.2f}%")
        show_image_difference(base, diff_img, ch_per)
        if ch_per > 15:
            shutil.move(path, 'not_single_box')
            print('Moved to not single!')
        else:
            shutil.move(path, 'single_box')
            print('Moved to single box!')
        
#Show base + diff image, and use the change percentage as title
def show_image_difference(base_image, difference_image, change_percentage):
    plt.title(f'Change: %{change_percentage:.2f}')
    plt.imshow(base_image + difference_image)
    plt.show()
    plt.close()
        

init_folders()
sort_images_in_folders()
        
        
        
    


