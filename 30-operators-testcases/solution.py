# -*- coding: utf-8 -*-
"""Solution.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i8fPFwc5_whqBSBP45FSc38Yowjq8xXZ
"""

cost = float(input())
tip = cost * int(input()) / 100
tax = cost * int(input()) / 100
tcost=cost+tip+tax
print(round(tcost))

