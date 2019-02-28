# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:59:50 2019

@author: Sage
"""
import numpy as np


def unidimensional_greedy_heuristic(row_count, column_count, min_ingredient, 
                                    max_area, grid):

    row_slices, row_score = row_greedy_heuristic(row_count, column_count, 
                                                 min_ingredient, 
                                                 max_area, grid)
    print ('Score of the 1D greedy heuristic along rows: %d' % row_score)

    col_slices, col_score = row_greedy_heuristic(column_count, row_count, 
                                                 min_ingredient,
                                                 max_area, np.transpose(grid))
    col_slices = col_slices[:, [1, 0, 3, 2]]
    print ('Score of the 1D greedy heuristic along columns: %d' % col_score)

    if row_score > col_score:
        results = row_slices
    else:
        results = col_slices

    return results

def row_greedy_heuristic(row_count, column_count, min_ingredient,
                         max_area, grid):
    results = []
    score = 0
    for r in range(row_count):
        beg = 0
        end = 0
        mushroom_count = 0
        tomato_count = 0

        while end < column_count:
            if grid[r][end] == 'M':
                mushroom_count += 1
            elif grid[r][end] == 'T':
                tomato_count += 1
            end += 1
    
            if end - beg > max_area:
                if grid[r][beg] == 'M':
                    mushroom_count -= 1
                elif grid[r][beg] == 'T':
                    tomato_count -= 1
    
            if (end - beg <= max_area 
                    and mushroom_count >= min_ingredient
                    and tomato_count >= min_ingredient):
                results.append(np.array((r, beg, r, end - 1)))
                score += end - beg
                beg = end
                mushroom_count = 0
                tomato_count = 0

    return np.array(results), score
