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

bill = float(input("How much is the bill?"))
tip_percent = int(input("How much would you like to tip?"))
print ("Bill amount:", "$",bill)
print ("Tip percent:", tip_percent,"%")
print ("Tip: ",(bill * tip_percent)/100)
print ("Total: ", (bill + (bill * tip_percent)/10))
#alt: 
tip =((bill * tip_percent)/100)
total = (bill + tip)
print ("Bill amount:", "$",bill)
print ("Tip percent:", tip_percent,"%")
print ("Tip:", tip)
print ("Total:", total)