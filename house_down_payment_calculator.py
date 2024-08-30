
//QUESTION: If buyer have good credit score then he pay only 10% otherwise they have to pay 20% of the amount

price_of_house = 1000000
cr_score = int(input("Enter credit score: "))

if (cr_score < 300 or cr_score > 850):
    print("Invalid credit score. Please enter a score between 300 and 850.")
else:
    
    if (cr_score >=740):
        down_pymnt = (price_of_house * 0.10)
    else:
        down_pymnt = (price_of_house * 0.20)
    print(f"They need to pay ${down_pymnt} to book house")
