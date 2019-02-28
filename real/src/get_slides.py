# -*- coding: utf-8 -*-
"""
@author: Antoine
"""
import numpy as np


class Slide():
    def __init__(self, photo_ids, tags):
        self.photo_ids = photo_ids
        self.tags = set(tags)

def get_common_tags(photo1, photo2):
    common_tags = []
    for tag in photo1.tags:
        common_tags.append(tag)
    for tag in photo2.tags:
        if tag not in common_tags:
            common_tags.append(tag)
    
    return common_tags
            

def get_slides(list_of_photos):
    results = []
    vertical_photos = []

    for i, photo in enumerate(list_of_photos):
        if (photo.orientation == "V"):
            vertical_photos.append(photo)
        else:
            slide = Slide([photo.photo_id], photo.tags)
            results.append(slide)

    for i in range(len(vertical_photos) // 2):
        vertical_photo = vertical_photos.pop()
        return_photo = vertical_photos[0]
        score = len(get_common_tags(vertical_photo, return_photo))
        for i_test, test_photo in enumerate(vertical_photos):
            new_score = len(get_common_tags(vertical_photo, return_photo))
            if new_score > score:
                score = new_score
                return_photo = test_photo
        
        best_score_photo = vertical_photos.pop(i_test)

        photo_ids = [vertical_photo.photo_id, best_score_photo.photo_id]
        common_tags = get_common_tags(vertical_photo, best_score_photo)
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
        Photo('V', ['A', 'B', 'C'], 1),
        Photo('V', ['E', 'B', 'C'], 2),
        Photo('H', ['A', 'B', 'C'], 3),
        Photo('V', ['D', 'U'], 4),
        Photo('V', ['R', 'T', 'E'], 5),
    ]
    slides = get_slides(list_of_photos)