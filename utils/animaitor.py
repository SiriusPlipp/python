#import animation library
import matplotlib.pyplot as plt
import numpy as np
import time

class Person:
    def __init__(self, vorname, nachname, bday):
        self.vorname = vorname
        self.nachname = nachname
        self.bday = bday
        self.age = 0
        self.height = 0
        self.weight = 0
        self.gender = "male"
        self.nationality = "German"
        self.occupation = "Unemployed"
        self.education = "None"
        self.marital_status = "Single"
        self.children = 0
        self.pets = 0

    def __str__(self):
        return f"{self.vorname} {self.nachname} geboren am: {self.bday}"
    
    def __repr__(self):
        return self.__str__()



def animate(person):
    """Animates a person's life"""
    fig, ax = plt.subplots()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')
    ax.set_title(person.name)
    ax.set_xlabel('Age')
    ax.set_ylabel('Height')
    plt.show()



animate(Person("John", "Doe", "1990-01-01"))