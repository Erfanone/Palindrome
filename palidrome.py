a=input("Enter Text:")
txt=""
for char in a:
    txt=char+txt
if a==txt:
    print("True")
else:
    print("False")