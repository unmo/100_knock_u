# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa

@
"""

import argparse

def main(input_file):
    print "test"
    with open(input_file,"r") as in_file:
        for line in in_file:
            if "====" in line:
                print "".join(line.rstrip() + "\t" +"3")
            elif "===" in line:
                print "".join(line.rstrip() + "\t" + "2")
            elif "==" in line:
                print "".join(line.rstrip() + "\t" + "1")  
            else:
                pass
    
if __name__ == "__main__" :
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-i' , '--input', dest = 'input_file', default = './train_20.txt', help='input data')
    args = parser.parse_args()
    main(args.input_file)
    