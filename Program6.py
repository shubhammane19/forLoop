start = (input("Enter start range: "))
end  = (input("Enter end range: "))

num1 = ord(start)
num2 = ord(end)
for i in range(num1,num2):
    print(f"ASCII Value : {i},Character: ",chr(i))