def trap_rain_water(h):
    if not h or len(h) < 3:
        return 0    
    n = len(h)
    lm = [0] * n
    rm = [0] * n
    w = 0
    lm[0] = h[0]
    for i in range(1, n):
        lm[i] = max(lm[i - 1], h[i])

    rm[n - 1] = h[n - 1]
    for i in range(n - 2, -1, -1):
        rm[i] = max(rm[i + 1], h[i])

    for i in range(1, n - 1):
        w += max(0, min(lm[i], rm[i]) - h[i])

    return w

tc = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
r = trap_rain_water(tc)
print(r)

