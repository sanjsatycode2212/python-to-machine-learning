list = [1,2,4.0,5.3,85,500.2,000.0]
count = 0
for i in range(len(list)):
    if type(list[i]) == int:
            print(f"this {i} is an integer")
            count += 1
    else:
            print(f"this {i} are float")
            count += 1
            print(count)