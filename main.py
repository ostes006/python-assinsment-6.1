def main():
	# Display the intro screen
	intro()
	# Get the number of miles.
	steps_needed = float(input('Enter the number of steps: '))
	# Convert the miles to kilometers.
	steps_to_feet (steps_needed)

# The intro function displays an Introductory screen.
def intro():
	print('This program converts measurements')
	print('in steps to feet. For your')
	print('references the formula is:')
	print(' 1 steps = 1.609344 feet')
	print()

# The miles_to_kilometers function accepts a number of
# miles and displays the equivalent number of kilometers.
def steps_to_feet(steps):
	feet = steps * 1.609344
	print('That converts to', feet, 'feet.')

# Call the main function
main()