def lengthOfLongestSubstring(s: str):
    """
    :type s: str
    :rtype: int
    """
    seen = {}
    count = 0
    largest = 0
    for i in s:
        if i not in seen:
            count += 1
            # print(i, count)
            seen[i] = True
        else:
            seen = {}
            if count > largest:
                largest = count
            count = 1
    print(largest)


lengthOfLongestSubstring("abcabcbb")
