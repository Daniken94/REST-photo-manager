from __future__ import print_function
from email.policy import default
from django.db import models
from PIL import Image

import binascii
import struct
from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster

import os, json, postgres, psycopg2
import urllib.request
import shutil
import requests


def save_image(url, title_dow, src_path, dst_path):
    response = requests.get(url, stream=True)
    with open(title_dow, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
        shutil.move(src_path, dst_path)
    del response


def color(path):
        NUM_CLUSTERS = 5

        im = Image.open(path).resize((150, 150))
        ar = np.asarray(im)
        shape = ar.shape
        ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)
        codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
        vecs, dist = scipy.cluster.vq.vq(ar, codes)         
        counts, bins = scipy.histogram(vecs, len(codes))    
        index_max = scipy.argmax(counts)                    
        peak = codes[index_max]
        colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
        col = f'#{colour}'
        return col


def save_object():
    file = os.path.abspath('/home/kamil/workplace/REST-photo-manager/photo_manager/app/fixtures/photos2.json')
    json_data=open(file).read()
    json_obj = json.loads(json_data)

    def validate_string(val):
        if val != None:
            if type(val) is int:
                return str(val).encode('utf-8')
            else:
                return val


    conn = psycopg2.connect(
        host="localhost",
        database="photo_db",
        user="postgres",
        password="postgres")

    cursor = conn.cursor()

    for i, item in enumerate(json_obj):
        title = validate_string(item.get("title", None))
        title_dow = title + ".png"
        title_dow_jpeg = title + ".jpeg"

        title = validate_string(item.get("title", None))
        title_dow = title + ".png"
        title_dow_jpeg = title + ".jpeg"
        src_path = f"/home/kamil/workplace/REST-photo-manager/photo_manager/{title_dow}"
        dst_path = f"/home/kamil/workplace/REST-photo-manager/photo_manager/media/photos_png/{title_dow}"
        albumId = int(validate_string(item.get("albumId", None)))
        url = validate_string(item.get("url", None))
        url_download = url + ".png"
        save_image(url_download, title_dow, src_path, dst_path)

        Image.open(f'/home/kamil/workplace/REST-photo-manager/photo_manager/media/photos_png/{title_dow}').convert('RGB').save(f'/home/kamil/workplace/REST-photo-manager/photo_manager/media/photos_png/{title_dow}')
        change_format = Image.open(f"/home/kamil/workplace/REST-photo-manager/photo_manager/media/photos_png/{title_dow}", mode='r', formats=None)
        change_format.save(f"/home/kamil/workplace/REST-photo-manager/photo_manager/media/photos/{title_dow_jpeg}", format=None)

        dom_colour = color(dst_path)
        img = Image.open(dst_path)

        localdata = f"photos/{title_dow}"
        cursor.execute("INSERT INTO app_photo (title, albumId, width, height, dom_colour, image, url) VALUES (%s, %s, %s, %s, %s, %s, %s)", (title, albumId, img.width, img.height, dom_colour, localdata, url))

        dir = '/home/kamil/workplace/REST-photo-manager/photo_manager/media/photos_png'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

    conn.commit()
    conn.close()

save_object()
