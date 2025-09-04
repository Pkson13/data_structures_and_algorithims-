def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    output = []
    win = nums[:k]
    print(win)
    # output.append(max(win))
    for i in range(k, len(nums) + 1):
        win = nums[i - k : i]
        print(win)
        current_max = max(win)
        output.append(current_max)

    return output


print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], k=3))
