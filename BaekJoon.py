# 10926
id_name = input()
print(f"{id_name}??!")

# 18108
buda_year = input()
term = 543
print(int(buda_year) - term)

# 10430
A, B, C = input().split(" ")
A, B, C = int(A), int(B), int(C)
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)

# 2588
A = input()
B = input()

result_1 = int(B[2]) * int(A)
result_2 = int(B[1]) * int(A)
result_3 = int(B[0]) * int(A)
result_4 = result_1 + 10 * result_2 + 100 * result_3

print(result_1)
print(result_2)
print(result_3)
print(result_4)