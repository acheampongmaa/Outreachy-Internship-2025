#Learning Object Oriented Programming
''' Object-Oriented Programming is a way of writing code by creating objects that represent real-world things.
Instead of writing everything as just instructions, we group related data and behaviors into things called classes and objects.'''

#Example 1
#Creating a Car class

# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#         self.speed = 0    #starts at zero. 

#     def start(self):
#         print(f"{self.color} {self.brand} started.")

#     def accelarate(self):
#         self.speed += 10  #increase the speed of car by 10
#         print(f"{self.color} {self.brand} is moving at {self.speed} km/h.")    

#     def stop(self):
#         self.speed = 0
#         print(f"{self.color} {self.brand} stopped.")    

# #creating an object
# my_car=Car("Toyota", "Blue")    
# my_car.start()
# my_car.accelarate()
# my_car.stop ()   


#Example 2
#The Book class

class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def is_modern(self):
        return self.year >= 2000 
    
    def summary(self):
        return f" '{self.title}' by {self.author} published in {self.year}."
    
    def is_written_by(self, author_name):
        return self.author.lower() == author_name.lower()
    
    def age(self, current_year):
        return current_year - self.year
    
    def recommend(self):
        print(f"If you enjoy good reads try '{self.title}' by {self.author}!")

    def update_year(self, new_year):
        self.year = new_year

#creating object

my_book = Book("Eat that Frog", "Brain Tracy", 2001, "self help book")            
print(my_book.is_modern())
print(my_book.is_written_by("Brain Tracy"))
print(my_book.age(2025))
my_book.recommend()
print(my_book.summary())
my_book.update_year(2025)
print(my_book.year)