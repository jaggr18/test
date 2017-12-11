def calculate_grade(points_achieved, max_points):
    grade = (points_achieved / max_points) * 5 + 1
    return round(grade, 1)


def add_grade(filename, mode="w"):
    with open(filename, mode) as outfile:
        while True:
            should_continue = input("\nWould you like to add an exam? [y/n]\n")
            if should_continue.lower() == "n":
                break
            lecture = input("What is the title of the lecture?\n")
            semester = input("Which semester was it?\n")
            max_points = float(input("What was the maximum number of points?\n"))
            your_points = float(input("How many points did you get?\n"))
            ects = input("How many ECTS points did you get?\n")

            grade = str(calculate_grade(your_points, max_points))
            outfile.write(ects+"\t"+grade+"\t"+lecture+"\t"+semester+"\n")
