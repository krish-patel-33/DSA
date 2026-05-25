
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




def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Delete
                    dp[i][j - 1],      # Insert
                    dp[i - 1][j - 1]   # Replace
                )

    return dp[m][n]

print(f"Edit Distance: {edit_distance('horse', 'ros')}")
print(f"Edit Distance: {edit_distance('intention', 'execution')}")




def longest_unique_substring(s):
    char_index = {}
    max_len = 0
    start = 0

    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1

        char_index[s[end]] = end
        max_len = max(max_len, end - start + 1)

    return max_len

print(f"Length: {longest_unique_substring('abcabcbb')}")
print(f"Length: {longest_unique_substring('bbbbb')}")
print(f"Length: {longest_unique_substring('pwwkew')}")