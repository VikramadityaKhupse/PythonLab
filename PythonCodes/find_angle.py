# https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import atan2, degrees
AB, BC = int(input()), int(input())
theta = degrees(atan2(AB, BC))
print(f"{int(round(theta))}\u00B0")
