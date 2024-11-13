import random
import numpy as np
import os

import torch
from PIL import Image
import torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch.optim as optim
import cv2

import zipfile


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print("Using device:", device)