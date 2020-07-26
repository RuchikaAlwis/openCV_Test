from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import cv2

arr = np.array([1, 2, 3, 4, 5])
print(arr[2])
y = 3



def print_stuff():
    print("Calling print_stuff")
    print(y)
    z = 4
    print(z)
    print("exiting print_stuff")


print_stuff()  # we call print_stuff and the program execution goes to (***)
print(y)  # works fine
