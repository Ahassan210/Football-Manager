

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


def football_list_numbers_sorter(container: list)-> list:
    """
    Sort the list by alphabetical order and rearrange the numbers
    :param container: list to be sorted
    :return: sorted list with correct numbers including reserves
    """
    #variable to store just the names withoutr eserves
    number_of_players = 0
    list_of_names= []
    #variable to store list of reserves
    list_of_reserves= []
    #the list we'll return once evetyhign has ben sorted correctly
    list_to_return = []
    # the variable to count the number of players up to twelve,
    # so we can know when to add the rest to reserves
    player_number_counter = 0
    #inner scope variable to store the index of the first player using
    #the player finding function
    player_location = first_instance_finder(container)
    #variable for finding reserve players
    reserves_player_location = 0
    for index, item in enumerate(container):
        #While we haven't reached the players add to our list to return
        if index<player_location:
            list_to_return.append(item)
            continue
        #once we've reached the players start storing them in a list
        #break when we've added the main players
        if index >= player_location and player_number_counter<12:
            for location, player in enumerate(item):
            #if we've added all the main players come out the loop
                if player == ".":
                    item = item[location+1:]
                    list_of_names.append(item)
                    player_number_counter+=1
                    #sort the list of names then reassessing the correct number
                    list_of_names = sorted(list_of_names)
            continue
        #keep adding to the list before reserve players
        for number_of_players, each_player in enumerate(list_of_names):
            currnt_player = str((number_of_players)+1) + "." + each_player
            list_to_return.append(currnt_player)
            #find the location of first reserves player and iterte backwards to get the names
        reserves_player_location = first_instance_finder(container[index:]) + index
        #add the reserves to a list
        for item in (container[reserves_player_location:]):
            list_of_reserves.append(item)
        #sort the names of the reserves
        list_of_reserves = sorted(list_of_reserves)
        #reassign the correct number and add to final list

        #Error To be fixed(#SCRAPPED)
        for index, item in enumerate(list_of_reserves):
            item = str(index+1) + "." + item
            list_to_return.append(item)

        #return the final modded list
        return list_to_return







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
lines_counter = 0


#While loop to read all lines of input, Break manually when done
while lines_counter<20:
    #Exception handling to try Read All Lines
    try:


        #Prompt User to copy and paste the last list in
        prompt = input("Paste the Last list in here, Ctrl Z/D to finish: ")

    #Break when Ctrl Z or D is used
    except EOFError:
        break
    #Add each line to our current football list
    old_fotball_list.append(prompt)
    lines_counter+=1

#call function to sort the list players and numbers
new_football_list = football_list_numbers_sorter(old_fotball_list)


#Print Football List
for item in new_football_list:
    print(item)











