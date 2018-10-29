import random
text=input()
new = ""
numbcap=0
numblow=0
for i in range (len(text)):
    if bool(random.getrandbits(1)):#i%2==0: bool(random.getrandbits(1)):
        new+=text[i].capitalize()
        numbcap+=1
    else:
        new+=text[i]
        numblow+=1

    if numbcap > 2:
        new = new[:-1]
        new+=text[i]
        numbcap=0
    if numblow > 2:
        new = new[:-1]
        new+=text[i].capitalize()
        numblow=0
        
print(new)
