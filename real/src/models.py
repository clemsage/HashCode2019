# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:59:50 2019

@author: Sage
"""
import numpy as np
from copy import copy

def greedy_heuristic(slides, seed=None):
    np.random.seed(seed)
    np.random.shuffle(slides)
    results = []
    max_slides_search = 10

    idx_curr_slide = np.random.choice(len(slides))
    while True:
        curr_slide = copy(slides[idx_curr_slide])
        results.append(curr_slide.photo_ids)
        del slides[idx_curr_slide]
        
        if not len(slides):
            break

        idx_subset_slides = np.random.choice(len(slides), min(len(slides), max_slides_search), 
                                             replace=False)
        max_score = -1
        best_idx = None
        for idx_candidate in idx_subset_slides:
            score = score_two_slides(curr_slide, slides[idx_candidate])
            if  score > max_score:
                best_idx = idx_candidate
                max_score = score
        idx_curr_slide = best_idx

    return results

def score_two_slides(slide1, slide2):
    intersect = set.intersection(slide1.tags, slide2.tags)
    return min([len(intersect),
                len(slide1.tags - intersect),
                len(slide2.tags - intersect)])

def keep_original_order(slides):
    return [slide.photo_ids for slide in slides]
