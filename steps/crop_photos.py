from utils import crop_and_scale
from zenml.steps import step
import os
from PIL import Image


@step()
def format_photos(directory: str = None) -> None:
    if directory is None:
        directory = 'cats'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if (img := Image.open(f).convert('RGB')).format != "GIF":
            crop_and_scale(img).save(f)
        else:
            os.remove(f)
