n, m, k = map(int, input().split())
int_bus = (n + m) // k

if m // 2 != 0:
    max_bus = m // 2
    if (n + m) / max_bus <= k and (n + m) % k == 0:
        print(int_bus)
    elif (n + m) / max_bus <= k:
        print(int_bus + 1)
    else:
        print('0')
else:
    print('0')
