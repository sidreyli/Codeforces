#find distance to edge, sort and find biggest diff / 2, return max
def vanya_lanterns():
    nl = list(map(int, input().split()))
    n, l = nl[0], nl[1]
    lanterns = list(map(int, input().split()))
    lanterns.sort()
    dist1 = lanterns[0] - 0
    dist2 = l - lanterns[-1]
    biggest_gap = 0
    for i in range(len(lanterns)-1):
        gap = lanterns[i+1] - lanterns[i]
        if gap > biggest_gap:
            biggest_gap = gap
    sol = max(dist1, dist2, biggest_gap/2)
    print(f"{sol:.10f}")
vanya_lanterns() 