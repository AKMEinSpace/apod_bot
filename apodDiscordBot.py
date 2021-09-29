# import discord
import shutil
from typing import Dict, Iterable
import requests
import os
import json
from dataclasses import dataclass

api_key = "YczXIfmC25Zf6qf5XhzCOIzbCtEtwwXIxUqRWP02"


@dataclass
class Img:
    title: str
    description: str
    img_data: bytes


def get_img(api_response: Dict[str, str]) -> Img:
    """
    Takes single response from the APOD api and gets the the gets
    img from url in response and constructs Img
    """
    img_url = api_response["url"]
    img_response = requests.get(img_url)
    # Validates if the responce is valid
    img_response.raise_for_status()

    img_title = api_response["title"]
    img_description = api_response["explanation"]
    return Img(img_title, img_description,  img_response.content)


def get_from_api(*, count=None) -> Iterable[Dict[str, str]]:
    """
    Returns list of responces from APOD Api as List[Dicts] 
    """
    base_url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'
    is_multiple_img = count and count > 1
    if is_multiple_img:
        url = f"{base_url}&count={count}"

    response = requests.get(url, stream=True)
    if is_multiple_img:
        return json.loads(response.content)
    else:
        return [json.loads(response.content)]


def save_img(img: Img, *, folder: str = None):
    save_name = f'{img.title}jpg'
    save_path = save_name

    if folder:
        save_path = f"{folder}\\{save_name}"

    with open(save_path, 'wb') as out_file:
        out_file.write(img.img_data)


def main():
    for response in get_from_api(count=2):
        img = get_img(response)
        save_img(img, folder="imgs")


if __name__ == "__main__":
    main()
