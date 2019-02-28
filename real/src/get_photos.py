# -*- coding: utf-8 -*-
"""
@author: Antoine
"""
import numpy as np


def get_photos(list_of_photos):
    results = []
    vertical_pictures = []

    for i, photo in enumerate(list_of_photos):
        if (photo.orientation === "V"):
            vertical_pictures.append(photo)
        else:
            results.append(photo)

    return results