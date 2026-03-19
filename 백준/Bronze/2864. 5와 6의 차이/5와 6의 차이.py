import sys

A, B = sys.stdin.readline().split()

min_A = A.replace('6', '5')
min_B = B.replace('6', '5')
min_sum = int(min_A) + int(min_B)

max_A = A.replace('5', '6')
max_B = B.replace('5', '6')
max_sum = int(max_A) + int(max_B)

print(min_sum, max_sum)