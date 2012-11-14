#coding:utf-8
__author__ = 'nooper'

def GetResult(items):
    count = items.count(0)
    if count > 1:
        return [0 for i in xrange(len(items))]
    elif count == 1:
        if len(items) == 2:
            items.reverse()
            return items
        else:
            index = items.index(0)
            if index == 0:

            elif index == (len(items) - 1):
                pass
            else:
                result1 = reduce(lambda x, y: x * y, items[:index])
                result2 = reduce(lambda x, y: x * y, items[index + 1:])

                return ([0 for i in xrange(index)] + [result1 / x for x in items[:index]] + [result2 / x  for x in
                                                                                             items[index + 1:]] + [0 for
                                                                                                                   i in
                                                                                                                   xrange(
                                                                                                                       index + 1,
                                                                                                                       len(
                                                                                                                           items))])
    else:
        result = reduce(lambda x, y: x * y, items)
        req = []
        for x in items:
            req.append(result / x)
        return req


def main():
    n = int(raw_input())
    items = []
    if n >= 2:
        for i in xrange(n):
            items.append(int(raw_input().strip()))
        result = GetResult(items)
        for i in result:
            print i

    else:
        pass

if __name__ == '__main__':
    main()
