#grades range from 0-100
#passing grade = 40
#if "the next grade that is a multiple of 5" minus grade is lower 3 round up to the next grade
#if grade < 38 never round up since it won't make the passing grade even if rounded up

grades = [73,67,38,33]

def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade < 38:
            rounded_grades.append(grade)
        else:
            if (grade + 1) % 5 == 0:
                grade += 1
                rounded_grades.append(grade)
            elif (grade + 2) % 5 == 0:
                grade += 2
                rounded_grades.append(grade)
            else:
                rounded_grades.append(grade)
    return rounded_grades
        
print(gradingStudents(grades))
