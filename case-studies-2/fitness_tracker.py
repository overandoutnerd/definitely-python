activityLogs = [
    {"day": "Mon", "steps": 2500, "calories": 250, "goalMet": False},
    {"day": "Tue", "steps": 12400, "calories": 480, "goalMet": False},
    {"day": "Wed", "steps": 2600, "calories": 100, "goalMet": False},
    {"day": "Thu", "steps": 10000, "calories": 450, "goalMet": False},
    {"day": "Fri", "steps": 3400, "calories": 510, "goalMet": False},
    {"day": "Sat", "steps": 8700, "calories": 350, "goalMet": False},
    {"day": "Sun", "steps": 6200, "calories": 190, "goalMet": False}
]

for activity in activityLogs:
    if activity["steps"] >= 5000 and activity["calories"] >= 200:
        activity["goalMet"] = True
    else:
        activity["goalMet"] = False

totalSteps = 0
totalCalories = 0
goalMetDays = 0

for activity in activityLogs:
    steps = int(activity["steps"])
    calories = int(activity["calories"])

    totalSteps += steps
    totalCalories += calories

    if activity["goalMet"]:
        goalMetDays += 1

if len(activityLogs) > 0:
    averageSteps = totalSteps / len(activityLogs)
    averageSteps = int(averageSteps)
    goalCompletionRate = (goalMetDays / len(activityLogs)) * 100
else:
    averageSteps = 0
    goalCompletionRate = 0.0


print("\n====================================================")
print("          WEEKLY FITNESS ANALYTICS REPORT")
print("====================================================")
print("Day | Steps  | Calories (kcal) | Daily Goal Met")
print("----------------------------------------------------")

for activity in activityLogs:
    day = activity["day"]
    steps = activity["steps"]
    calories = activity["calories"]

    if activity["goalMet"]:
        goalStatus = "YES"
    else:
        goalStatus = "NO"

    print(f"{day:<3} | {steps:>6,} | {calories:>16} | {goalStatus}")

print("----------------------------------------------------")
print(f"Total Weekly Steps    : {totalSteps:,}")
print(f"Total Weekly Calories : {totalCalories:,} kcal")
print(f"Average Daily Steps   : {averageSteps:,}")
print(f"Goal Completion Rate  : {goalCompletionRate:.1f}%")
print("====================================================")