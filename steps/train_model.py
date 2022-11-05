from zenml.steps import step
from image_formatting import crop_and_scale
import torch
from torch.utils.data import Dataset
from torchvision import transforms
import os
import pandas as pd
from image_label_creator import save_files_list
from torch.utils.data import DataLoader
import torch.nn as nn
import time
import numpy as np
from PIL import Image
import resnet
from CustomImageDataset import CustomImageDataset
from scipy import spatial


@step()
def train_model(model: nn.Module, device: str, image_dataset: Dataset) -> nn.Module:
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)
    dataloader = DataLoader(image_dataset, batch_size=16, shuffle=True)
    for epoch in range(3):
        start = time.time()
        for data in dataloader:
            img, _ = data
            img = img.to(device)
            # img = img.view(img.size(0), -1)
            optimizer.zero_grad()
            recon = model(img)
            loss = criterion(recon, img)
            loss.backward()
            optimizer.step()

    torch.save(model.state_dict(), "../saved_models/deep_CNN_v3.pth")
