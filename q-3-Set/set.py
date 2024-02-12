'''
Title:
    Color Set Operations

Prerequisites:
    Basic understanding of Python syntax, particularly sets.

Objectives:

    Create a set of favorite colors and print it.
    Add a new color to the set and print the updated set.
    Remove a color from the set and print the updated set.
    Create a new set containing only colors that start with the letter "B" and print it.
    Use the len() function to find the number of colors in the set and print it.

'''


favorite_colors = {"Blue", "green", "purple", "orange", "Pink", "Violet", "brown", "black"}

print("My favorite colors are:", favorite_colors)

# Adding new color
favorite_colors.add("red")

print("Added new color:", favorite_colors)

#Removing color
favorite_colors.remove("green")

print("Removed a color:", favorite_colors)

# Create a new set with colors starting with "B"
colors_starting_with_b = {color for color in favorite_colors if color.lower().startswith("b")}

# Print the new set of colors starting with "B"
print("Colors starting with 'B':", colors_starting_with_b)

# Calculate the number of colors in the set
num_colors = len(favorite_colors)

# Print the number of colors in the set
print("Number of colors in the set:", num_colors)
