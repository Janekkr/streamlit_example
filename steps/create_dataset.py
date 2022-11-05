from zenml.steps import step
from torch.utils.data import Dataset
import pandas as pd
from PIL import Image
import os
from image_formatting import crop_and_scale
import os
from os import listdir
from os.path import isfile, join
import pandas as pd
import pathlib


def get_files_list(directory):
    # get list of files in directory and subdirectories
    files_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if not file.endswith(".gif"):
                p = pathlib.Path(os.path.join(root, file))
                files_list.append(pathlib.Path(*p.parts[1:]))
    return files_list


def save_files_list(directory):
    df = pd.DataFrame(get_files_list(directory))
    df.to_csv("../files_list.csv", index=False)


@step()
def create_dataset(): -> Dataset
    save_files_list("../cats")
    image_dataset = CustomImageDataset(
        annotations_file="../files_list.csv", img_dir="../cats", transform=transforms.ToTensor()
    )
    return image_dataset
