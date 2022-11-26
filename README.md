# Playing-Card-Classifier
Project for CSE 5524 Computer Vision

Findings
- Aspect ratio of standard playing card is 3.5 x 2.5, height x width
- Plain subtraction of pixels results in unintended results with uint8, you want to use cv2.absdiff()
- Compressed formats take a longer time to read, use uncompressed formats that use a larger space on disk but shorter processing time
- Converting images to black and white produces a better result than with color


Training
- [x] Convert images from heic to jpg
- [x] Determine a good size to crop the cards
- [x] Use code to crop from the center 

Testing
- [ ] Classify playing cards of the same dimensions
- [ ] Classify playing cards of smaller dimension
- [ ] Classfiy playing cards of larger dimension
- [ ] Classify a playing card with multiple different backgounds
- [ ] Classify multiple playing cards in a single frame
- [ ] Classify rotated playing cards
- [ ] Classify partial playing cards
- [ ] Classfiy playing cards in a video

Algorithm
- [x] Crop the test image from the center
- [x] Compare with all ground truth images and output those over 0.5
- [ ] Bonus: Scale images to specified size using gaussian pyramid
- [ ] Bonus: Add corner detection
- [ ] Bonus: Add edge detection
- [ ] Bonus: Combine both to crop out closed shapes within the image
- [ ] Bonus: Rotate images to horizontal alignment
- [ ] Bonus: Save images into an uncompressed format like .bmp to save on computation time
- [ ] Count the number of non white areas, ncc matching