# 10818

'''
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
'''

n = int(input())
num_list = input().split(" ")
for i in range(n):
    num_list[i] = int(num_list[i])

print(min(num_list), max(num_list))
