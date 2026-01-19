# Simple Jumping Jacks Workout

total_jacks = 100
done_jacks = 0
set_size = 10

for i in range(0, total_jacks, set_size):
    done_jacks += set_size
    print(f"You did {done_jacks} jumping jacks so far.")
    
    tired = input("Are you tired? (yes/y or no/n): ").lower()
    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip remaining sets? (yes/y or no/n): ").lower()
        if skip == "yes" or skip == "y":
            print(f"You completed a total of {done_jacks} jumping jacks.")
            break
else:
    print("Congratulations! You completed the workout.")
