# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 19:39:48 2018

@author: Lua
"""

class HashIndex:
    """
    Extremly sofisticated python dict index
    Now supports duplicate items (!!!)
    Also assumes full access to original data list (for somewhat adequate reconstruction)
    """
    
    
    def __init__(self):
        self.item_list = []
        self.index = {}
        
    def insert(self, item, p):
        """
        Add a new item to index. 
        """
        self.item_list.append(item)
        if item in self.index.keys():
            self.index[item].append(p)
        else:  
            self.index[item] = [p] 
            
  
        
    def remove(self, item, x=None):
        """
        Remove specific item from index and reconstructs it
        
        """
        def shift_values(remove_candidates,values):
            """
            Shifts all values of values if value greater than remove candidates
            """
            new_values = []
            for value in values:
                candidate_value = value
                for remove in remove_candidates:
                    if candidate_value>remove:
                        candidate_value = candidate_value-1
                new_values.append(candidate_value)
            return new_values
            
            
            
            
        remove_candidates = self.index.get(item)
        self.index = {key:shift_values(remove_candidates,listx)
                    for key,listx in self.index.items() 
                    if key!=item }

    def search(self, item):
        """
        Search for specific item location(s)
        """
        candidates = self.index.get(item)
        if candidates:
            return candidates
        else:
            print("Woops")
            return None

class HashIndex_no_duplicates:
    """
    Basic hash index implementation
    Doesn't support duplicate item storage
    Fully reconstructs itself on removal
    """
    def __init__(self):
        self.index = {}
        
    def insert(self, item, p):
        """
        Add a new item to index. 
        """
        self.index[item] = p
              
        
    def remove(self, item):
        """
        Remove specific item from index and reconstructs it
        
        """  
        remove_candidate = self.index.get(item)            
        self.index = {key:(value-1 if value>remove_candidate else value) for key,value in self.index.items() if value != remove_candidate }

        

    def search(self, item):
        """
        Search for specific item location
        """
        candidate = self.index.get(item)
        if candidate:
            return candidate
        else:
            return None