def grading_system():
    table = []
    while True:
        student_name = input("Enter the student's name: ").strip().lower()
        if student_name.isalpha():
            while True:
                try:
                    score = float(input("Enter the student's score (0-100): "))
                    if score < 0 or score > 100:
                        print("Invalid score. Please enter a value between 0 and 100.")    
                    elif 90 <= score <= 100:
                        print(f"{student_name} received an A.")
                        table.append((student_name, score, 'A'))
                        break
                    elif 80 <= score < 90:
                        print(f"{student_name} received a B.")
                        table.append((student_name, score, 'B'))    
                        break
                    elif 70 <= score < 80:
                        print(f"{student_name} received a C.") 
                        table.append((student_name, score, 'C'))
                        break
                    elif 60 <= score < 70:
                        print(f"{student_name} received a D.") 
                        table.append((student_name, score, 'D'))
                        break
                    else:
                        print(f"{student_name} received an F.")
                        table.append((student_name, score, 'F'))
                        break
             
                except ValueError:
                    print("Invalid input. Please enter a numeric value for the score.")
        else:
            print("Invalid input. Please enter a valid name consisting of alphabetic characters only.")
            continue
        end = input("Do you want to enter another student's score? (yes/no): ").strip().lower()

        if end != 'yes':
                print(table)
                return 
                


           













grading_system()