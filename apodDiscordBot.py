# import discord
import shutil
import requests
import os
import json

api_key = "YczXIfmC25Zf6qf5XhzCOIzbCtEtwwXIxUqRWP02"

# print(api_key)


def get_from_api(*, count=None):
    base_url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'
    is_multiple_img = count and count > 1
    if is_multiple_img:
        url = f"{base_url}&count={count}"

    response = requests.get(url, stream=True)
    if is_multiple_img:
        return json.loads(response.content)
    else:
        return [json.loads(response.content)]
# print(json_content)


def save_img(response, *, folder=None):
    img_url = response["url"]
    img_name = f'{response["title"]}.jpg'
    img_response = requests.get(img_url)

    save_path = img_name
    if folder:
        save_path = f"{folder}\\{img_name}"

    with open(save_path, 'wb') as out_file:
        out_file.write(img_response.content)
    del img_response


for response in get_from_api(count=2):
    save_img(response, folder="imgs")
    # print(img["url"])

    # print(type(respons))
    # print(respons.content)
