# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 19:39:48 2018

@author: Lua
"""

class HashIndex:
    """
    Extremly sofisticated python dict index
    Now supports duplicate items (!!!)
    """
    
    
    def __init__(self):
        self.index = {}
        
    def insert(self, item, p):
        """
        Add a new item to index. 
        """
        if item in self.index.keys():
            self.index[item].append(p)
        else:  
            self.index[item] = [p] 
            
  
        
    def remove(self, item, x=None):
        """
        Remove specific item from index and reconstructs it
        
        """
        remove_candidate = self.index.get(item)
        self.index = {key:(value-1 if value>remove_candidate else value) for key,listx in self.index.items() for value in listx if value not in remove_candidate }
        

    def search(self, item):
        """
        Search for specific item location
        """
        candidates = self.index.get(item)
        if candidate:
            return candidate
        else:
            print("Woops")
            return None

class HashIndex_no_duplicates:

    
    def __init__(self):
        self.index = {}
        
    def insert(self, item, p):
        """
        Add a new item to index. 
        """
        self.index[item] = p
              
        
    def remove(self, item, x=None):
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
            print("Woops")
            return None