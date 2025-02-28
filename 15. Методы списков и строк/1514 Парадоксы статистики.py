n = int(input())
list_vals = []
med = []
mod = []

for _ in range(n):
    list_vals.append([int(v) for v in input().split()])

for vals in list_vals:
    lv = len(vals)
    vs = sorted(vals)
    med.append(vs[lv // 2])
    mod.append(max(vals, key=vals.count))

print(' '.join(str(m) for m in med))
print(' '.join(str(m) for m in mod))

print(med[len(med) // 2])
print(max(mod, key=mod.count))

allvals = sorted([item for sublist in list_vals for item in sublist])
print(allvals[len(allvals) // 2])
print(max(allvals, key=allvals.count))
