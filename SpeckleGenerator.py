import cv2
import numpy as np
import random

height = 3036
width = 4024
mu = 127
sigma = 1
#sample = np.random.normal(loc=mu, scale=sigma, size=(height * width))
sample = sigma * np.random.randn(height * width) + mu
print(sample)
print(np.average(sample))
print(np.sqrt(np.var(sample)))
blank = np.zeros((height,width,3))
num = 0
for h in range(len(blank)):
    for w in range(len(blank[h])):
        blank[h][w] += sample[num]
        num += 1
cv2.imwrite('blank.png',blank)

print("Success")
print(len(blank))
print(len(blank[0]))
print(len(blank[0][0]))