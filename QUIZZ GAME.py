print("Welcome to the quiz game!")
print("When you answer the question, please use underscores for correct understanding.")

score = 0  # Initialize score

question = input("Do you want to play the game? ").lower()
if question != "yes":
    print("Ohh, it's okay.")
    quit()
else:
    print("Whoa, let's play!")

# Question 1
question1 = input("What is the full form of CPU? ")
if question1.lower() == "central_processing_unit":
    print("WOAH, RIGHT ANSWER!!")
    score += 1  # Increment score for correct answer
else:
    print("HMM, WRONG ANSWER!!")

# Question 2
question2 = input("What is the full form of GPU? ")
if question2.lower() == "graphics_processing_unit":
    print("WOAH, RIGHT ANSWER!!")
    score += 1
else:
    print("HMM, WRONG ANSWER!!")

# Question 3
question3 = input("What is the full form of RAM? ")
if question3.lower() == "random_access_memory":
    print("WOAH, RIGHT ANSWER!!")
    score += 1
else:
    print("HMM, WRONG ANSWER!!")

# Question 4
question4 = input("What is the full form of ROM? ")
if question4.lower() == "read_only_memory":
    print("WOAH, RIGHT ANSWER!!")
    score += 1
else:
    print("HMM, WRONG ANSWER!!")

# Question 5
question5 = input("What is the full form of USB? ")
if question5.lower() == "universal_serial_bus":
    print("WOAH, RIGHT ANSWER!!")
    score += 1
else:
    print("HMM, WRONG ANSWER!!")

# Display the final score
print(f"Congratulations! You finished the quiz with a score of {score}/5.")