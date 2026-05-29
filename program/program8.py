data = [
  {
    "id": 1,
    "name": "Anshu",
    "age": 19,
    "city": "Bhopal",
    "course": "Python ML",
    "marks": 88
  },
  {
    "id": 2,
    "name": "Rahul",
    "age": 21,
    "city": "Indore",
    "course": "Data Science",
    "marks": 72
  },
  {
    "id": 3,
    "name": "Priya",
    "age": 20,
    "city": "Delhi",
    "course": "AI",
    "marks": 45
  },
  {
    "id": 4,
    "name": "Karan",
    "age": 22,
    "city": "Mumbai",
    "course": "Web Dev",
    "marks": 91
  },
  {
    "id": 5,
    "name": "Sneha",
    "age": 18,
    "city": "Pune",
    "course": "Cyber Security",
    "marks": 67
  }
]

for i in data:
    row = [
        i["id"],
        i["name"]
    ]
    print(row)