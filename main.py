#!/usr/bin/env python

# This is a sample Python script.
import pandas as pd


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    iii={}
    iii[0] = [1,2]
    iii[1] = [3,9]
    iii[2] = [1,5]
    iii[3] = [1,6]

    Distance = [0] * 5
    NDSet_obj = {}

    for i in range(3):
        NDSet_obj[i] = iii[i]

    ND = sorted(NDSet_obj.items(), key=lambda x: (x[1][0], x[1][1]))
    ND


    LL=[2,4,1,6,7]
    distance = dict(enumerate(LL))
    # distance distance = dict(enumerate(Distance))
    New_distance = sorted(distance.items(), key=lambda x: x[1], reverse=True)


    print(iii.keys())
    print()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # f=open(r"C:/Users/29639/Desktop/2.csv",ncoding='gbk')
    name = "C:/Users/29639/Desktop/dis.csv"
    dis = pd.read_csv(name, header=None).values

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
