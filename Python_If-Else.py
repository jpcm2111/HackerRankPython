#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':

    num = int(input())

    if num % 2 == 1:
        print("Weird")
    elif (num >= 2 and num <= 5):
        print("Not Weird")
    elif (num >= 6 and num <= 20):
        print("Weird")
    elif num > 20:
        print("Not Weird")
