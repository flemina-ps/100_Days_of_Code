print(
'''
        ___________
        \         /
         )_______(
         |"""""""|_.-._,.---------.,_.-._
         |       | | |               | | ''-.
         |       |_| |_             _| |_..-'
         |_______| '-' `'---------'` '-'
         )"""""""(
        |_________|
        `'-------'`
       .-------------.
      /_______________\ 
'''
)



def find_Highest_Bidder(bidding_dictionary):
        winner=""
        highest_bid=0

        max(bidding_dictionary)

        for bidder in bidding_dictionary:
            bid_amount=bidding_dictionary[bidder]
            if bid_amount>highest_bid:
                highest_bid=bid_amount
                winner=bidder
        print(f"The winner is {winner} with a bid of ${highest_bid}")

bids={}
continue_bidding=True
while continue_bidding:
    name=input("What is your name: ")
    price=int(input("What is your bid: $"))
    bids[name]=price
    should_continue=input("Are there any other bidders? Type 'yes' or 'no': \n").lower()

    if should_continue=='no':
        continue_bidding=False
        find_Highest_Bidder(bids)
    elif should_continue=="yes":
        print("\n" *100)




