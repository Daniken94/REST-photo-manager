import os, json, postgres, psycopg2
import urllib.request





import shutil

import requests

url = 'https://via.placeholder.com/600/92c952.png'
response = requests.get(url, stream=True)
with open('img.png', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
    src_path = "/home/kamil/workplace/REST-photo-manager/photo_manager/img.png"
    dst_path = "/home/kamil/workplace/REST-photo-manager/photo_manager/media/photos/img.png"
    shutil.move(src_path, dst_path)
del response



# # read JSON file which is in the next parent folder
# file = os.path.abspath('/home/kamil/workplace/REST-photo-manager/photo_manager/app/fixtures/photos.json')
# json_data=open(file).read()
# json_obj = json.loads(json_data)

# def validate_string(val):
#    if val != None:
#         if type(val) is int:
#             #for x in val:
#             #   print(x)
#             return str(val).encode('utf-8')
#         else:
#             return val


# conn = psycopg2.connect(
#     host="localhost",
#     database="photo_db",
#     user="postgres",
#     password="postgres")

# cursor = conn.cursor()

# # parse json data to SQL insert
# for i, item in enumerate(json_obj):
#     title = validate_string(item.get("title", None))
#     albumId = int(validate_string(item.get("albumId", None)))
#     url = validate_string(item.get("url", None))
#     cursor.execute("INSERT INTO app_photo (title, albumId, url) VALUES (%s,	%s,	%s)", (title, albumId, url))


# conn.commit()
# conn.close()