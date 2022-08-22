def num_isthere(li,ele):
    if(len(li)==1):
        return
    a=num_isthere(li[1:],ele)
    if(li[0]==ele or a):
        return True
    else:
        return False
print(num_isthere([1,2,3,45],4))