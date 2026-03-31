print("SMART STUDY PLANNER\n")

subjects = []

n = int(input("How many subjects? "))

for i in range(n):
    print(f"\nEnter details for subject {i+1}")
    
    name = input("Subject name: ")
    deadline = int(input("Days left for exam: "))
    difficulty = int(input("Difficulty (1-5): "))
    
    # Priority formula (AI-like logic)
    priority = (10 - deadline) + difficulty * 2
    
    subjects.append([name, deadline, difficulty, priority])

# Sort by priority (highest first)
subjects.sort(key=lambda x: x[3], reverse=True)

print("\n YOUR STUDY PLAN:\n")

for sub in subjects:
    print(f" {sub[0]}")
    print(f"   Deadline: {sub[1]} days")
    print(f"   Difficulty: {sub[2]}")
    print(f"   Priority Score: {sub[3]}")
    
    if sub[3] > 10:
        print(" Study 2-3 hours daily")
    elif sub[3] > 5:
        print(" Study 1-2 hours daily")
    else:
        print(" Light revision")
    
    print()