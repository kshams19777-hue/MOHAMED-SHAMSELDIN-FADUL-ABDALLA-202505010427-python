# WEEK 2 - TUTORIAL 2

## Scenario

A movie theater has the following admission policy:

- Users are 18 years old or older, OR
- Users are accompanied by an adult.
- Users must have a valid ticket.

A person is allowed to enter if:

((Age >= 13) OR AccompaniedByAdult) AND ValidTicket

---

# 1. Identify the Components

## 1.1 Inputs

- Age
- AccompaniedByAdult (True/False)
- ValidTicket (True/False)

## 1.2 Process

Check whether:

(Age >= 13 OR AccompaniedByAdult = True)
AND
ValidTicket = True

## 1.3 Output

- Allow Entry
- Deny Entry

---

# 2. Design the Algorithm

## 2.1 Flowchart

```text
 ┌───────┐
 │ Start │
 └───┬───┘
     │
     ▼
┌─────────────────────┐
│ Input Age           │
│ Input Adult         │
│ Input Ticket        │
└─────────┬───────────┘
          │
          ▼
 ┌──────────────────┐
 │ Valid Ticket ?   │
 └──────┬─────┬─────┘
        │Yes  │No
        ▼     ▼
 ┌──────────┐ ┌──────────┐
 │Age>=13 ? │ │Deny Entry│
 └───┬──┬───┘ └────┬─────┘
     │Yes│No       │
     ▼   ▼         ▼
┌──────────┐ ┌─────────────┐
│Allow     │ │Accompanied? │
│Entry     │ └─────┬───┬───┘
└────┬─────┘       │Yes│No
     │             ▼   ▼
     │       ┌────────┐ ┌──────────┐
     │       │ Allow  │ │Deny Entry│
     │       │ Entry  │ └────┬─────┘
     │       └────┬───┘      │
     └────────────┴──────────┘
                  ▼
               ┌─────┐
               │ End │
               └─────┘
```

## 2.2 Truth Table

| Age >= 13 | Accompanied Adult | Valid Ticket | Allow Entry |
| ---------- | ------------------ | ------------ | ----------- |
| T | T | T | T |
| T | T | F | F |
| T | F | T | T |
| T | F | F | F |
| F | T | T | T |
| F | T | F | F |
| F | F | T | F |
| F | F | F | F |

## 2.3 Step-by-Step Algorithm

1. Start
2. Input Age
3. Input AccompaniedByAdult
4. Input ValidTicket
5. If ValidTicket = False
      Display "Deny Entry"
6. Else
      If Age >= 13 OR AccompaniedByAdult = True
            Display "Allow Entry"
      Else
            Display "Deny Entry"
7. End

## 2.4 Pseudocode

```text
BEGIN

INPUT Age
INPUT AccompaniedByAdult
INPUT ValidTicket

IF ValidTicket = TRUE THEN

    IF Age >= 13 OR AccompaniedByAdult = TRUE THEN
        OUTPUT "Allow Entry"
    ELSE
        OUTPUT "Deny Entry"
    ENDIF

ELSE
    OUTPUT "Deny Entry"

ENDIF

END
```

---

# 3. Evaluate Expression

## 3.1 Test Input Samples

### Test Case 1

Input:

Age = 15
AccompaniedByAdult = False
ValidTicket = True

Output:

Allow Entry

### Test Case 2

Input:

Age = 10
AccompaniedByAdult = True
ValidTicket = True

Output:

Allow Entry

### Test Case 3

Input:

Age = 15
AccompaniedByAdult = False
ValidTicket = False

Output:

Deny Entry

### Test Case 4

Input:

Age = 10
AccompaniedByAdult = False
ValidTicket = True

Output:

Deny Entry
