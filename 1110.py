class Course:
   def __init__(self, course_name, course_id, course_credits):
      self.couse_name = course_name
      self.couse_id = course_id
      self.couse_credits = course_credits


class Student:
   def __init__(self, stu_name, stu_id):
      self.stu_name = stu_name
      self.stu_id = stu_id

   def _str_(self):
         return f"Name: {self.stu_name}\nID = {self.stu_id}"
   def addCourse(self, course_info):
      self.course_info = course_info

c1 = Course(course_name="套裝軟體應用", course_id="G0D17M01", course_credits=3)

s1



class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

      def _str_(self):
         return f"Name: {self.name}\nAge = {self.age}"
      
p1 = Person("John", 36)
print(p1)

p2 = Person("Sue", 21)
print(p2.__dict__)

