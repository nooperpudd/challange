#coding:utf-8
"""
Frequency Counting of Words / Top N words in a document.

Given N terms, your task is to find the k most frequent terms from given N terms.

Input format :

First line of input contains N, denoting the number of terms to add.
In each of the next N lines, each contains a term.
Next line contains k, most frequent terms.

Output format :

Print the k most frequent terms in descending order of their frequency. If two terms have same frequency print them in lexicographical order.

Sample input :

14
Fee
Fi
Fo
Fum
Fee
Fo
Fee
Fee
Fo
Fi
Fi
Fo
Fum
Fee
3

Sample output :

Fee
Fo
Fi

Constraint :
0 < N < 300000
0 < term length < 25.
"""

__author__ = 'nooper'

def get_top_frequency(terms, k):
    termsset = set(terms)
    termsdict = {}.fromkeys(termsset, 0)
    for term in terms:
        if termsdict.has_key(term):
            termsdict[term] += 1
        else:
            termsdict[term] = 1
    countdict = termsdict.items()
    countdict.sort(key=lambda x: x[0])
    countdict.sort(key=lambda x: -x[1])
    return [t for t, c in countdict[:k]]


def main():
    num_n = int(raw_input())
    terms = []
    for i in xrange(num_n):
        terms.append(raw_input().strip())

    #print "please input a num as k:"
    num_k = int(raw_input())
    frequency = get_top_frequency(terms, num_k)
    for t in frequency:
        print t


if __name__ == '__main__':
    main()