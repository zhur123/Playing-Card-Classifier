import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
from time import time

import crop

goal_dim = (3500, 2500) # h x w, 3.5 x 2.5 ratio

test_path = './Test_Images'
ground_truth_path = './Ground_Truth_Cropped'

gt_images = []
def initialize():
    start = time()
    print('Initializing Algorithm...')
    global gt_images
    deck = []
    numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['spades', 'clubs', 'diamonds', 'hearts']
    for number in numbers:
        for suit in suits:
            deck.append(number + '_' + suit + '.jpg')
    deck.append('Back.jpg')
    deck.append('joker_color.jpg')
    deck.append('joker_black.jpg')
    print('Deck Initialization took', time()-start, 'seconds')
    start = time()
    for card_name in deck:
        gt_image = cv2.imread(os.path.join(ground_truth_path, card_name))
        gt_images.append((card_name, gt_image))
    print('Finished Initialization in ', time()-start, 'seconds') # Takes around 15-20 seconds

def find_best(test_image):
    diff_list = []
    # start = time()
    test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
    plt.imshow(test_image, cmap='gray')
    plt.show()
    for (card_name, gt_image) in gt_images:
        gt_image = cv2.cvtColor(gt_image, cv2.COLOR_BGR2GRAY)
        
        # print(gt_image.shape, test_image.shape)
        diff = cv2.absdiff(gt_image, test_image).sum()
        rotate_diff = cv2.absdiff(cv2.rotate(gt_image, cv2.ROTATE_180), test_image).sum()
        if rotate_diff < diff:
            diff_list.append((rotate_diff, card_name))
        else:
            diff_list.append((diff, card_name))
    # print('Comparing with other cards took', time()-start, 'seconds') # Takes around 60 seconds
    diff_list.sort()
    return diff_list

def test(image_name):
    initialize()
    image_path = os.path.join(test_path, image_name)
    test_image = crop.crop_image(image_path, goal_dim=goal_dim)
    print(test_image.shape)
    diff_list = find_best(test_image)
    percent = (diff_list[1][0] - diff_list[0][0]) / diff_list[1][0]
    print(image_name, 'is predicted to be', diff_list[0][1], 'with a difference of', diff_list[0][0], str(round(percent*100)) + '%')
    if percent <= 0.5:
        print('The next 5 possibilities are: ')
        for i in range(1, 6):
            print(diff_list[i])

def preprocess(test_path, goal_dim=goal_dim):
    test_image = cv2.imread(test_path)
    gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
    retval, thresh = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
    edges = cv2.Canny(thresh, 50, 100) # 50, 55 works relatively well
    kernel = np.ones((3, 3), np.uint8)
    transform1 = cv2.morphologyEx(edges, cv2.MORPH_DILATE, kernel, iterations=1)
    transform2 = cv2.morphologyEx(transform1, cv2.MORPH_OPEN, kernel, iterations=1)
    contours, heirarchy = cv2.findContours(transform2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cards = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 900 and h > 600:
            card = test_image[x:x+w, y:y+h]
            card = cv2.resize(card, (2500, 3500))
            cards.append(card)
    return cards

def main():
    initialize()
    for image_name in os.listdir(test_path):
        image_path = os.path.join(test_path, image_name)
        # cards = preprocess(image_path, goal_dim=goal_dim)
        # if len(cards) == 0:
        #     print('No playing cards detected')
        #     continue
        test_image = crop.crop_image(image_path, goal_dim=goal_dim)
        diff_list = find_best(test_image)
        percent = (diff_list[1][0] - diff_list[0][0]) / diff_list[1][0]
        print(image_name, 'is predicted to be', diff_list[0][1], 'with a difference of', diff_list[0][0], str(round(percent*100)) + '%')
        if percent <= 0.5:
            print('The next 5 possibilities are: ')
            for i in range(1, 6):
                print(diff_list[i])
        # for card in cards:
        #     # plt.imshow(card)
        #     # plt.show()
        #     diff_list = find_best(card)
        #     percent = (diff_list[1][0] - diff_list[0][0]) / diff_list[1][0]
        #     if percent > 0.5:
        #         print(image_name, 'is predicted to be', diff_list[0][1], 'with a difference of', diff_list[0][0], str(round(percent*100)) + '%')
        #     # if percent <= 0.5:
        #     #     print('The next 5 possibilities are: ')
        #     #     for i in range(1, 6):
        #     #         print(diff_list[i])

if __name__ == '__main__':
    # main()
    test('Test10.jpg')
    # preprocess('Test_Images/Test7.jpg')

    # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # cv2.imshow('image', cv2.resize(test_image, (700, 500)))
    # cv2.waitKey(0)