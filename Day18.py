import os
#exercise
student_data = [
     {
        'Math': 85,
        'English': 90,
        'Science': 88
    },
    {
        'Math': 92,
        'English': 85,
        'Science': 89
    }
]

def new_dict(Math,English,science):
    new_dict = {

    }
    new_dict["Math"]=Math
    new_dict["English"]=English
    new_dict["science"]=science

    student_data.append(new_dict)


new_dict(90,87,85)
print(student_data)

#Excersice 2

def find_winner(bidderdetails):
    highest_bid = 0
    winner = " "
    for bidder in bidderdetails:
        bid_value = bidderdetails[bidder]
        if bid_value>highest_bid:
            highest_bid = bid_value
            winner = bidder
    print(f" the winner is {winner} with bidding price {highest_bid} (::)")        


no_bidder = False
while not no_bidder:
    Name = input("What is your name: ")
    Bid = int(input("What is your bid: "))
    bid_data = {}
    bid_data[Name]=Bid

    Any_Bid = input("Any one interested (Yes/No)")
    if Any_Bid == 'No':
        no_bidder = True
        find_winner(bid_data)
    else:
        os.system('clear')



