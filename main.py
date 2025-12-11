import heapq

class Student:
  def __init__(self, name, age, gpa, student_id,prerequisites=None):
      self.name = name 
      self.age = age
      self.gpa = gpa
      self.student_id = student_id
      self.prerequisites = prerequisites if prerequisites is not None else []
      self.registered_class = []
      self.completed_class = []

def has_completed(self, course_code):
        return any(course.course_code == course_code for course in self.completed_courses)



class Course:
    def __init__(self, course_code, course_name, capacity,prerequisites=None):
            self.course_code = course_code
            self.course_name = course_name
            self.capacity = capacity
            self.enrolled_students = []
            self.prerequisites = prerequisites or [] 

    def __lt__(self, other):
        return self.course_code < other.course_code



student1 = Student("favour", 21, 4.0, "S1001", prerequisites=[])
student2 = Student("eunice", 20, 3.9, "S1002", prerequisites=[])
student3 = Student("crispine", 20, 3.8,"S1003", prerequisites=[])
student4 = Student("chima", 25, 3.5, "S1004", prerequisites=[])
student5 = Student("alex", 18, 2.0, "S1005", prerequisites=[])
student6 = Student("jay", 26, 2.1, "S1006", prerequisites=[])
student7 = Student("tom", 17, 3.2, "S1007", prerequisites=[])
student8 = Student("bradley", 31, 1.1, "S1008", prerequisites=[])
student9 = Student("vicky", 22, 2.9, "S1009", prerequisites=[])
student10 = Student("ewo", 26, 3.3, "S1010", prerequisites=[])
student11 = Student("benjamin", 21, 3.1, "S1011", prerequisites=[])
student12 = Student("mia", 22, 3.9, "S1012", prerequisites=[])
student13 = Student("lucas", 20, 3.3, "S1013", prerequisites=[])
student14 = Student("charlotte", 23, 3.7, "S1014", prerequisites=[])
student15 = Student("henry", 19, 3.5, "S1015", prerequisites=[])
student16 = Student("amelia", 21, 4.0, "S1016", prerequisites=[])
student17 = Student("alexander", 22, 3.6, "S1017", prerequisites=[])
student18 = Student("harper", 20, 3.1, "S1018", prerequisites=[])
student19 = Student("daniel", 24, 3.2, "S1019", prerequisites=[])
student20 = Student("evelyn", 19, 3.9, "S1020", prerequisites=[])
student21 = Student("michael", 21, 3.4, "S1021", prerequisites=[])
student22 = Student("ethan", 22, 3.7, "S10022", prerequisites=[])
student23 = Student("abigail", 20, 2.9, "S1023", prerequisites=[])
student24 = Student("matthew", 21, 3.3, "S1024", prerequisites=[])
student25 = Student("ella", 23, 3.8, "S1025", prerequisites=[])
student26 = Student("samuel", 19, 3.5, "S1026", prerequisites=[])
student27 = Student("scarlett", 22, 4.0, "S1027", prerequisites=[])
student28 = Student("david", 20, 3.6, "S1028", prerequisites=[])
student29 = Student("grace", 24, 3.7, "S1029", prerequisites=[])
student30 = Student("joseph", 21, 2.2, "S1030", prerequisites=[])
student31 = Student("chloe", 19, 3.9, "S1031", prerequisites=[])
student32 = Student("carter", 22, 3.4, "S1032", prerequisites=[])
student33 = Student("victoria", 20, 3.8, "S1033", prerequisites=[])
student34 = Student("john", 23, 1.1, "S1034", prerequisites=[])
student35 = Student("riley", 21, 3.7, "S1035", prerequisites=[])
student36 = Student("owen", 19, 2.5, "S1036", prerequisites=[])
student37 = Student("aubrey", 22, 3.9, "S1037", prerequisites=[])
student38 = Student("jackson", 20, 2.3, "S1038", prerequisites=[])
student39 = Student("zoey", 24, 1.8, "S1039", prerequisites=[])
student40 = Student("sebastian", 21, 3.2, "S1040", prerequisites=[])


# Register Courses
course1 = Course("CS101", "Introduction to Programming", 20)
course1 = Course("CS101", "Introduction to Programming", 20)
course2 = Course("MATH201", "Calculus I", 25)
course3 = Course("ENG101", "English Composition", 30)
course4 = Course("PHY301", "Physics Fundamentals", 22)
course5 = Course("BIO110", "Biology Basics", 28)
course6 = Course("CHEM201", "General Chemistry", 24)
course7 = Course("HIST101", "World History", 35)
course8 = Course("PSY150", "Introduction to Psychology", 32)
course9 = Course("ART120", "Art Appreciation", 18)
course10 = Course("ECON201", "Microeconomics", 26)
course11 = Course("BUS101", "Business Principles", 29)
course12 = Course("CS201", "Data Structures", 20)
course13 = Course("MATH202", "Calculus II", 23)
course14 = Course("ENG201", "Advanced Writing", 27)
course15 = Course("PHY302", "Modern Physics", 21)
# prerequisites courses
cs301 = Course("CS301", "Advanced Algorithms", 30, ["CS201", "CS101"])
cs201 = Course("CS201", "Data Structures", 40, ["CS101"])
cs101 = Course("CS101", "Intro to Programming", 100, [])


students_db = {}
courses_db = {}

def add_student(name, age, gpa,student_id):
    
    if student_id in students_db:
        return f"Error: Student {student_id} already exist"
    new_student = Student(name, age, gpa, student_id)

    students_db[student_id] = new_student
    return f"student {name} added sucessfully"

def remove_student(student_id):
    if student_id not in students_db:
        return f"Error: Student {student_id} not found"
    

    del students_db[student_id]
    return f"Student {student_id} removed successfully"

def add_course(course_code, course_name, capacity):
    if course_code in courses_db:
       return f"Error: course {course_code} already exists" 
       
    new_course = Course(course_code, course_name, capacity)
    courses_db[course_code] = new_course
    return f"Course {course_name} added successfully"

def remove_course(course_code):
    if course_code not in courses_db:
        return f"Error: Course {course_code} not found"
    
    del courses_db[course_code]
    return f"Course {course_code} removed successfully"

def find_student(student_id):
     if student_id in students_db:
         return students_db [student_id]
     else:
          return None
     
def find_course(course_code):
    if course_code in courses_db:
        return courses_db[course_code]  
    else:
        return None
    
def search_courses_by_name(keyword) :
    results = []
    keyword_lower = keyword.lower()
    
    for course in courses_db.values():
        if keyword_lower in course.course_name.lower():
            results.append(course)
    return results

def get_available_course():
    availble = []

    for course in courses_db.values():
        if len(course.enrolled_students) < course.capacity:
            availble.append(course)

    return availble

def get_full_courses():
  
    full = []
    
    for course in courses_db.values():
        if len(course.enrolled_students) >= course.capacity:
            full.append(course)
    
    return full

def get_most_popular_courses(limit = 10):
    if not courses_db or limit <= 0:
        return[]
    
    min_heap = []
    for course in courses_db.values():
        if course.capacity > 0:
            enrollment_ratio = len(course.enrolled_students) / course.capacity
        else:
            enrollment_ratio = 0
        if len(min_heap) < limit:
            heapq.heappush(min_heap, (enrollment_ratio, course))
        elif enrollment_ratio > min_heap[0][0]:
            heapq.heapreplace(min_heap, (enrollment_ratio, course))
    sorted_courses = [course for ratio, course in sorted(min_heap, reverse=True)]
    return sorted_courses

def get_courses_by_availability_status():
 
    status = {
        'available': [],
        'full': [],
        'empty': []
    }
    
    for course in courses_db.values():
        enrolled_count = len(course.enrolled_students)
        
        if enrolled_count == 0:
            status['empty'].append(course)
        elif enrolled_count >= course.capacity:
            status['full'].append(course)
        else:
            status['available'].append(course)
    
    return status

def get_available_courses():
 status = {
        'available': [],
        'full': [],
        'empty': []
    }
 for course in courses_db.values():
    enrolled_count = len(course.enrolled_students)

    if enrolled_count == 0:
       status['empty'].append(course)
    elif enrolled_count >= course.capacity:
        status['full'].append(course)
    else:
        status['available'].append(course)
 return status

def enroll_student(student_id, course_code):
    student = find_student(student_id)
    course = find_course(course_code)

    if not student:
        return f"Error: Student{student_id} not found"
    if not course:
        return f"Error: Course{course_code} not found"

    if course in student.registered_courses:
        return f"Error: Student already enrolled in {course_code}"
    if len(course.enrolled_students) >= course.capacity:
        return f"Error: Course {course_code} is full"
    
    course.enrolled_students.append(student)
    student.registered_courses.append(course)
    return f"Student {student_id} sucessfully enrolled in {course_code}"

def drop_course(student_id, course_code):
    student = find_student(student_id)
    course = find_course(course_code)

    if not student:
        return f"Error: Student {student_id} not found"
    if not course:
        return f"Error: Course {course_code} not found"
    if course not in student.registered_courses:
        return f"Error: Student not enrolled in {course_code}"
      
    course.enrolled_students.remove(student)
    student.registered_courses.remove(course)
    
    return f"Student {student_id} successfully dropped from {course_code}"

def get_student_schedule(student_id):

    student = find_student(student_id)
    if not student:
        return f"Error: Student {student_id} not found"
    
    return student.registered_courses



def get_course_roster(course_code):

    course = find_course(course_code)
    if not course:
        return f"Error: Course {course_code} not found"
    
    return course.enrolled_students

def valid_student(student_id, course_code):

    student = find_student(student_id)
    course = find_course(course_code)
    
    if not student or not course:
        return "Error: Invalid student or course"

    MAX_COURSES = 6
    if len(student.registered_courses) >= MAX_COURSES:
        return f"Error: Student already registered for {MAX_COURSES} courses (maximum)"
   
    return enroll_student(student_id, course_code)

def test_search_functions():
 
    add_student("Jane Smith", 22, 3.9, "S1002")
    add_student("John Doe", 20, 3.8, "S1001")
    add_course("MATH201", "Calculus I", 25)
    add_course("CS101", "Introduction to Programming", 30)
    add_course("PHY301", "Physics Fundamentals", 20)
    print("Students in database:", list(students_db.keys()))
    print("Courses in database:", list(courses_db.keys()))

    
   
    print("Find student S1001:", find_student("S1001").name)
    print("Find course CS101:", find_course("CS101").course_name)
    
    print("Search 'programming':", [c.course_name for c in search_courses_by_name("programming")])
    print("Available courses:", [c.course_code for c in get_available_course()])
    
 
    status = get_courses_by_availability_status()
    print("Empty courses:", len(status['empty']))
    print("Available courses:", len(status['available']))
    print("Full courses:", len(status['full']))
    
  
    popular = get_most_popular_courses(3)
    print("Most popular courses:", [c.course_code for c in popular])


    
test_search_functions()



def check_prerequisites(student, course):
    """
    Check if student has completed all prerequisites for a course
    Returns: (can_enroll, missing_prerequisites)
    """
    missing = []
    
    for prereq_code in course.prerequisites:
        if not student.has_completed(prereq_code):
            missing.append(prereq_code)
    
    return len(missing) == 0, missing

student = find_student("S1001")
course = find_course("CS301")
print(f"Course object: {course}")
print(f"Course type: {type(course)}")

can_enroll = False  
missing = []

if course is None:
    print("ERROR: Course is None! Check how you're getting the course object.")
  
else:

    can_enroll, missing = check_prerequisites(student, course)

if not can_enroll:
    print(f"Cannot enroll. Missing: {', '.join(missing)}")







    def check_prerequisites_graph(student, course, course_graph):

     def dfs(current_course_code, visited):
        if current_course_code in visited:
            return True  
        visited.add(current_course_code)
     
        if current_course_code not in course_graph:
            return True
        
        for prereq in course_graph[current_course_code]:
            if not student.has_completed(prereq):
               
                if not dfs(prereq, visited):
                    return False
        
        return True
    
     return dfs(course.course_code, set())

course_graph = {
    "CS301": ["CS201", "CS101"],
    "CS201": ["CS101"],
    "CS101": []
}