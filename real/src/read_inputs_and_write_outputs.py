# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:59:50 2019

@author: Antoine
"""
import os
import models
import numpy as np


out_folder = '../out/'
try:
    os.makedirs(out_folder)
except OSError:
    if not os.path.isdir(out_folder):
        raise

landscape_paths = [
    '../in/a_example.txt',
    '../in/b_lovely_landscapes.txt',
    '../in/c_memorable_moments.txt',
    '../in/d_pet_pictures.txt',
    '../in/e_shiny_selfies.txt',
]

class Photo():
    def __init__(self, orientation, tags):
        self.orientation = orientation
        self.tags = tags

for landscape_path in landscape_paths:
    print ('Landscape file: %s' % landscape_path)
    f = open(landscape_path, mode='r')
    
    header = f.readline()
    row_count = int(header)
    
    photos = []
    for i in range(row_count):
        elts = list(map(str.rstrip, f.readline().split(' ')))
        photo = Photo(elts[0], elts[2:])
        photos.append(photo)
    f.close()

    results = models.greedy_heuristic(photos)

    f = open(out_folder + landscape_path.split('/')[-1], mode='w')
    f.write(str(len(results)) + '\n')
    f.writelines(map(lambda x: ' '.join(map(str, x)) + '\n', results))
    f.close()
    print ('\n')
