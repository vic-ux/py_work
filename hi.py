name = 'Victor Omodewu'
age = 25 
height = 74
weight = 180
eyes = 'Brown'
teeth = "Yellow"
hair = "Brown"
# conversion of pound to kilogram
weight_in_kg = round(weight / 2.2)

#conversion of height to centimetre
height_in_cm =round(height * 2.54)


print (f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's {height_in_cm} centimetre tall.")
print(f"He's {weight_in_kg} kilogram heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height + weight
print (f"If I add {age}, {height}, and {weight} I get {total}.")
