start = int(input("Enter start of range: "))
end  = int(input("Enter end of range: "))
count = 0
prod = 1

for i in range(start,end):
    if i%2 != 0:
        count = count +1
        
prod = count**count
print(prod)
