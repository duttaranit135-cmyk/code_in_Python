f= open("myfile.txt", "r")#open file
# Read its contents
text = f.read()
if("boy"in text):
    print("it is present")
else:
    print("it is not present")
# Print its contents
print(text)
# Close the file
f.close()

f=open("myfile1.txt","w")
text=f.write("ranit is a student of jis college of engineering")
f.close()

f=open("readline.txt","r")
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
f.close()
