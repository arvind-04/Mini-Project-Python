# Function to print the name of student who
names=input("Enter List of Name: ").split(',')
marks=input("Enter list of Marks: ").split(',')
updates=input("Enter List of Updated Marks: ").split(',')
n = len(marks)
def nameRank(names, marks, updates, n):
    x = [[0 for j in range(3)] for i in range(n)]
    for i in range(n):
        x[i][0] = names[i]                     # Store the name of the student
        x[i][1] = marks[i] + updates[i]        # Update the marks of the student
        x[i][2] = i + 1                        # Store the current rank of the student
    highest = x[0]
    for j in range(1, n):
        if (x[j][1] >= highest[1]):
            highest = x[j]
    print("Name: ", highest[0], ", Jump: ",abs(highest[2] - 1), sep="")
    
nameRank(names, marks, updates, n)
