print('\n'.join([','.join([num for num in nums.split(',')
                           if int(num) >= 10**9])
                 for nums in input().split(';')]))
