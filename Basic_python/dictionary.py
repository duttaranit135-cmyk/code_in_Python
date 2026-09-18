marks={
    "ranit":100,
    "shubham":56,
    "rohan":23,
    96:"ayon"

}

print(marks,type(marks))
print(marks["ranit"])
#its mutable

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"ranit":99,"rimi":96})
print(marks)
print(marks.get("arohi"))#print none
print(marks.get("ranit"))#let,like(print(marks["ranit2"])) it is error

words={
    "madad":"help",
    "kursi":"chair"
}

word=input("enter the word you meaning of:")
print(word[word])