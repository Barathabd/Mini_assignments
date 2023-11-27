Students_height=(input("Enter a list of students heights:").split( ))
for n in range(0,len(Students_height)):
    Students_height[n]=int(Students_height[n])
    
Number_of_students=0
for students in Students_height:
    Number_of_students+=1
Total_height=0
for height in Students_height:
    Total_height+=height
Average_height=Total_height/Number_of_students
print(round(Average_height))