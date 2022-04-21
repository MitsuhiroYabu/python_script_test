import cv2
import numpy as np

img = cv2.imread("blank.png")
N = img.shape[0] * img.shape[1]
print(N)
sample = np.zeros(N)
h = None
w = None
num = 0
for h in range(len(img)):
    for w in range(len(img[0])):
        sample[num] = img[h][w][0]
        num += 1
        #print(num)

print(np.average(sample))
print(np.sqrt(np.var(sample)))
print(sample)
