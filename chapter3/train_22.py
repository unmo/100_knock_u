# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa

@
"""

import sys
import argparse

def main(in_file):
    with open(in_file,"r") as read_file:
        for line in read_file:
            if line.find("Category") != -1:
                category_list = line.rstrip("|*]]\n").split(":")
                print category_list[1]
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest='input', default='train_20.txt', help='input data')
    args = parser.parse_args()
    main(args.input)
    