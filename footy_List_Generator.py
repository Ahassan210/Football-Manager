import datetime
def first_instance_finder(find: list)-> int:
    """
    Find the first instance in a loop where there's a player
    :return: return the index position
    """
    for index, item in enumerate(find):
        for char in item:
            if char == ".":
                first_instance = index
                return first_instance



#List to store this weeks current list
current_footbal_list = []
#List to store last weeks football list
old_fotball_list = []
    #A list with JUST the names of Players
names_of_Players = []
#A variable to store the index of the first player in the list
first_instance_index = None
#variable for player names
player_name_only=""


#While loop to read all lines of input, Break manually when done
while True:
    #Exception handling to try Read All Lines
    try:


        #Prompt User to copy and paste the last list in
        prompt = input("Paste the Last list in here, Ctrl Z/D to finish: ")
        if prompt =="":
            break
    #Break when Ctrl Z or D is used
    except EOFError:
        break
    #Add each line to our current football list
    old_fotball_list.append(prompt)

#call funtion to find index position and store in our variable
first_instance_index = first_instance_finder(old_fotball_list)
# print(first_instance_index)
#remove everything other than players from the list
old_fotball_list = old_fotball_list[first_instance_index:]


# A loop to store each player in the names of players list
# print(old_fotball_list)
for player in old_fotball_list:
    #check every item in the list(every player)
    if "-" in player:
        names_of_Players.append(player)
        continue
    elif player =="Reserves":
        names_of_Players.append(player)
    else:
        for char in player:
            #only add the name remove the rest
            if char.isalpha():
                player_name_only+=char
        #add to a new list of just player names
        names_of_Players.append(player_name_only)
        #reset player name to store next player's name
        player_name_only=""

#set current football list [0] to todays date and football details
D = datetime.datetime.now()
D = D.strftime("%A %dth %B")
if current_footbal_list ==[]:
    current_footbal_list.append([f"{D} - Goals Eltham 8:45 MEET SO "
                             f"WE CAN START EARLY"])
    current_footbal_list.append([""])

#Create indexer for reserves
reserves = 0
#Loop to add players and their number to current list after
for index, player in enumerate(names_of_Players):
    if index<=11:
        current_footbal_list.append([index+1, player])
    elif "-" in player:
        current_footbal_list.append(player)
    elif player.casefold() == "reserves":
        current_footbal_list.append(player)
    else:
        current_footbal_list.append([reserves, player])
        reserves+=1



#printing football list
#beggining message
print()
for item in current_footbal_list[:2]:
    #remove from list into string using .join method
    print("".join(item))

for value in current_footbal_list[2:]:
    if "." in value[1]:
        num, name = value
        print(f"{num}. {name}")
    elif "-" in value:
        name = value[0]
        print(name)







