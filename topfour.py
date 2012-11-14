#coding:utf-8
'''
Given an unordered list of N elements, write a function to find the top four elements of the given list. Make sure your function runs in linear time O(N).

Input format :

First line of input contains N , number of elements in list.
Next N line , each contains a element.

Output format :

Print the top four elements of list.

Sample input :

8
6930886
-1692777
4636915
7747793
-4238335
9885386
9760492
6516649

Sample ouput :

9885386
9760492
7747793
6930886

Constraint :

N < 1000000.
all numbers will fit  in 32-bit integer.
'''

__author__ = 'nooper'

def sortlist(items):
    if len(items) == 0:
        pass
    else:
        items.sort(key=lambda x: -x)
        return [j for i, j in enumerate(items) if i < 4]


def main():
    n = int(raw_input())
    iterms = []
    for i in xrange(n):
        iterms.append(int(raw_input().strip()))
    a = sortlist(iterms)
    for i in a:
        print i


if __name__ == '__main__':
    main()