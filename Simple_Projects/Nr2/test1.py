arn = "arn:aws:iam:123456789:user/johndoe"

#inbuild function for string datatype and numeric = split
print(arn.split("/")[1])  #will show obj 1 = johndoe
print(arn.split("/")[0])  #object 0 before / 