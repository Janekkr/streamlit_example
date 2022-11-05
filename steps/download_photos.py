from utils import get_cats
from zenml.steps import step


@step()
def download_cat_photos(number_of_photos_in_hundrets: int = 90) -> None:
    get_cats(number_of_photos_in_hundrets)
