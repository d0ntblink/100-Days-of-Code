# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
totalheight = 0
stunum = 0
for height in student_heights :
    totalheight += height
    stunum += 1
'''stunum = len(student_heights)
totalheight = sum(student_heights)'''
print(f"average student height is {totalheight // stunum}")



