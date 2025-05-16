#Task 1 - Working with Lists

fruits = ['mango', 'banana', 'apple', 'kiwi', 'grape']
print("Original list:", fruits)

fruits.append('orange')
print("After adding a fruit:", fruits)

fruits.remove('mango')
print("After removing a fruit:", fruits)

print("Reversed list:", fruits[::-1])

#Task 2 - Exploring Dictionaries

my_info = {
    "name": "Nyrah",
    "age": 22,
    "city": "San Diego"
}

my_info["favorite color"] = "Purple"

# Update the city
my_info["city"] = "San Diego"

# Print all keys and values
print("Keys:", ', '.join(my_info.keys()))
print("Values:", ', '.join(str(value) for value in my_info.values()))

#Task 3 - Using Tuples

favorite_movies = ('Interstellar', 'Dune 2', 'To Kill a Mockingbird')
print("Favorite things:", favorite_movies)

print("Oops! Tuples cannot be changed.")
print("Length of tuple:", len(favorite_movies))
