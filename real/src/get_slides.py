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
            slide = Slide(str(photo.photo_id), photo.tags)
            results.append(slide)


    for i in range(len(vertical_photos) // 2):
        photo1 = vertical_photos[2 * i]
        photo2 = vertical_photos[2 * i + 1]
        common_tags = photo1.tags
        for tag in photo2.tags:
            if tag not in common_tags:
                common_tags.append(tag)
        
        photo_ids = ' '.join(map(str, [photo1.photo_id, photo2.photo_id]))
        slide = Slide(photo_ids, common_tags)
        results.append(slide)

    return results


if __name__ == "__main__":
    class Photo():
        def __init__(self, orientation, tags, photo_id):
            self.orientation = orientation
            self.tags = tags
            self.photo_id = photo_id

    list_of_photos = [
        Photo('H', ['A', 'B', 'C'], 1),
        Photo('V', ['A', 'B', 'C'], 2),
        Photo('V', ['D', 'C'], 3),
    ]