strs = [input(),input(),input()]
maxlen = max(len(s) for s in strs)
step = min(len(s) for s in strs)
for i in range(2, -1, -1):
    if len(strs[i]) == maxlen or len(strs[i]) == step:
        strs.pop(i)
minlen = len(strs[0])

for num in range(maxlen, minlen, -step):
    print(num, end=' ')