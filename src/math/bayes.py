"""
Bayes Rules Library

@author Soren
@version v1.0
"""

from scipy.integrate import quad
import numpy as np

def bayes(B, E, S):
    """
    Calculate the probability of getting shot in the next round
        :param B: total number of bullets
        :param E: number of empty shots
        :param S: number of times hit
        :return: probability of getting shot in the next round
    """
    def binomial_dist(B, p, S):
        """
        Calculate the binomial distribution probability
            :param B: total number of trials
            :param p: probability of success in each trial
            :param S: number of successes
            :return: binomial distribution probability
        """
        return np.math.comb(B, S) * p**S * (1-p)**(B-S)

    def posterior_distribution(p, B, E, S):
        """
        Posterior distribution of the probability of getting shot
            :param p: probability of getting shot
            :param B: total number of bullets
            :param E: number of empty shots
            :param S: number of times hit
            :return: posterior distribution of the probability of getting shot
        """
        prior = 1  # Prior probability of getting shot, set to a uniform distribution here
        likelihood = binomial_dist(B, p, S)
        normalizing_constant, _ = quad(lambda x: binomial_dist(B+E, x, B) * binomial_dist(B, x, S), 0, 1)
        return (prior * likelihood) / normalizing_constant

    normalizing_constant, _ = quad(lambda x: binomial_dist(B+E, x, B) * binomial_dist(B, x, S) * posterior_distribution(x, B, E, S), 0, 1)
    return binomial_dist(B+E, 1/(1+S/(B-E)), B) * posterior_distribution(1/(1+S/(B-E)), B, E, S) / normalizing_constant