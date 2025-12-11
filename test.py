

'''def test_search_functions():
 
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
'''

def timsort(arr, key=None):

    if key is None:
        key = lambda x: x
    
    n = len(arr)
    
   
    MIN_MERGE = 32
    
    
    min_run = compute_min_run(n)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end, key)

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            
            if mid < right:
                merge(arr, left, mid, right, key)
        
        size = 2 * size
    
    return arr

def compute_min_run(n):

    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return n + r

def insertion_sort(arr, left, right, key):

    for i in range(left + 1, right + 1):
        j = i
        while j > left and key(arr[j]) < key(arr[j - 1]):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def merge(arr, left, mid, right, key):
   
    len1, len2 = mid - left + 1, right - mid
    left_arr, right_arr = [], []
    
   
    for i in range(len1):
        left_arr.append(arr[left + i])
    for i in range(len2):
        right_arr.append(arr[mid + 1 + i])
    
    
    i = j = 0
    k = left
    
    while i < len1 and j < len2:
        if key(left_arr[i]) <= key(right_arr[j]):
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len2:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def timsort_students_by_gpa(students, ascending=True):
  
    def gpa_key(student):
  
        if ascending:
            return student.gpa
        else:
            return -student.gpa
    
    return timsort(students, key=gpa_key)
class Student:
    def __init__(self, student_id, name, gpa):
        self.student_id = student_id
        self.name = name
        self.gpa = gpa
    
    def __repr__(self):
        return f"Student({self.name}, GPA: {self.gpa})"


students = [
    Student("S001", "Alice", 3.8),
    Student("S002", "Bob", 3.5),
    Student("S003", "Charlie", 3.9),
    Student("S004", "Diana", 3.7),
    Student("S005", "Eve", 3.6),
    Student("S006", "Frank", 3.4),
    Student("S007", "Grace", 3.9),  
    Student("S008", "Henry", 3.2),
    Student("S009", "Ivy", 3.8),   
    Student("S010", "Jack", 3.1)
]

print("Original order:")
for s in students:
    print(f"  {s.name}: {s.gpa}")

print("\nSorted by GPA (descending):")
sorted_students = timsort_students_by_gpa(students, ascending=False)
for s in sorted_students:
    print(f"  {s.name}: {s.gpa}")

print("\nSorted by GPA (ascending):")
sorted_students = timsort_students_by_gpa(students, ascending=True)
for s in sorted_students:
    print(f"  {s.name}: {s.gpa}")
