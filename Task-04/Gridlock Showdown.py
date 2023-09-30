t=int(input())
for i in range (t):
    l=[]
    main=[]
    c=0
    for i in range (3):
        x=input()
        l=[x[0],x[1],x[2]]
        main.append(l)
    while True:
        if main[0][0]==main[1][0] and main[0][0]==main[2][0] and main[0][0]!=".":
            print(main[0][0])
            break
        elif main[0][1]==main[1][1] and main[0][1]==main[2][1] and main[0][1]!=".":
            print(main[0][1])
            break
        elif main[0][2]==main[1][2] and main[0][2]==main[2][2] and main[0][2]!=".":
            print(main[0][2])
            break
        elif main[0][0]==main[0][1] and main[0][0]==main[0][2] and main[0][0]!=".":
            print(main[0][0])
            break
        elif main[1][0]==main[1][1] and main[1][0]==main[1][2] and main[1][0]!=".":
            print(main[1][0])
            break
        elif main[2][0]==main[2][1] and main[2][0]==main[2][2] and main[2][0]!=".":
            print(main[2][0])
            break
        elif main[0][0]==main[1][1] and main[0][0]==main[2][2] and main[0][0]!=".":
            print(main[0][0])
            break
        elif main[0][2]==main[1][1] and main[0][2]==main[2][0] and main[0][2]!=".":
            print(main[0][2])
            break
        else:
            print("DRAW")
            break