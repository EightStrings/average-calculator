def grade_average_calculator():
    print("Welcome to the Grade Average Calculator!")
    num_subjects = int(input("How many subjects would you like to calculate? "))

    averages = {}
    for _ in range(num_subjects):
        try:
            subject = input("Enter the name of the subject: ")
            num_grades = int(input(f"Enter the number of grades for {subject}: "))

            grades = []
            for i in range(num_grades):
                grade = int(input(f"Enter grade {i + 1} for {subject}: "))
                grades.append(grade)

            average = sum(grades) / num_grades
            averages[subject] = average

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("Results:")
    for subject, average in averages.items():
        print(f"{subject} = {average}")

grade_average_calculator()
