from sklearn import datasets

import matplotlib.pyplot as plt

digits = datasets.load_digits()

#We set the configs of the window
plt.figure(1, figsize=(5, 5))

#We give an image to function that has 8x8 size 
plt.imshow(digits.images[0], cmap=plt.cm.gray_r, interpolation="nearest")

#Finally we show the window
plt.show()