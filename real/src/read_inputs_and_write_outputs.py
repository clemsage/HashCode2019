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
    '../a_example.txt',
    '../b_lovely_landscapes.txt',
    '../c_memorable_moments.txt',
    '../d_pet_pictures.txt',
    '../e_shiny_selfies.txt',
]

for landscape_path in landscape_paths:
    print ('Landscape file: %s' % landscape_path)
    f = open(landscape_path, mode='r')
    
    header = f.readline()
    row_count = int(header)
    
    grid = []
    for i in range(row_count):
        grid.append(list(f.readline().rstrip()))
    grid = np.array(grid)
    f.close()
    
    results = models.unidimensional_greedy_heuristic(row_count, grid)
    
    f = open(out_folder + landscape_path.split('/')[-1], mode='w')
    f.write(str(len(results)) + '\n')
    f.writelines(map(lambda x: ' '.join(map(str, x)) + '\n', results))
    f.close()
    print ('\n')
