N, r, c = list(map(int, input().split()))
def zfunction(N, r, c):
    if N == 0:
        return 0
    return 2*(r%2)+(c%2) + 4*zfunction(N-1,int(r/2),int(c/2))

print(zfunction(N, r, c))
