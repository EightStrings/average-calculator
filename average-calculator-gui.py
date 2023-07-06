import tkinter as tk
from tkinter import messagebox, simpledialog

def create_input_fields():
    num_subjects = int(num_subjects_entry.get())

    for i in range(num_subjects):
        subject_label = tk.Label(window, text=f"Subject {i+1}:")
        subject_label.pack()

        subject_entry = tk.Entry(window)
        subject_entry.pack()
        subjects_entries.append(subject_entry)

        num_grades_label = tk.Label(window, text=f"Number of grades for Subject {i+1}:")
        num_grades_label.pack()

        num_grades_entry = tk.Entry(window)
        num_grades_entry.pack()
        num_grades_entries.append(num_grades_entry)

    create_fields_button.config(state=tk.DISABLED)
    calculate_button.config(state=tk.NORMAL)
    create_fields_button.pack_forget()

def enter_grades():
    for i in range(len(subjects_entries)):
        subject = subjects_entries[i].get()
        num_grades = int(num_grades_entries[i].get())

        grades_row = []
        for j in range(num_grades):
            grade = simpledialog.askfloat(f"Grade for Subject {i+1}", f"Enter grade {j+1} for: {subject}")
            grades_row.append(grade)

        grades_entries.append(grades_row)

    calculate_averages()

def calculate_averages():
    averages = {}

    for i in range(len(subjects_entries)):
        subject = subjects_entries[i].get()
        grades_row = grades_entries[i]
        num_grades = len(grades_row)
        grades = []

        for j in range(num_grades):
            grade = grades_row[j]
            grades.append(grade)

        average = sum(grades) / num_grades
        averages[subject] = average

    messagebox.showinfo("Results", f"Results:\n{averages}")

# Create the main window
window = tk.Tk()
window.title("Grade Calculator")
window.geometry("400x300")
# Greeting popup
messagebox.showinfo("Welcome", "Welcome to the Average Grade Calculator!")

# Label and input field for the number of subjects
num_subjects_label = tk.Label(window, text="How many subjects do you want to calculate?")
num_subjects_label.pack()

num_subjects_entry = tk.Entry(window)
num_subjects_entry.pack()

# Button to create input fields for subjects and number of grades
create_fields_button = tk.Button(window, text="OK", command=create_input_fields)
create_fields_button.pack()

# Lists to store the input entries for subjects, number of grades, and grades
subjects_entries = []
num_grades_entries = []
grades_entries = []

# Button to calculate the averages
calculate_button = tk.Button(window, text="Calculate", command=enter_grades, state=tk.DISABLED)
calculate_button.pack()

# Start the application
window.mainloop()
