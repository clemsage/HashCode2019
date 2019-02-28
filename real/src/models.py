# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:59:50 2019

@author: Sage
"""
import numpy as np

def greedy_heuristic(slides, seed=None):
    import pdb; pdb.set_trace()
    np.random.seed(seed)
    np.random.shuffle(slides)
    results = []
    max_slides_search = 100
    for ind_s, slide in enumerate(slides):
        subset_slides = np.random.choice(slides[ind_s:], max_slides_search, 
                                         replace=False)
        max_score = 0
        
        
    return results

def max_scores_two_slides(slide1, slide2):
    return min([len(set(slide1+slide2)),
                len([tag for tag in slide1 if tag not in slide2]),
                len([tag for tag in slide2 if tag not in slide1])])

def keep_original_order(slides):
    return [slide.photos for slide in slides]
