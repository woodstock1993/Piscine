def maxLength(a, k):
    a = sorted(a)
    sums = 0
    index = 0
    arr = []
    for i in range(len(a)):
        sums += a[i]
        index = i
        arr.append(a[i])
        if sums > k:
            break
    while sums > k:
        print(sums, sum(arr), len(arr))
        num = arr.pop()
        sums -= num
        index -= 1
    print(sum(arr), arr)
    return len(arr)

a = [978, 409, 229, 934, 299, 982, 636, 14, 866, 815, 64, 537, 426, 670, 116, 95, 630, 502, 518, 196, 106, 405, 452, 299, 189, 124, 506, 883, 753, 567, 717, 338, 439, 145, 502, 898, 872, 829, 138, 359, 178, 398, 295, 905, 610, 232, 746, 176, 636, 299, 143, 400, 969, 413, 261, 558, 595, 9, 396, 969, 114, 531, 7, 963, 943, 366, 83, 853, 768, 822, 696, 713, 672, 902, 591, 832, 739, 58, 617, 791, 641, 680, 336, 7, 973, 99, 96, 320, 455, 224, 290, 761, 906, 127, 124, 507, 814, 771, 239, 95, 221, 845, 367, 535, 227, 395, 364, 739, 845, 591, 551, 160, 624, 948, 386]
k = 30603

print(maxLength(a, k))