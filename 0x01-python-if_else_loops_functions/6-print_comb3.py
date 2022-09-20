#!/usr/bin/python3

for num in range(10):
    for i in range(10):
        if (i != num and i > num) and (num != 8 or i != 9):
            print(f"{num:d}{i:d}" + ", ", end ='')
        elif num == 8 and i ==9:
            print(f"{num:d}{i:d}")

