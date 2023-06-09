def BMHSearch(pattern, text):
    m = len(pattern)
    n = len(text)
    numberPatterns=0
    if m > n: return -1
    skip = []
    for k in range(256): skip.append(m)
    for k in range(m - 1): skip[ord(pattern[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1; i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1; i -= 1
        if j == -1: numberPatterns+=1
        k += skip[ord(text[k])]
    #print(numberPatterns)
    return -1