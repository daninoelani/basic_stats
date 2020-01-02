# Author: Dani Sadorf
# Date: 6 Jan 2020
# Description: Creates a class called Person with name and age. Builds a function to take a list of person objects as the parameter and return
#   the mean, median and mode of the ages. Returns basic stats as a tuple in the specified order.

import statistics


class Person:
    '''This class creates a person with name and age'''

    # Must initialize the class with name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age


def basic_stats(people):
    '''Accepts a list of people built using the Person object and returns the mean, median and mode of their ages'''
    # Create a list of all the ages
    ages = [Person.age for Person in people]

    # Create variables for each stat for easy readability
    people_mean = statistics.mean(ages)
    people_median = statistics.median(ages)
    people_mode = statistics.mode(ages)

    # Return a tuple of basic statistics
    return (people_mean, people_median, people_mode)
