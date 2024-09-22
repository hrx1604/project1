#Create a list of 15 courses in any order from the given table

courses = ["Introduction to Programming","Calculus I","Data Structures and Algorithms", "Linear Algebra", "Physics I",
         "Chemistry I","Biology I","Microeconomics","Macroeconomics","Psychology I","History I", "English Composition I", 
         "Introduction to Philosophy","Calculus II","Discrete Mathematics"]

# Print the courses list in its original order.

print(courses)

# Sort the courses list alphabetically without modifying the original list.
sort_courses = sorted(courses)
print(sort_courses)

# Print the courses list in reverse alphabetical order using sorted().

reverse_sort_courses = sorted(courses, reverse=True)
print(reverse_sort_courses)
# Reverse the order of the courses list using reverse().
courses.reverse()
print(courses)

# Reverse the courses list back to its original order.
courses.reverse()
print(courses)

# Sort the courses list alphabetically and store it.

courses.sort()
print(courses)

#Sort the courses list in reverse alphabetical order and store it.

courses.sort(reverse=True)
print(courses)


# Use sorted() and print the available courses with a message.

sorted_courses = sorted(courses)
print("The following courses are available for expression of interest if the students meet the prerequisites:")
for course in sorted_courses:
    print(course)
# Replace a course and print a message.

courses[0] = "Advanced Python Programming"
print("The course 'Psychology I' has been replaced with 'Advanced Python Programming'.")
#Insert new courses and append a course.

courses.insert(0, "Artificial Intelligence")
courses.insert(len(courses)//2, "Data Science")
courses.append("Cybersecurity")
print(courses)
# Use pop() to remove courses.

removed_courses = [courses.pop() for _ in range(4)]
print(f"The following courses are unavailable due to technical issues: {', '.join(removed_courses)}")

# Create a list of tuples.

course_data = [ (1, "Introduction to Programming"), (2, "Calculus I"), (3, "Data Structures and Algorithms"),
                (4, "Linear Algebra"), (5, "Physics I"), (6, "Chemistry I"),  (7, "Biology I"),
                (8, "Microeconomics"),(9, "Macroeconomics"), (10, "Psychology I")]

# Loop through tuples and extract names.

course_names = []
for course_id, course_name in course_data:
    course_names.append(course_name)
# Print the course names
print("Course Names:", course_names)