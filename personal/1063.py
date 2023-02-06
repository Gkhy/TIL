K, R, N = input().split()
N = int(N)
AL = ["A", "B", "C", "D", "E", "F", "G", "H"]
NL = ["1", "2", "3", "4", "5", "6", "7", "8"]
for i in range(N):
    d = input()
    if d[0] == "B":
        a = AL.index(K[0])
        b = NL.index(K[1])
        c = AL.index(R[0])
        d = NL.index(R[1])
        if 0 <= a < 8 and 0 <= b - 1 < 8:
            if R == AL[a] + NL[b - 1] and 0 <= c < 8 and 0 <= d - 1 < 8:
                R = AL[c] + NL[d - 1]
                K = AL[a] + NL[b - 1]
            elif R != AL[a] + NL[b - 1]:
                K = AL[a] + NL[b - 1]

    elif d[0] == "T":
        a = AL.index(K[0])
        b = NL.index(K[1])
        c = AL.index(R[0])
        d = NL.index(R[1])
        if 0 <= a < 8 and 0 <= b + 1 < 8:
            if R == AL[a] + NL[b + 1] and 0 <= c < 8 and 0 <= d + 1 < 8:
                R = AL[c] + NL[d + 1]
                K = AL[a] + NL[b + 1]
            elif R != AL[a] + NL[b + 1]:
                K = AL[a] + NL[b + 1]
    elif d[0] == "R":
        if len(d) == 2:
            if d[1] == "T":
                a = AL.index(K[0])
                b = NL.index(K[1])
                c = AL.index(R[0])
                d = NL.index(R[1])
                if 0 <= a + 1 < 8 and 0 <= b + 1 < 8:
                    if R == AL[a + 1] + NL[b + 1] and 0 <= c + 1 < 8 and 0 <= d + 1 < 8:
                        R = AL[c + 1] + NL[d + 1]
                        K = AL[a + 1] + NL[b + 1]
                    elif R != AL[a + 1] + NL[b + 1]:
                        K = AL[a + 1] + NL[b + 1]
            elif d[1] == "B":
                a = AL.index(K[0])
                b = NL.index(K[1])
                c = AL.index(R[0])
                d = NL.index(R[1])
                if 0 <= a + 1 < 8 and 0 <= b - 1 < 8:
                    if R == AL[a + 1] + NL[b - 1] and 0 <= c + 1 < 8 and 0 <= d - 1 < 8:
                        R = AL[c + 1] + NL[d - 1]
                        K = AL[a + 1] + NL[b - 1]
                    elif R != AL[a + 1] + NL[b - 1]:
                        K = AL[a + 1] + NL[b - 1]
        else:
            a = AL.index(K[0])
            b = NL.index(K[1])
            c = AL.index(R[0])
            d = NL.index(R[1])
            if 0 <= a + 1 < 8 and 0 <= b < 8:
                if R == AL[a + 1] + NL[b] and 0 <= c + 1 < 8 and 0 <= d < 8:
                    R = AL[c + 1] + NL[d]
                    K = AL[a + 1] + NL[b]
                elif R != AL[a + 1] + NL[b]:
                    K = AL[a + 1] + NL[b]
    elif d[0] == "L":
        if len(d) == 2:
            if d[1] == "T":
                a = AL.index(K[0])
                b = NL.index(K[1])
                c = AL.index(R[0])
                d = NL.index(R[1])
                if 0 <= a - 1 < 8 and 0 <= b + 1 < 8:
                    if R == AL[a - 1] + NL[b + 1] and 0 <= c - 1 < 8 and 0 <= d + 1 < 8:
                        R = AL[c - 1] + NL[d + 1]
                        K = AL[a - 1] + NL[b + 1]
                    elif R != AL[a - 1] + NL[b + 1]:
                        K = AL[a - 1] + NL[b + 1]
            elif d[1] == "B":
                a = AL.index(K[0])
                b = NL.index(K[1])
                c = AL.index(R[0])
                d = NL.index(R[1])
                if 0 <= a - 1 < 8 and 0 <= b - 1 < 8:
                    if R == AL[a - 1] + NL[b - 1] and 0 <= c - 1 < 8 and 0 <= d - 1 < 8:
                        R = AL[c - 1] + NL[d - 1]
                        K = AL[a - 1] + NL[b - 1]
                    elif R != AL[a - 1] + NL[b - 1]:
                        K = AL[a - 1] + NL[b - 1]
        else:
            a = AL.index(K[0])
            b = NL.index(K[1])
            c = AL.index(R[0])
            d = NL.index(R[1])
            if 0 <= a - 1 < 8 and 0 <= b < 8:
                if R == AL[a - 1] + NL[b] and 0 <= c - 1 < 8 and 0 <= d < 8:
                    R = AL[c - 1] + NL[d]
                    K = AL[a - 1] + NL[b]
                elif R != AL[a - 1] + NL[b]:
                    K = AL[a - 1] + NL[b]
print(K)
print(R)
