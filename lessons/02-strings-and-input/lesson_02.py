# Lesson 2 exercise.

# Part 1: Tidying text
# Leave this line as it is. The tests change the text to check your code.
raw_name = "   tOM sMITH   "

# Create clean_name, shout, name_length and greeting, then print greeting.

clean_name =(raw_name.strip().title())
shout =(raw_name.strip().upper())
name_length =(len(clean_name))
greeting =(f"Hello, {clean_name}!")

print (greeting)

# Part 2: Tip calculator
# Ask "Bill amount: " and "Tip percent: ", then print the tip and total.

bill = float(input("Bill amount?"))
tip_percent = float(input("Tip percent?"))
tip =((bill * tip_percent)/100)
total = (bill + tip)
print (f"Bill amount: {bill}")
print (f"Tip percent: {tip_percent}")
print (f"Tip: {tip:.2f}")
print (f"Total: {total:.2f}")