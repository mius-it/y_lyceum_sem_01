print(' '.join((str(int(x) ** 2)
                for x in input().split()
                if int(x) % 2 == 1 and str(int(x) ** 2)[-1] != '9' )))
