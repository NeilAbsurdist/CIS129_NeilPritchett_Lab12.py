# Neil Pritchett
# CIS129 - Introduction to Programming
# Lab 12: Object-Oriented Programming - Create a Pet Class
# Date: May 16, 2025
# Description:
# This program defines a Pet class with private fields for name, type, and age.
# It includes mutator and accessor methods for each field.
# The main program creates a Pet object, gets input from the user,
# stores it using mutators, then displays the data using accessors.

class Pet:
    def __init__(self, name="", pet_type="", age=0):
        self.__name = name
        self.__type = pet_type
        self.__age = age

    def setName(self, name):
        self.__name = name

    def setType(self, pet_type):
        self.__type = pet_type

    def setAge(self, age):
        self.__age = age

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def getAge(self):
        return self.__age


def main():
    # Create Pet object
    animal = Pet()

    # Get input from user
    input_name = input("Enter a pet name: ")
    animal.setName(input_name)

    input_type = input("Enter a pet type: ")
    animal.setType(input_type)

    input_age = int(input("Enter a pet age: "))
    animal.setAge(input_age)

    # Output the pet's data
    print("\nThe pet name is", animal.getName())
    print("The pet type is", animal.getType())
    print("The pet age is", animal.getAge())


if __name__ == "__main__":
    main()