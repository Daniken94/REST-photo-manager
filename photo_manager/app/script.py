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
    """
    Function save images from external api
    """
    response = requests.get(url, stream=True)
    with open(title_dow, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
        shutil.move(src_path, dst_path)
    del response


def color(path):
        """
        Function for load dominant color from image. Image must by .jpg/.jpeg format.
        """
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
    """
    Load data from JSON file
    """
    file = os.path.abspath('/home/kamil/workplace/REST-photo-manager/photo_manager/app/fixtures/photos2.json')
    json_data=open(file).read()
    json_obj = json.loads(json_data)

    def validate_string(val):
        if val != None:
            if type(val) is int:
                return str(val).encode('utf-8')
            else:
                return val

    # Connect to database
    conn = psycopg2.connect(
        host="localhost",
        database="photo_db",
        user="postgres",
        password="postgres")

    cursor = conn.cursor()

    for i, item in enumerate(json_obj):
        # Loop for iterate by each object in JSON file
        # Get title
        title = validate_string(item.get("title", None))
        title_dow = title + ".png"
        title_dow_jpeg = title + ".jpeg"

        # Get albumId
        albumId = int(validate_string(item.get("albumId", None)))

        # Get url
        url = validate_string(item.get("url", None))
        url_download = url + ".png"

        # Replace files to correct place after download
        photo_path_raw = "/home/kamil/workplace/REST-photo-manager/photo_manager/"
        photo_path = "/home/kamil/workplace/REST-photo-manager/photo_manager/photos/"
        photo_path_png = "/home/kamil/workplace/REST-photo-manager/photo_manager/media/photos_png/"
        src_path = photo_path_raw + title_dow
        dst_path = photo_path_png + title_dow

        # Use function to download images from API
        save_image(url_download, title_dow, src_path, dst_path)

        # Images from API has
        Image.open(photo_path_png + title_dow).convert('RGB').save(photo_path_png + title_dow)
        change_format = Image.open(photo_path_png + title_dow, mode='r', formats=None)
        change_format.save(photo_path + title_dow_jpeg, format=None)

        # Use function to get color from image
        dom_colour = color(dst_path)
        img = Image.open(dst_path)

        # Get image path to save in DB
        localdata = f"photos/{title_dow}"

        # Create cursor
        cursor.execute("INSERT INTO app_photo (title, albumId, width, height, dom_colour, image, url) VALUES (%s, %s, %s, %s, %s, %s, %s)", (title, albumId, img.width, img.height, dom_colour, localdata, url))


    # Close connection
    conn.commit()
    conn.close()

    # Delete all from png dictionary
    for f in os.listdir(photo_path_png):
        os.remove(os.path.join(dir, f))

save_object()

