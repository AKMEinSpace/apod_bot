import discord, shutil, requests, os,json

api_key = "YczXIfmC25Zf6qf5XhzCOIzbCtEtwwXIxUqRWP02"

#print(api_key)
url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&count=2'
response = requests.get(url, stream=True)
json_content = json.loads(response.content)
#print(json_content)


for img in json_content:

    #print(img["url"])

    respons = requests.get(img["url"])

    #print(type(respons))
    #print(respons.content)

    with open(f'{json_content.index(img)}img.jpg', 'wb') as out_file:
        out_file.write(respons.content)
    del respons

