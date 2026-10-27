#x+13*x/x+x/12*x-x-11+x*x/x-10=66
for a in range(0,9):
    for b in range(0,9):
        for c in range(1,9):
            for d in range(0,9):
                for e in range(0,9):
                    for f in range(0,9):
                        for g in range(0,9):
                            for h in range(0,9):
                                for i in range(1,9):
                                    if a + 13 * b / c + d / 12 * e - f - 11 + g * h / i - 10 == 66:
                                        print(a, b, c, d, e, f, g, h, i)
                                    