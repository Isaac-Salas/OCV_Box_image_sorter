import cv2
import glob
import shutil
import os
import matplotlib.pyplot as plt


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

# Use 'Calculate percentage' to evaluate what folder to put the images in
def sort_images_in_folders(single_treshold : float = 15, show_images : bool = False):
    for path,image in images:
        diff_img, ch_per = calculate_percentage(base, image)
        print(f"Percentage of image changed: {ch_per:.2f}%")
        is_single = evaluate_percentage(ch_per, single_treshold)
        if is_single:
            shutil.move(path, 'not_single_box')
            print('Moved to not single!')
        else:
            shutil.move(path, 'single_box')
            print('Moved to single box!')
        
        if show_images:
            show_image_difference(base, diff_img, ch_per, is_single)

def save_single_box_images(single_treshold : float = 15, show_images : bool = False,new_folder_name = '11/11/11'):
    image_count = 1
    for path,image in images:
        cropped_base = crop_image(base,crop_y_start,crop_y_end,crop_x_start,crop_x_end)
        cropped_image = crop_image(image,crop_y_start,crop_y_end,crop_x_start,crop_x_end)
        color_image = crop_image(cv2.imread(path),crop_y_start,crop_y_end,crop_x_start,crop_x_end)
        diff_img, ch_per = calculate_percentage(cropped_base, cropped_image)
        is_single = evaluate_percentage(ch_per, single_treshold)
        print(f"Percentage of image changed: {ch_per:.2f}%")
        os.makedirs(f"single_box/{new_folder_name}", exist_ok=True)
        if is_single:
            cv2.imwrite(f"single_box/{new_folder_name}/box_{image_count}.png", color_image)
            image_count += 1
        if show_images:
            show_image_difference(cropped_base, diff_img, ch_per, is_single)
        
        
def crop_image(image, y_start, y_end, x_start, x_end):
    cropped_img = image[y_start:y_end, x_start:x_end]
    return cropped_img


def evaluate_percentage(percentage, treshold):
    if percentage > treshold:
        return False
    else:
        return True
    
        
#Show base + diff image, and use the change percentage as title
def show_image_difference(base_image, difference_image, change_percentage, is_single):
    plt.title(f'Change: %{change_percentage:.2f}, Is Single Box: {is_single}')
    plt.imshow(base_image + difference_image)
    plt.show()
    plt.close()


        
# Path to images folder
path = "images/2026-10-23/*.jpg"

# Load base image and images list in grayscale
base = cv2.imread("base23.jpg", 0)
images = [[f,cv2.imread(f,0)] for f in glob.glob(path) if cv2.imread(f,0) is not None]

# Global vars for image cropping
crop_x_start = 790
crop_x_end = 1990
crop_y_start = 470
crop_y_end = 1670

init_folders()
#sort_images_in_folders(15,True)
save_single_box_images(44, False, '23/10/2026')

        
        
        
    


