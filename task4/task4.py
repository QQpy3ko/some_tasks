#!/usr/bin/env python3.7

import sys

def hoursmin_to_min(time_span):
    a, b = time_span.split()[0], time_span.split()[1]
    a1, a2 = a.split(':')[0], a.split(':')[1]
    b1, b2 = b.split(':')[0], b.split(':')[1]
    arrival_min = int(a1)*60 + int(a2)
    departure_min = int(b1)*60 + int(b2)

    return [arrival_min, departure_min]

def min_to_hoursmin(mins):
    h = str(mins // 60)
    m = mins % 60
    if m < 10:
        m = '0' + str(m)
    else:
        m = str(m)
    return(f"{h}:{m}")

def main():

    arr_dep_timeline = []
    with open(sys.argv[1], "r") as input_file:
        for line in input_file:
            arr_dep_timeline.append(hoursmin_to_min(line))
    arr_dep_timeline.sort()
    max_dep_value = 0
    for x in arr_dep_timeline:
        for y in x:
            if y > max_dep_value:
                max_dep_value = y

    minutes_dict = {x: 0 for x in range(arr_dep_timeline[0][0], max_dep_value + 1)}
    
    for arriv, dep in arr_dep_timeline:

        counter = arriv
        while counter <= dep:
            # print(counter)
            # print(dep)
            minutes_dict[counter] += 1
            counter += 1

    max_customers_number = max(minutes_dict.values())
    list_max_keys = []

    for key, value in minutes_dict.items():
        
        if value == max_customers_number:
            list_max_keys.append(key)
      
    i = 0
    while i < len(list_max_keys):
        start = list_max_keys[i]
        end = list_max_keys[i]
        
        j = 1
        while i + j < len(list_max_keys):
            if list_max_keys[i + j] - start == j:
                end = list_max_keys[i + j]
                j += 1
            else:
                j -= 1 
                break
        
        if start == end:
            print(min_to_hoursmin(start))
        else:
            print(f"{min_to_hoursmin(start)} {min_to_hoursmin(end)}")
        
        i += 1 + j


if __name__ == "__main__":
    main()