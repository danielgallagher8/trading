"""
Indicators for technical analysis
"""

#Import libraries
import math

#Definitions/classes
def obv(obv_prev, close, close_prev, volume):
    """
    ON-BALANCE-VOLUME:
    On-balance volume (OBV) is a technical trading 
    momentum indicator that uses volume flow to 
    predict changes in stock price. 
    """
    if close > close_prev:
        return obv_prev + volume
    elif close == close_prev:
        return obv_prev
    elif close < close_prev:
        return obv_prev - volume

def ad(close, high, low, volume, prev_ad):
    """
    ACCUMULATION/DISTRIBUTION:
    The accumulation/distribution indicator (A/D) is 
    a cumulative indicator that uses volume and price 
    to assess whether a stock is being accumulated or 
    distributed.
    """
    #mfm = Money Flow Multiplier
    mfm = ( (close - low) - (high - close) )/ (high - low)
    #mfv = Money Flow Volume
    mfv = mfm * volume
    a_d = prev_ad + mfv
    return a_d

def atr():
    """
    AVERAGE TRUE RANGE: 
    """

def adx(prev_adx, atr):
    """
    AVERAGE DIRECTIONAL INDEX:
    The average directional index (ADX) is a technical
    analysis indicator used by some traders to 
    determine the strength of a trend.
    """
    smooth_pos_dm
    smooth_neg_dm
    pos_di = (smooth_pos_dm / atr) * 100
    neg_di = (smooth_neg_dm / atr) * 100
    mod_pos = math.sqrt((pos_di ** 2) + (neg_di ** 2))
    mod_neg = math.sqrt((pos_di ** 2) - (neg_di ** 2))
    dx = (mod_pos / mod_neg) * 100
    adx = ((prev_adx * 13) + dx) / 14
    return adx
    
    
