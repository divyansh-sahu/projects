lisline = []
lisamount = []
lisoutput = []
lisindex = []

def Order(Id, amount):
    lisline.append(Id)
    lisamount.append(amount)

def Serve():
    if len(lisline) == 0:
        lisoutput.append("Invalid")
        # print("Invalid")
    else:
        p = max(lisamount)
        q = lisamount.index(p)
        lisamount.pop(q)
        lisline.pop(q)

def Highest():
    if len(lisline) == 0:
        lisoutput.append("Invalid")
        # print("Invalid")
    else:
        p = max(lisamount)
        q = lisamount.index(p)
        lisoutput.append(lisline[q])
        # print(lisline[q])


def testcase():
    n = int(input())
    for j in range(1, n+1):
        b = str(input())
        lis = b.split(" ")
        if len(lis) == 3:
            function = lis[0]
            Id = int(lis[1])
            amount = int(lis[2])
            Order(Id, amount)
        else:
            function = lis[0]
            if function == "Highest":
                Highest()
            elif function == "Serve":
                Serve()
    for k in range(0, len(lisoutput)):
        print(lisoutput[k])

testcase()
