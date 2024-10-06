from astropy.io import fits
import numpy as np
import os
import fitsio
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

fitsDir = '/home/haider/snap/fitsData'
fitsFiles = [f for f in os.listdir(fitsDir) if f.endswith('.fits')]

image = []
for file in fitsFiles:
    filePath = os.path.join(fitsDir, file)

    with fits.open(filePath) as hdul:
        imageData = hdul[0].data
        image.append(imageData)
image = np.array(image)

images = image/image.max()

imageFlat = image.reshape(image.shape[0],-1)

