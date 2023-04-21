import pandas as pd
import numpy as np


chat_id = 630197911 # Ваш chat ID, не меняйте название переменной

def solution(x, y):
    result = ttest_ind(x, y, equal_var=False, alternative='two-sided')
    return result.pvalue < 0.03
