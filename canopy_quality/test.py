import numpy as np
from canopy_quality import treenet
import torch
import matplotlib.pyplot as plt
import numpy as np
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from torch.autograd import Variable
from torchmetrics.classification import BinaryJaccardIndex
from utils import custom_replace
from data import batch_data_clean
import pooch



# test numpy array
# load model
device = "cuda" if torch.cuda.is_available() else "cpu"

# load model
model = treenet_ms()

##predict on random image
image = np.random.randint(255, size=(14, 240, 240), dtype=np.uint8) ## create 14 band image
y = model.predict(np_image=image)

# predict on batch with rgb
model = treenet_rgb()

images = np.random.randint(255, size=(25, 3, 240, 240), dtype=np.uint8) ## create 3 band image
y = model.predict_batch(images, batch_size=16)

# predict on actual image
model = treenet_ms()
a= np.load("../example_data/ms/P_1_X0_1_X1_240_Y0_1_Y1_240_113.npy",allow_pickle=True)
a = a[:14]
print(a.shape)
y = model.predict(np_image=a)