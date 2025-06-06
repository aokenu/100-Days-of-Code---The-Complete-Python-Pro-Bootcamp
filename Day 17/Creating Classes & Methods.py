# """First Practice"""
# from appdirs import user_state_dir
#
#
# class Car:
#     def __init__(self, car_brand, car_color):
#         self.brand = car_brand
#         self.color = car_color
#
#     def drive(self):
#         print(f" I am driving a {self.color} {self.brand}")
#
#
# car1 = Car("Toyota Camry", "Grey")
# car2 = Car("Tesla", "Black")
#
# car1.drive()
# car2.drive()
#
#
# """Second Practice"""
# class Student():
#     def __init__(self, student_name, student_grade):
#         self.name = student_name
#         self.grade = student_grade
#
#     def show_info(self):
#         print(f"{self.name}, {self.grade}")
#
#
# student1 = Student("Fred", 78)
# student2 = Student("Chuks", 93)
#
# students = [
#     Student("Fred", 78),
#     Student("Chuks", 93),
#     Student("Ada", 85)
# ]
#
# for student in students:
#     student.show_info()



"""Example Practice"""
class User:

    def __init__(self, user_id, username ):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1
        print(f"{self.followers}")
        print(f"{self.following}")
        print(f"{user.followers}")
        print(f"{user.following}")

user1 = User("102", "Manroe")
user2 = User("103", "Chukie")

user1.follow(user2)
