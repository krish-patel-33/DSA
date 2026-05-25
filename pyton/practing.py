
def my_atoi(s):
    s = s.strip()
    if not s:
        return 0

    sign = 1
    i = 0

    if s[0] == '-':
        sign = -1
        i = 1
    elif s[0] == '+':
        i = 1

    result = 0
    while i < len(s) and s[i].isdigit():
        result = result * 10 + (ord(s[i]) - ord('0'))
        i += 1

    return sign * result

print(my_atoi("   -42"))
print(my_atoi("4193 with words"))
print(my_atoi("+123"))

