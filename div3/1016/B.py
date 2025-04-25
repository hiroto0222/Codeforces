# the minimum would be 1 as xyz >= x + y + z
# basically want as many leading zeros as possible
# 
# so to achieve minimum, we need only one digit to remain,
# and to remove all trailing non zero digits
# 
# greedy approach
# - keep the right most digit
# - keep all zeros to its left
# - remove all other digits

for _ in range(int(input())):
    s = input()
    n = len(s)
    zeros = 0

    if (n == 1):
        print(0)
        continue

    met_positive = False
    for i in range(n - 1, -1, -1):
        if (s[i] != '0'):
            met_positive = True
        elif (met_positive):
            zeros += 1
    
    print(n - (zeros + 1))
