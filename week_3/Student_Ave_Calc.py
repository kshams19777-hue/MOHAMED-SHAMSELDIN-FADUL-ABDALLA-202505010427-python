# Loop to allow entering marks for multiple students
while True:
    print("\n--- Student Mark Calculator ---")
    
    # 1. Ask the user to enter three quiz marks
    quiz1 = float(input("Enter Quiz 1 mark: "))
    quiz2 = float(input("Enter Quiz 2 mark: "))
    quiz3 = float(input("Enter Quiz 3 mark: "))

    # 2. Calculate the average mark
    average = (quiz1 + quiz2 + quiz3) / 3

    # 3. Display the average
    print("Average Mark:", average)

    # 4. Determine whether the student passes or fails (Passing mark is 50)
    if average >= 50:
        print("Status: Pass")
    else:
        print("Status: Fail")

    # 5. Allow another student's marks to be entered
    another = input("Do you want to enter another student's marks? (yes/no): ")
    
    # If the user types anything other than 'yes', exit the loop
    if another != "yes":
        print("Goodbye!")
        break