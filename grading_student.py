# Time complexity 1
# Space complexity 1

def gradingStudents(grades):

    for i, grade in enumerate(grades):
        if grade >= 38:
            nextMultipleoffive = ((grade//5)+1)*5
            difference = nextMultipleoffive - grade

            if difference < 3:
                grades[i] = nextMultipleoffive
    return grades


print(gradingStudents([73, 67, 38, 33]))
