
class Student:
  def __init__(self, name, age, gpa, student_id,):
      self.name = name 
      self.age = age
      self.gpa = gpa
      self.student_id = student_id
      self.registered_class = []
      self.completed_class = []

student1 = Student("favour", 21, 4.0, "af22304710")
student2 = Student("eunice", 20, 3.9, "eu22304710")
student3 = Student("crispine", 20, 3.8,"cr22304710")
student4 = Student("chima", 25, 3.5, "ch22304710")
student5 = Student("alex", 18, 2.0, "al22304710")
student6 = Student("jay", 26, 2.1, "jy22304710")
student7 = Student("tom", 17, 3.2, "tm22304710")
student8 = Student("bradley", 31, 1.1, "ba22304710")
student9 = Student("vicky", 22, 2.9, "vy22304710")
student10 = Student("ewo", 26, 3.3, "eo22304710")
student11 = Student("benjamin", 21, 3.1, "af22304720")
student12 = Student("mia", 22, 3.9, "af22304721")
student13 = Student("lucas", 20, 3.3, "af22304722")
student14 = Student("charlotte", 23, 3.7, "af22304723")
student15 = Student("henry", 19, 3.5, "af22304724")
student16 = Student("amelia", 21, 4.0, "af22304725")
student17 = Student("alexander", 22, 3.6, "af22304726")
student18 = Student("harper", 20, 3.1, "af22304727")
student19 = Student("daniel", 24, 3.2, "af22304728")
student20 = Student("evelyn", 19, 3.9, "af22304729")
student21 = Student("michael", 21, 3.4, "af22304730")
student22 = Student("ethan", 22, 3.7, "af22304731")
student23 = Student("abigail", 20, 2.9, "af22304732")
student24 = Student("matthew", 21, 3.3, "af22304733")
student25 = Student("ella", 23, 3.8, "af22304734")
student26 = Student("samuel", 19, 3.5, "af22304735")
student27 = Student("scarlett", 22, 4.0, "af22304736")
student28 = Student("david", 20, 3.6, "af22304737")
student29 = Student("grace", 24, 3.7, "af22304738")
student30 = Student("joseph", 21, 2.2, "af22304739")
student31 = Student("chloe", 19, 3.9, "af22304740")
student32 = Student("carter", 22, 3.4, "af22304741")
student33 = Student("victoria", 20, 3.8, "af22304742")
student34 = Student("john", 23, 1.1, "af22304743")
student35 = Student("riley", 21, 3.7, "af22304744")
student36 = Student("owen", 19, 2.5, "af22304745")
student37 = Student("aubrey", 22, 3.9, "af22304746")
student38 = Student("jackson", 20, 2.3, "af22304747")
student39 = Student("zoey", 24, 1.8, "af22304748")
student40 = Student("sebastian", 21, 3.2, "af22304749")

class Course:
   def __init__(self, course_code, course_name, capacity):
          self.course_code = course_code
          self.course_name = course_name
          self.capacity = capacity
          self.enrolled_students = []

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

print(add_student("John Doe", 20, 3.8, "S1001" ))
print(add_student("Jane Smith", 22, 3.9, "S1002",))

print(add_course("CS101", "Introduction to Programming", 30))
print(add_course("MATH201", "Calculus I", 25))

# Verify they're in databases
print("Students in database:", list(students_db.keys()))
print("Courses in database:", list(courses_db.keys()))

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
print("Search 'programming':", [c.course_name for c in search_courses_by_name("programming")])


def get_availble_course():
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

import heapq

def get_most_popular_course(limit = 10):
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