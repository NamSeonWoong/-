import random


def processing(original):    
    for item in original:
        if (random.uniform(0,1) > 0.5):
            item['isTrader'] = True
        else:
            item['isTrader'] = False
    return original