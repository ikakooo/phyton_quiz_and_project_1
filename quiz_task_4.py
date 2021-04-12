def fib(s):
    if s==0:
        return 0
    elif s==1 or s==2:
        return 1
    else:
        return fib(s-1)+fib(s-2)
def saveInFile(a):
    fileforfun=open('./Desktop/file.txt','w')
    fileforfun.write(a)
    fileforfun.close()
    
saveInFile(str(fib(10)))