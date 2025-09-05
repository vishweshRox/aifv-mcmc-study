#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 07:47:27 2025

@author: vishweshpalani
"""

# RE-READ ALGORITHM AND PLAN IMPLEMENTATION

class Node:
    def __init__(self, child1=None, child2=None):
        
        # accepts an object or 
        

class Huffman:
    def __init__(self, x_arr, p_arr):
        if len(x_arr) != len(p_arr):
            raise ValueError("x_arr and p_arr should have the same number of elements.")
        self.N = len(x_arr)
        enc_arr = ["" for i in range(self.N)]
        self.X = list(zip(x_arr, p_arr, enc_arr))
        
    def sort(self, arr):
        # need to return a copy, since we are replacing two with 1 each time
        return sorted(arr, key=lambda t : t[1])
    
    def ___huffman(self, arr):
        # MUST RECURSIVELY CONSTRUCT THE ENCODING USING NODE's
        if len(arr) == 2:
            for i in range(2):
                arr[i][2] = str(i) + arr[i][2]
            
            
        
    
    def encode(self):
        
        for _ in range(N-1):
            
        
        
        cpy = list(self.X)
        if len(cpy) == 2:
            
        # takes last two, merges and replaces, re-sorts
        
        #check base case each time
        #sort, pick 2, merge, replace
        
    def avg_len(self):
        # check if encoding is complete and avg_len has been computed, else
        return self.avg_len
        
        
        