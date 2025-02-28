vals = [int(v) for v in input().split()]
lv = len(vals)

srar = sum(vals) / lv

vs = sorted(vals)
if lv % 2 == 1:
    med = float(vs[lv // 2])
else:
    med = (vs[lv // 2 - 1] + vs[lv // 2]) / 2

print(srar, med)