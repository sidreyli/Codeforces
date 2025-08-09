def watermelon():
    n = input()
    if int(n) % 2 == 1:
        print("NO")
    else:
        for i in range(2,int(n)-1):
            j = int(n) - i
            if j % 2 == 0 and i % 2 == 0:
                print("YES")
                return
        print("NO")
watermelon()