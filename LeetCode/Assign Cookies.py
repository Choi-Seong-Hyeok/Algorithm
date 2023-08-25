g = [1,2]
s = [1,2,3]

g = sorted(g)
s = sorted(s)
g_max = g[-1]
s_max = s[-1]

if s_max >= g_max:
    print(len(g))
else:
    for i in range(len(g)-1,-1,-1):
        if g[i] <= s_max:
            g = g[:i+1]
            print(len(g))
    print(0)
            


