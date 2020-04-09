# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 20:23:28 2020

@author: turjo
"""

def double (x):
    """
    

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    return x*2

def apply_to_one(f):
    """
    

    Parameters
    ----------
    f : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    return f(1)

def my_function(fname):
   
    """
    

    Parameters
    ----------
    "name" : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    print ("your name is", fname)
    
#exe python statement
#   print ("enter your name ")
#   input_name =input()
#   my_function(input_name)
    
#specify the arguments by name 
def full_name (first = "Just some bs", last = "lname"):
    return first +" "+ last

##
    