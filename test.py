    add_student("Jane Smith", 22, 3.9, "S1002")
    add_student("John Doe", 20, 3.8, "S1001")
    add_course("MATH201", "Calculus I", 25)
    add_course("CS101", "Introduction to Programming", 30)
    add_course("PHY301", "Physics Fundamentals", 20)
    
 print("Find student S1001:", find_student("S1001").name)
 print("Find course CS101:", find_course("CS101").course_name)