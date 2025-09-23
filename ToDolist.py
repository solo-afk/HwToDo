activities = []
dates = []
times = []

print("\nThis is your To-Do list!!!")
print("press a to add new activity\n")

ans = input()

def addactivity():
    print("What activity do you want to add?")
    activity = input()
    activities.append(activity)
    
    print(f"What is the date of {activity}?")
    date = input()
    dates.append(date)

    print("Does this activity have a specific time? (y/n)")
    time = input()
    if time == "y":
        print("What time is it?")
        time = input()
        times.append(time)
    else:
        times.append("none")

def another():
    print("Do you want to add another activity? (y/n)")
    again = input()
    if ans == "a":
        addactivity()
        again = input()
    if again == "y":
        addactivity()


if ans == "a":
    addactivity()
    another()

else:
    print("You have nothing to do")

print("Your to do list:")
for i in range(len(activities)):
    if times[i] != "none":
        print(f"{i+1}. {activities[i]} on {dates[i]} at {times[i]}")
    else:
        print(f"{i+1}. {activities[i]} on {dates[i]}")

