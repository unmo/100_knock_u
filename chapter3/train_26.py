# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa

@
"""
import argparse
import re

def main(input_file,output_file):
    
    my_dict = {}
    info = re.compile("\|(.*) = (.*)")
    with open(input_file,"r") as in_file :
        for line in in_file:
            i = info.search(line)
            if i is not None:
                
                my_dict =  line.strip("|").rstrip().split("=")
                print type(my_dict[1])
                my_dict[1] = my_dict.replace("''","").replace("'''","").replacce("''''","")
                
                with open(output_file,"w") as out_file :
                    out_file.write(my_dict)
        
                
if __name__ == "__main__" :
    
    parser = argparse.ArgumentParser();
    parser.add_argument("-i", "--input", dest = "input_file", default = "train_20.txt", help = "help test")
    parser.add_argument("-o", "--output", dest = "output_file", default = "output_26.txt", help = "help_test")
    args = parser.parse_args()
    main(args.input_file,args.output_file)
    