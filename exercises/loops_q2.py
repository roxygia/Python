#Q2) Use a for loop to format and print the following list:

mailing_list = [
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
["Biscuit", "biscuit@whippies.park"],
["Rory", "rory@whippies.park"],
]

for mail in mailing_list:
    print(f"{mail[0]}: {mail[1]}")
