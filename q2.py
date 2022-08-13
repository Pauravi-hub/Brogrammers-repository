T = int(input())
if 1 <= T <= 1000:
    for x in range(T):
        x,y = map(int,input().split())
        if x >= 100 and y <= 200 and x != y: 
            if x > y:
                print("A")
            else:
                print("B")
        else:
            print("input doesnt follow constraints")
else:
    print("test cases not in range")

