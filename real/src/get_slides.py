# -*- coding: utf-8 -*-
"""
@author: Antoine
"""
import numpy as np


class Slide():
    def __init__(self, photo_ids, tags):
        self.photo_ids = photo_ids
        self.tags = tags

def get_slides(list_of_photos):
    results = []
    vertical_photos = []

    for i, photo in enumerate(list_of_photos):
        if (photo.orientation == "V"):
            vertical_photos.append(photo)
        else:
            slide = Slide(photo.photo_id, photo.tags)
            results.append(slide)

    
    for i, photo in enumerate(len(vertical_photos) // 2):
        photo1 = vertical_photos[i]
        photo2 = vertical_photos[i + 1]
        common_tags = photo1.tags
        for tag in photo2.tags:
            if tag not in common_tags:
                common_tags.append(tag)
        
        photo_ids = ' '.join(map(str, [photo1.photo_id, photo1.photo_id]))
        slide = Slide(photo_ids, common_tags)
        results.append(slide)

    return results