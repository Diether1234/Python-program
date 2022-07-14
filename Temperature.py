c = float(input("Enter a temperature to convert: "))
f = (c * 9/5) + 32
print(f)
if(f>100):
    print("too hot")
elif(f<50):
    print("too cold")
else:
    print("just right")

