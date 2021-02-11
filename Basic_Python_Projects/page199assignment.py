# INHERITANCE ASSIGNMENT (Page 199)
"""
Create two classes that inherit from
    another class.
Each child should have at least two of
    their own attributes.
Add comments throughout your Python
    explaining your code.
Upload your code to Github and submit
    your link below.
"""

# Parent class
class book:
    # attributes
    name = 'Book Title'
    author = 'Lastname, Firstname'
    publisher = 'XYZ Publishing House'
    pages = '333'
    yearPublished = '1979'
# Child class 1
class nonFiction(book):
    # attributes
    refType = 'dictionary' # cant use 'type' as a variable
    subject = 'definitions'

class fiction(book):
    # attributes
    form = 'classic lit'
    characters = 'Raskolnikov'
