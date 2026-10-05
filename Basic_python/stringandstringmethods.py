name="ranit"
nameshort=name[0:3]#start from index 0 all the way till 3(excluding 3)
print(nameshort)

name="ranitdutta"
s=name[0:10]
print(s)
s=name[-4:-1]#we calculate 1:4 (right to left)
print(s)

#so,string is imutable,not changeable just new string create

#string function

name="ranit dutta"
print(len(name))#len()function(calculate length of the string)
print(name.endswith("tta"))#check string is end with given text(true or false)
print(name.count("a"))#count same character in present string
print(name.capitalize())# convert capital letter in first character
print(name.find("a"))#returns the index of first occurrence
print(name.replace(""," "))
print(name.replace("t","a"))#replace the position

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>","Ranit").replace("<|Date|>","1 january"))
