import csv
import random

headers = ["Roll No", "Name", "Class", "Age", "Marks"]

names = [
    "Aarav", "Ananya", "Rohan", "Kavya", "Arjun",
    "Ishita", "Rahul", "Sneha", "Aditya", "Nisha",
    "Karan", "Pooja", "Aman", "Priya", "Siddharth",
    "Meera", "Ritik", "Simran", "Varun", "Neha"
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    for i in range(20):
        row = [
            i+1,
            names[i],
            f"10{random.choice(['A','B','C'])}",
            random.randint(14, 18),
            random.randint(40, 100)
        ]
        writer.writerow(row)

print("✅ students.csv created with data ")
