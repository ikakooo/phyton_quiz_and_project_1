import random

emptyTuple = ()


for i in range(100):
    emptyTuple +=(random.randrange(0,1000),)
    
    
    
def oddElemets(x):
    oddNumbers= ()
    for j in x:
      if j%2==0:
        oddNumbers+=(j,)
    return  oddNumbers
def evenElements(e):
     evenNumbers= ()
     for j in e:
      if j%2==1:
        evenNumbers+=(j,)
     return  evenNumbers
     
def devideByThree(w):
     NumbersdevideByThree= ()
     for j in w:
      if j%3==0:
        NumbersdevideByThree+=(j,)
     return  NumbersdevideByThree     
     
     
     
print(oddElemets(emptyTuple))   
print(evenElements(emptyTuple)) 
print(devideByThree(emptyTuple))   