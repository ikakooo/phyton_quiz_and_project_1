import string

def encrypt(st):
    y=7
    letters = string.ascii_lowercase + string.ascii_lowercase + string.ascii_uppercase + string.ascii_uppercase
    for i in range(0,len(st)):
        if letters.find(st[i])!=-1:
            st=st[:i]+letters[letters.find(st[i])+y]+st[i+1:]
    return st
    
def decrypt(st):
    y=7
    letters = string.ascii_lowercase + string.ascii_lowercase + string.ascii_uppercase + string.ascii_uppercase
    letters = letters[::-1]
    for i in range(0,len(st)):
        if letters.find(st[i])!=-1:
            st=st[:i]+letters[letters.find(st[i])+y]+st[i+1:]
    return st

inputChar=" "
while "d"!=inputChar and inputChar!="e":
    inputChar=input("Enter E or D: ").lower()
    if inputChar=="e":
      print(encrypt("ikakofghfoo"))
    elif "d"==inputChar :
        print(decrypt("ikakoo"))
    else: print("Upss!!!! try again!!")  