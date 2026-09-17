a=9

if(a>10):
    print("true")
else:
    print("false")

score=int(input("enter a score:",))

if(score>=90):
    print("A")
elif(score>=80):
    print("B")
elif(score>=60):
    print("C")
else:
    print("D")

#Sometimes we want to play PUBG on our phone if the day is Sunday.

day=str(input("enter a day:"))

if("sunday"==day):
         print("we play PUBG")
else:
     print("not play PUBG")

#(A spam comment is defined as a text containing following keywords: “Make a lot of
#money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.)

p1="Make a lot of money"
p2="buy now"
p3="ubscribe this"
p4="lick this"

message=input("enter your comment:")

if((p1 in message)or(p2 in message)or(p3 in message)or (p4 in message)):
     print("this comment is a spam")
else:
     print("this comment is not a spam")
     
