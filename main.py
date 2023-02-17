def main():
	# Display the intro screen
	intro()
	# Get the number of miles.
	steps_needed = float(input('Enter the number of steps: '))
	# Convert the miles to kilometers.
	steps_to_kilometers(miles_needed)

# The intro function displays an Introductory screen.
def intro():
	print('This program converts measurements')
	print('in steps to kilometers. For your')
	print('references the formula is:')
	print(' 1 miles = 1.609344 kilometers')
	print()

# The miles_to_kilometers function accepts a number of
# miles and displays the equivalent number of kilometers.
def steps_to_kilometers(miles):
	kilometers = miles * 1.609344
	print('That converts to', kilometers, 'kilometers.')

# Call the main function
main()