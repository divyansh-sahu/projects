a=[2,1,3,4,5]
def fu (lis):
    if(len(lis)==1):
        return True
    newlist=lis[1:]
    so=fu(newlist)
    if(lis[0]<newlist[0] and so==True):
        so=True
    else:
        so=False
    return so

print(fu(a))