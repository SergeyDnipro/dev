for x1 in range(100):
    for x2 in range(100):
        for x3 in range(100):
            for x4 in range(100):
                if x1 + x2 == 8 and x1 * x3 == 21 and x3 * x4 == 9 and x2 - x4 == 5:
                    print(x1, x2, x3, x4)