from PyQt5.QtWidgets import *
from PyQt5 import uic
import datetime
from datetime import timedelta


def assign_new_date(new_date) -> str:
    """ Creates new correct date for football list"""

    current_date = datetime.datetime.today()
    d= datetime.datetime.now()
    correct_date = datetime.datetime.today()

    for i in range(8):
        if current_date.strftime("%a") == "Wed":
            print("The dates today")
            break
        else:
            dt = timedelta(days=i)

            correct_date = dt + d
            if correct_date.strftime("%a") == "Wed":
                # print("new date has been found")
                break
    correct_date = correct_date.strftime("%a %dth %b")
    new_date = f"{correct_date} - Goals Eltham 8:45 MEET SO WE CAN START EARLY"
    return new_date


def create_player_list(football_list: list, week_count: int) -> list:
    """ Create a list/string showing the new football list

    creates a new football list based on the number of people playing
    and a sorted list in alphabetical order

    :param football_list: The football lsit as a string
    :param week_count: The number of players for that week
    :return: new football list to print
    """
    # String of new football list
    new_football_list = []
    # List to hold all players
    list_of_all_players = []
    # list to hold the playing players according to weekly amount
    list_playing_players = []
    # list to hold the players that aren't playing but are in reserve
    list_of_reserve_players = []
    reserve_player_count = 0

    # First find all the players and add them to a list
    for item in football_list:
        if "." in item:
            player = ""
            for char in item:
                if char.isalpha():
                    player += char
            if player == "":
                continue
            else:
                list_of_all_players.append(player)

    # Add the number of this week's players to a list
    for player in list_of_all_players:
        # Check how many players are playing and add them to a list
        if len(list_playing_players) < week_count:
            list_playing_players.append(player)
    # sort the list alphabetically so its easier organised
    list_playing_players = sorted(list_playing_players)

    # check if there were players that weren't added to the playing list
    # and add to reserve
    if list_of_all_players > list_playing_players:
        # value to store how many reserve players there are
        reserve_player_count = len(list_of_all_players) - len(list_playing_players)

        if reserve_player_count > 0:
            # add the rest of the players to the reserve list
            # by iterating backwards up to the difference of the number of reserve players
            list_of_reserve_players.extend(list_of_all_players[:-reserve_player_count-1:-1])
            # sort the list to make it more readable
            # list_of_reserve_players = sorted(list_of_reserve_players)

    # create a new list with the football list details

    # if football list is empty add items to empty list
    if len(new_football_list) <= 0:
        new_football_list.append(assign_new_date(football_list[0]))
        new_football_list.append("")
        for index, player in enumerate(list_playing_players):
            new_football_list.append(f"{index+1}. {player}")
        # add the reserve Player dividers
        new_football_list.append("————————————————")
        new_football_list.append("Reserves")
        # check if there are Reserve players
        if reserve_player_count > 0:
            # Then add the reserve players
            for index, reserve_player in enumerate(list_of_reserve_players):
                new_football_list.append(f"{index+1}. {reserve_player}")
        else:
            for i in range(3):
                new_football_list.append(f"{i+1}. ")

    return new_football_list


class MYGUI(QMainWindow):
    def __init__(self):
        super(MYGUI, self).__init__()
        uic.loadUi("Football.ui", self)
        self.show()
        # when modify button is clicked call modify method
        self.list_modify_button.clicked.connect(self.modify)

    def modify(self):
        if self.football_list_edit.toPlainText() == "":
            message = QMessageBox()
            message.setText("Editor is Empty")
            message.exec_()
        # if statements for each combobox
        elif self.number_of_players_comboBox.currentText() == "":
            message = QMessageBox()
            message.setText("Please Select Number of Players")
            message.exec_()
        else:
            # create a list containing each new line from edit box
            current_football_list = self.football_list_edit.toPlainText().split("\n")
            # Create a new football list string using the function
            new_football_list = create_player_list(current_football_list,int(self.number_of_players_comboBox.currentText()))
            # Create a new string since textBrowser only passes strings
            new_message = "\n".join(new_football_list)
            self.football_list_textBrowser.setText(new_message)


def main():
    app = QApplication([])
    window = MYGUI()
    app.exec_()


if __name__ == '__main__':
    main()