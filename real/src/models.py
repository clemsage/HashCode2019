# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:59:50 2019

@author: Sage
"""
import numpy as np

def greedy_heuristic(slides, seed=None):
    np.random.seed(seed)
    np.random.shuffle(slides)
    results = []
    max_slides_search = 100
    
    nb_slides = len(slides)
    for _ in range(nb_slides):
        idx_curr_slide = np.random.choice(len(slides))
        subset_slides = np.random.choice(slides, min(len(slides), max_slides_search), 
                                         replace=False)
        import pdb; pdb.set_trace()
        
        
        
    return results

def score_two_slides(slide1, slide2):
    intersect = set.intersection(slide1.tags, slide2.tags)
    return min([len(intersect),
                len(slide1.tags - intersect),
                len(slide2.tags - intersect)])

def keep_original_order(slides):
    return [slide.photo_ids for slide in slides]
