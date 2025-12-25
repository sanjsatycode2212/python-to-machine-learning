import numpy as np

students = np.array(["Aman", "Riya", "Satyam", "Neha", "Karan"])

marks = np.array([
    [85, 90, 88],   # Aman
    [78, 82, 80],   # Riya
    [92, 88, 95],   # Satyam
    [70, 75, 72],   # Neha
    [88, 85, 84]    # Karan
])

# total 

total = np.sum(marks,axis=1)
print("total  :-  ",total)

# subject :-
topper_index = np.argmax(total)
# print(topper_index)
print("Overall Topper :-  ", students[topper_index], total[topper_index])
#                        student[2],total[2]

sub1 = np.argmax(marks[:,0])
print(sub1)
print("subject 1 :- ",students[sub1],marks[sub1,0])

sub2 = np.argmax(marks[:,1])
print(sub2)
print("subject 2 :- ",students[sub2],marks[sub2,1])

sub3 = np.argmax(marks[:,2])
print(sub3)
print("subject 3 :- ",students[sub3],marks[sub3,2])

average = np.mean(marks,axis=1)
print(("average :- ",average).astype(int))


