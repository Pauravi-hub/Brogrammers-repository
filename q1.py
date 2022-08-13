T=int(input())
if 1 <= T <=1000:
    for test in range(T):
        X=int(input())
        if 1 <= X <= 1000:
            print((X)%10)
        else:
            print('Invalid Testcase!')
else:
    print('Test cases out of range')

