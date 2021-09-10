import statistics
from collections import Counter
# bài tập 2
def thongke(lis):
    mean = statistics.mean(lis)
    lis.sort()
    if len(lis) % 2 == 0:
        median = (lis[int(len(lis) / 2)] + lis[int(len(lis) / 2 - 1)]) / 2
    else:
        median = lis[int(len(lis) - 1 / 2)]
    mode = []
    d = Counter(lis)
    for i in d:
        if d[i] == max(d.values()):
            mode.append(i)
    return mean,median,mode

A = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
B=[4,4,5,4,5,5]
print("======================================================")
print(thongke(A))
print(thongke(B))