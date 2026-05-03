students = [
    {"name": "Amit", "marks": 78, "age": 20},
    {"name": "Sneha", "marks": 92, "age": 22},
    {"name": "Rahul", "marks": 65, "age": 19},
    {"name": "Priya", "marks": 88, "age": 21},
    {"name": "John", "marks": 55, "age": 20}
]

#Q1. Extract Student Names
list(map(lambda s: s["name"], students))


#Q2. Students with Marks > 75
list(filter(lambda s: s["marks"] > 75, students))


#Q3. Scholarship Students (>= 85)
list(filter(lambda s: s["marks"] >= 85, students))


#Q4. Names of Failed Students
list(
        map(lambda s: s["name"],
            filter(lambda s: s["marks"] < 60, students))
    )


#Q5. Return names of students:
#	Age > 20
#	Marks > 80
list(
        map(lambda s: s["name"],
            filter(lambda s: s["age"] > 20 and s["marks"] > 80, students))
    )


employees = [
    {"name": "Raj", "salary": 25000},
    {"name": "Simran", "salary": 40000},
    {"name": "Aman", "salary": 18000},
    {"name": "Neha", "salary": 32000}
]

#Q1. High Salary Employees (> 30000)
list(filter(lambda e: e["salary"] > 30000, employees))


#Q2. Names of Low Salary Employees (< 25000)
list(
        map(lambda e: e["name"],
            filter(lambda e: e["salary"] < 25000, employees))
    )

#Q3. Special Filter:
 #    Filter employees: Salary > 20000 and Name starts with 'N'
list(filter(
        lambda e: e["salary"] > 20000 and e["name"].startswith("N"),
        employees
    ))
