
MI = {'Rohit':12, 'QDcock':10.5, 'Kishan':10, 'Surya':10,'Hardik':9,'Pollard':9,'Bumrah':10,'Bolt':10,'Pandya':8,'Jayant':7,'Coulter-Nile':9}
CSK = {'Faf-du':11, 'Gaikwad':12, 'Raina':9, 'Dhoni':9.5,'Jadeja':9,'Deepak':9,'Rayadu':9,'Moeen Ali':8.5,'Sam Curren':8.5,'Shardul':8,'Lungi':9.5}

Combo=MI|CSK
print(Combo)

Players = Combo.items()
print(Players)
for Play in Players:
    # if Play in Combo:
    print("shubham:",Play)



# myteam =[]
#
# for x in range(3):
#     y = input("Enter Player name:" )
#     if y in Combo:
#         myteam.append(y)
#
# L = len(myteam)
# print("The Team is:{}".format(L),myteam)









