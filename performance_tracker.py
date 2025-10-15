def calculate_average(marks):
    return sum(marks) / len(marks)
def track_performance(students):
    averages = {name: round(calculate_average(scores), 2) for name, scores in students.items()}
    top_student = max(averages, key=averages.get)
    return averages, top_student
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
averages, top = track_performance(students)
print("Average Marks:", averages)
print("Top Performer:", top)
