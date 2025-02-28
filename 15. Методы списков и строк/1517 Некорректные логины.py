logins = input().split(',')
bad_logins = []
maxlen = max(len(l) for l in logins)
for l in logins:
    if not l.replace('_','').isalnum():
        bad_logins.append(l)
bad_logins.sort()
print('\n'.join(l.rjust(maxlen,' ') for l in bad_logins))