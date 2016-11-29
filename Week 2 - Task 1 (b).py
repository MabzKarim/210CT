import math

def HIGHEST_PERFECT_SQUARE(r):
""" This function would find the highest perfect square for any given number"""
    temp = int(math.sqrt(r))
    # the sqrt of the given number is rounded down(truncated)
    hps = temp**2
    # the rounded down number is squared to find the highest perfect square
    return hps
