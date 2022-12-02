import time
import inspect
import datetime
from ..Tasks.src.linearRegression import *
from ..Tasks.src.updateResults import *


def mainFuntion():

    minutes = 0

    while 1==1:
        if minutes == 0:
            res = CalcLinearRegressions()
        if ((minutes % 2) == 0 and minutes != 0):
            res = UpdateResult()
        time.sleep(60)
        minutes=minutes+1
        if(minutes>=60):
            minutes=0
    return 0