# Playing-Card-Classifier
Project for CSE 5524 Computer Vision

Findings
- Aspect ratio of standard playing card is 3.5 x 2.5, height x width
- Plain subtraction of pixels results in unintended results with uint8, you want to use cv2.absdiff()
- Compressed formats take a longer time to read, use uncompressed formats that use a larger space on disk but shorter processing time
- Converting images to black and white produces a better result than with color


Missing 37-39, 41-46, 49, 51
Training
- [x] Convert images from heic to jpg
- [x] Determine a good size to crop the cards
- [x] Use code to crop from the center 

Testing
- [ ] Classify playing cards of the same dimensions
- [ ] Classify playing cards of smaller dimension
- [ ] Classify playing cards of larger dimension
- [ ] Classify a playing card with multiple different backgrounds
- [ ] Classify multiple playing cards in a single frame
- [ ] Classify rotated playing cards
- [ ] Classify partial playing cards
- [ ] Classify playing cards in a video

Algorithm
- [x] Take each test image and convert to binary
- [x] Compare with all ground truth images and output those over 0.5
- [ ] Bonus: Use Canny Edge Detection to preprocess images to get rectangles with aspect ratio of 1.4
- [ ] Bonus: Rotate rectangular images to horizontal alignment
- [ ] Bonus: Orient and scale images to specified size using gaussian pyramid
- [ ] Bonus: Save images into an uncompressed format like .bmp to save on computation time

Potential
- [ ] NCC template matching with binary images an scaling from smaller image
- [ ] Noise removal by binary morphology and removing small regions