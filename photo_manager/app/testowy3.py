from __future__ import print_function
from email.policy import default
from django.db import models

import binascii
import struct
from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster




def save():
    NUM_CLUSTERS = 5

    im = Image.open("/home/kamil/workplace/REST-photo-manager/photo_manager/media/photos/bunny.jpg").resize((150, 150))
    ar = np.asarray(im)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)
    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
    vecs, dist = scipy.cluster.vq.vq(ar, codes)         
    counts, bins = scipy.histogram(vecs, len(codes))    
    index_max = scipy.argmax(counts)                    
    peak = codes[index_max]
    colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')

    print(f'#{colour}')

save()