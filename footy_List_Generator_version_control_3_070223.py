import datetime
from datetime import timedelta
# a function to find where the category seperator for reserve players
#starts, that way the first player for the reserves list can be found
def find_reserve_players_category(football_list: list) -> int:
    """find where the reserve players category starts"""

    for index, value in enumerate(football_list):
        if "—" in value:
            return index


#use the funtion above to find the first reserve player
def find_first_reserve_player(football_list: list) -> int:
    """find where the index of the actual first reserve player"""
    reserve_category_start = \
        find_reserve_players_category(football_list)
    for index, value in enumerate(football_list[reserve_category_start:]):
        if "." in value:
            return index


#use this to find where the first category ends and second
# category starts
def first_instance_finder(football_list: list)-> int:
    """
    Find the first instance in a loop where there's a player
    :return: return the index position
    """
    for index, value in enumerate(football_list):
        for char in value:
            if char == ".":
                first_instance = index
                return first_instance





def football_list_categoriser(football_list: list)->list:
    """
    Categorise the list into welcome message, football players and
    reserve players

    :param football_list:
    :return: list containing three lists: welcome message,
    football players and reserves
    """
    first_catrgory = first_instance_finder(football_list)-1
    second_category = first_catrgory+1
    third_category = find_reserve_players_category(football_list)
    first_category_list = []
    second_category_list=[]
    third_category_list = []
    categorised_list = []
    #add all the first category items to a list
    for item in football_list[:first_catrgory+1]:
        first_category_list.append(item)
    #add all the second category items to a list

    for item in football_list[second_category:third_category]:
        second_category_list.append(item)

    #add all the third category items to a list
    for item in football_list[third_category:]:
        third_category_list.append(item)

    categorised_list.append(first_category_list)
    categorised_list.append(second_category_list)
    categorised_list.append(third_category_list)

    return categorised_list



def Assign_new_date(new_date)->str:
    """ Creates new correct date for football list"""

    current_date = datetime.datetime.today()
    D= datetime.datetime.now()
    correct_date = datetime.datetime

    for i in range(8):
        if current_date.strftime("%a") == "Wed":
            break
        else:
            dt = timedelta(days=i)

            correct_date = dt + D
            if correct_date.strftime("%a") == "Wed":
                break
    correct_date = correct_date.strftime("%a %dth %b")
    new_date = f"{correct_date} - Goals Eltham 8:45 MEET SO WE CAN START EARLY"
    return new_date


def sort_players(players: list):
    """sorts the players and gives them the right number"""

    #figure out where the numbers are and remove them
    for location, player in enumerate(players):
        for index, char in enumerate(player):
            if char == ".":
                player = str(player[index+1:]).title().split()
                players[location] = "".join(player)


    #sort the players with the removed number
    players = sorted(players)
    #after sorting add the correct numbrer back again
    for index, item in enumerate(players):
        new_player = str(index+1) + "." + item
        players[index] = new_player
    #return this list of correct nubmer and names
    return players


def create_new_list(football_list: list)-> list:
    """
    create a new list by adding the right values to the old list
    :param football_list:
    :return: correct list with correct date and sorted names
    """
    #loop to edit the three categories of lists
    for index, item in enumerate(football_list):
        #for the first category get the correct Date
        if index == 0:
            item[0] = Assign_new_date(item[0])
        #for the second category rearrange and sort the names correctly
        elif index == 1:
            football_list[index] = sort_players(item)
        #for the reserve category do the same(sorting player names and numbers
        elif index == 2:
            for index, value in enumerate(item):
                if index>1:
                    sort_players(item[index:])
    #add this all into a new list not as three different lists but as 1
    organised_list= []
    for item in football_list:
        organised_list.extend(item)
    #return the oragnised new list
    return organised_list



#List to store this weeks current list
current_football_list = []
#List to store last weeks football list
old_football_list = []
#for debugging
lines_counter = 0


#While loop to read all lines of input, Break manually when done
while True:
    #Exception handling to try Read All Lines
    try:


        #Prompt User to copy and paste the last list in
        prompt = input("Paste the Last list in here, Ctrl Z/D to finish: ")

    #Break when Ctrl Z or D is used
    except EOFError:
        break
    #Add each line to our current football list
    old_football_list.append(prompt)
    # lines_counter+=1


#categorise the old football lsit using previous functions and return it
current_football_list = football_list_categoriser(old_football_list)
#use the createlist function to work on the three categories and return
#as one list
new_football_list = create_new_list(current_football_list)

for item in new_football_list:
    print(item)







