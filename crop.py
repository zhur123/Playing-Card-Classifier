import cv2
import os

def crop_images(original_path, cropped_path, goal_dim=(3500, 2500)):
    os.mkdir(cropped_path)
    for image_name in os.listdir(original_path):
        original_image_path = os.path.join(original_path, image_name)
        cropped_image_path = os.path.join(cropped_path, image_name)
        image = cv2.imread(original_image_path)
        mid = (image.shape[0]//2, image.shape[1]//2)
        cropped_image = image[mid[0]-goal_dim[0]//2:mid[0]+goal_dim[0]//2, mid[1]-goal_dim[1]//2:mid[1]+goal_dim[1]//2]
        cv2.imwrite(cropped_image_path, cropped_image)
        print('original size', image.shape)
        print(cropped_image_path, 'with dimension', cropped_image.shape, 'saved!')

def crop_image(image_path, goal_dim=(3500, 2500)):
    image = cv2.imread(image_path)
    mid = (image.shape[0]//2, image.shape[1]//2)
    cropped_image = image[mid[0]-goal_dim[0]//2:mid[0]+goal_dim[0]//2, mid[1]-goal_dim[1]//2:mid[1]+goal_dim[1]//2]
    return cropped_image

if __name__ == '__main__':
    original_path = './Ground_Truth_Original'
    cropped_path = './Ground_Truth_Cropped'
    goal_dim = (3500, 2500) # h x w, 3.5 x 2.5 ratio
    crop_images(original_path, cropped_path, goal_dim)