# determine whether k is an ideal generator
# when k = 2m is even, [a1, a2, ..., am-1, am, am, am-1, am-2, ..., a1]
# so sum is 2*(a1 + ... + am), hence when k is even, the sum is also even, can never generate odd n
# 
# when k = 2m + 1 is odd, [a1, ..., am, am+1, am, ..., a1]
# so sum is am+1 + 2*(a1 + ... + am)
# so for any n, there exists a palindrome array of form [1, ..., 1, n - (k - 1), 1, ..., 1]
# therefore there exists a palindrome array iff k is odd

for _ in range(int(input())):
    k = int(input())
    print("Yes" if k % 2 != 0 else "No")
