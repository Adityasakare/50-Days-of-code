names = input("Enter a name: ").title().split(",")   #  get and process input for a list of names
assignments = input("Enter number of assignments: ").title().split(",")             # get and process input for a list of the number of assignments
grades = input("Enter a grades: ").title().split(",")                   # get and process input for a list of grades

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"
for name, assignment, grade in zip (names, assignments, grades):

	print(message.format(name, assignment, grade,int(grade) + int(assignment)*2))
# message string to be used for each student
# HINT: use .format() with this string in your for loop
