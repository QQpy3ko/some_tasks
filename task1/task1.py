#!/usr/bin/env python3.7

import sys
import numpy

def output_2_dig(number):
    print('{:.2f}'.format(number))


if __name__ == "__main__":

    with open(sys.argv[1], "r") as input_file:
        file_content = input_file.read()
        lines  = file_content.splitlines()
        int_lines = [int(i) for i in lines]

        percentile = numpy.percentile(int_lines, 90)
        output_2_dig(percentile)
        
        median = numpy.percentile(int_lines, 50)
        output_2_dig(median)

        output_2_dig(max(int_lines))

        output_2_dig(min(int_lines))

        output_2_dig(sum(int_lines) / len(int_lines))