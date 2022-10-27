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



class Photo(models.Model):
    title = models.CharField(max_length=120)
    albumid = models.IntegerField(default=1)
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    dom_colour = models.CharField(max_length=80, blank=True, null=True)
    image = models.ImageField(upload_to="photos", height_field='height', width_field='width', blank=True, null=True)
    url = models.CharField(max_length=500, blank=True)


    def save(self, *args, **kwargs):
        NUM_CLUSTERS = 5

        im = Image.open(self.image).resize((150, 150))
        ar = np.asarray(im)
        shape = ar.shape
        ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)
        codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
        vecs, dist = scipy.cluster.vq.vq(ar, codes)         
        counts, bins = scipy.histogram(vecs, len(codes))    
        index_max = scipy.argmax(counts)                    
        peak = codes[index_max]
        colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')

        self.dom_colour = f'#{colour}'
        super(Photo, self).save(*args, **kwargs)


    def __str__(self):
            return f"{self.title}"