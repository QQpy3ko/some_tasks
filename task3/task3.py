#!/usr/bin/env python3.7

import sys
import os


def main():

    summary = {x: 0 for x in range(1, 17)}

    for file in os.listdir(sys.argv[1]):
        with open(sys.argv[1] + '/' + file, "r") as input_file:
            file_content = input_file.read()
            lines  = file_content.splitlines()
            counter = 1
            for i in lines:
                summary[counter] += float(i)
                counter += 1

    max_value = 0
    
    for key, value in summary.items():
        if value > max_value:
            max_value = value
            result = key

    print(result)        


if __name__ == "__main__":
    main()