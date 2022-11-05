from zenml.steps import step
from image_formatting import crop_and_scale
import torch
from torchvision import transforms
import os
import pandas as pd
from image_label_creator import save_files_list
from torch.utils.data import DataLoader
import torch.nn as nn
import time
import numpy as np
from PIL import Image
from Autoencoder import Autoencoder
from CustomImageDataset import CustomImageDataset
from scipy import spatial


@step()
def load_model() -> nn.Module, str:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = Autoencoder()
    model.load_state_dict(torch.load("../saved_models/deep_CNN_v3.pth"))
    model.eval()
    model.to(device)
    return model, device
