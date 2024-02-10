"""
Bayes Rules Library

@author Soren
@version v1.0
"""

from scipy.integrate import quad
import numpy as np

class bayes:
    def __init__(self,number:int,fake:int,shoot:int):
        """
        Args:
            number (int): Total bullet count.
            fake (int): Number of blanks.
            shoot (int): Number of hits.
        """
        
        self.B = number
        self.E = fake
        self.S = shoot
    