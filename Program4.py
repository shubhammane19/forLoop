start = int(input("Enter start of range: "))
end  = int(input("Enter end of range: "))

if start<1 or end<1:
    print("Wrong Input")
else:
    for i in range(start,end):
        print(f"ASCII Value: {i},Character :",chr(i))