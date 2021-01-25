a = int(input("a: "))
b = int(input("b: "))
#S1 = int(input("S1: "))
#S2 = int(input("S2: "))
#t1 = int(input("t1: "))
#t2 = int(input("t2: "))

a1 = a
b1 = b
S1 = 1
S2 = 0
t1 = 0
t2 = 1

print(f"\na={a} b={b} S1={S1} S2={S2} t1={t1} t2={t2}\n")

while b != 0:
    q = a // b
    r = a - (q * b)

    a = b
    b = r
    print(f"q={q}  r={r}  a={a}  b={b}")

    S = S1 - (q * S2)
    S1 = S2
    S2 = S
    print(f"S={S}  S1={S1}  S2={S2}")

    t = t1 - (q * t2)
    t1 = t2
    t2 = t
    print(f"t={t}  t1={t1}  t2={t2}\n")

print(f"nod({a1},{b1}) = {a}")
