#!/usr/bin/python3
for i in range(0, 100):
    if i != 99:
        if len(str(i)) == 1:
            print("{}{}".format("0", i), end=", ")
        else:
            print("{}".format(i), end=", ")
    else:
        print(i, end="")
