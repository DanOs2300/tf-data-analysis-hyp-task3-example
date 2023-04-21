import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest

chat_id = 630197911 # Ваш chat ID, не меняйте название переменной

def solution(x):
    result = ztest(x1=x, value=500, alternative='larger')
    return result[1] < 0.06
