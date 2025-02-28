vals = [int(v) for v in input().split()]
lv = len(vals)
vs = sorted(vals)
med = vs[lv // 2]
mod = max([(vals.count(v), v) for v in set(vals)])[1]
#mod = max(vals, key=vals.count)

print(med, mod)