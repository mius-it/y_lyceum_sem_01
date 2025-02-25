print(', '.join(str(x ** 2) for x in range(int(input()) + 1)
                if '0' not in str(x) and
                '2' not in str(x) and
                '3' not in str(x) and
                '4' not in str(x) and
                '5' not in str(x) and
                '6' not in str(x) and
                '7' not in str(x) and
                '8' not in str(x) and
                '9' not in str(x)))
