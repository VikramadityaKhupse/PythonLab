# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
ordered_dict = OrderedDict()
N = int(input())

for _ in range(N):
    data = input().split(' ')
    item_name, net_price = ' '.join(data[:len(data)-1]), int(data[-1])
    if item_name in ordered_dict.keys():
        ordered_dict[item_name] += net_price
    else:
        ordered_dict[item_name] = net_price

for name, price in ordered_dict.items():
    print(name, price)