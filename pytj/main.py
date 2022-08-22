arr=input("Enter a number")
count=0
max=0
flag=0
for i in range(0,len(arr)):
    if(arr[i]==0 and flag==0):
        flag=1
        if(flag==0):

            if(arr[i+1]==0):
                if(count>max):
                    max=count
                else:
                    count=count+1
                    if(count>max):
                        max=count
                    flag=0
                    count=0

        else:
            count=count+1
    else:
        count=count+1
    if(i==len(arr)-1):
        max=count
print(max)




