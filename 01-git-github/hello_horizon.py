name = "Boutaina"
profession = "Computer Science Lecturer"
goal = "Become a Data Engineering professional"

print("Welcome to Project Horizon 2027!")
print(f"Name: {name}")
print(f"Profession: {profession}")
print(f"Goal: {goal}")
skills = ["Python", "SQL", "Git", "Data Engineering"]

print("\nSkills I want to develop:")
for skill in skills:
    print(f"- {skill}")
# Project Horizon 2027 - Learning Progress

learning_goals = {
    "Git & GitHub": "In Progress",
    "Advanced SQL": "Not Started",
    "Data Engineering": "Not Started",
    "Microsoft Azure": "Not Started"
}

print("\nMy Learning Progress:")

for topic, status in learning_goals.items():
    print(f"{topic}: {status}")