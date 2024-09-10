#printing 1+2+3+4+5+6+7+8+9+10

i = 1
result = ""

while i <= 10:
    result += str(i)  # Convert the integer to a string and append it to the result
    if i < 10:        # Add a '+' sign if it's not the last number
        result += "+"
    i += 1           # Increment the counter

print(result)