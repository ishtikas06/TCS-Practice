s = "cadbzabcd"
n = len(s)
char_map = {}
l = r = 0
max_len = 0

while r < len(s):
    if s[r] in char_map:
        if char_map[s[r]] >= l:
            l = char_map[s[r]] + 1
    curr_len = r-l+1
    max_len = max(max_len, curr_len) 

    char_map[s[r]] = r
    r += 1

print(max_len)