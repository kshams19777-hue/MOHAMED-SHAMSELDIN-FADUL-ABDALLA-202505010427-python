# ACTIVITY: Week 3 Documentation

## 1. Identify the Components
* **1.1. What are the inputs?**
    * Three quiz marks from the user (e.g., Quiz 1, Quiz 2, and Quiz 3).
* **1.2. What is the process?**
    * Take the three inputs.
    * Calculate the average using the formula: (Quiz 1 + Quiz 2 + Quiz 3) / 3.
    * Check if the average is greater than or equal to 50 to determine if the student passes or fails.
    * Repeat the process if the user wants to enter marks for another student.
* **1.3. What is the output?**
    * The calculated average mark.
    * The final status (PASS or FAIL).

---

## 2. Design the Algorithm (Pseudocode)
```text
START
    LOOP
        INPUT quiz1, quiz2, quiz3
        COMPUTE average = (quiz1 + quiz2 + quiz3) / 3
        OUTPUT "Average Mark: " + average
        IF average >= 50 THEN
            OUTPUT "Status: PASS"
        ELSE
            OUTPUT "Status: FAIL"
        ENDIF
        INPUT choice ("Do you want to enter marks for another student? yes/no")
    UNTIL choice is NOT "yes"
END