n = int(input("which number factors you want: "))

count = 0
for i in range(1, n+1): 
    if n % i == 0:
        count = count+1
        print(i)

print(f"Total factors: {count}")