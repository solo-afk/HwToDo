work = []

task = ""

while task != "n":
    
    task = input("Enter hw (n to end)\n")
    if task != "n":
        work.append(task)



for i in range(len(work)):
    num = str(i+1)
    print(num +"."+ work[i])