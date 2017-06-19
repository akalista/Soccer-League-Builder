# Project 1: Build a Soccer League, EXTRA CREDIT included
# Author: Anton Kalista

'''
You have volunteered to be the Coordinator for your town’s youth soccer league.
As part of your job you need to divide the 18 children who have signed up for the league into three even teams
- Dragons, Sharks and Raptors. In years past, the teams have been unevenly matched, so this year you are doing your best
to fix that. For each child, you will have the following information: Name, height (in inches), whether or not they have
played soccer before, and their guardians’ names. You'll take a list of these children, divide them into teams and
output a text file listing the three teams and the players on them.
'''


# Import CSV
import csv

# Create lists and strings for teams
# Create lists for experienced and not experienced players
# Create count variable for loops

Sharks = [];  shark_str = ""
Dragons = []; dragon_str = ""
Raptors = []; raptor_str = ""
XP = []; NXP = []; count = 0


# EXTRA CREDIT LISTS for players, guardians, and more(count var)
players = []
guardians = []
more = 0


# Function to write into teams.txt
def writer(args):
    with open("teams.txt", "a") as file:
        file.write(args)
        file.write("\n")
        file.close()


# Reads soccer_players.csv and appends values to appropriate lists
def to_team(file):
    with open(file, newline='') as csvfile:
        team_reader = csv.DictReader(csvfile)
        # Loop through names, exp, and guardian names to append to lists
        for row in team_reader:
            if row['Soccer Experience'] == "YES":
                XP.append(row['Name'])
                XP.append(row['Soccer Experience'])
                XP.append(row['Guardian Name(s)'])
            elif row['Soccer Experience'] == "NO":
                NXP.append(row['Name'])
                NXP.append(row['Soccer Experience'])
                NXP.append(row['Guardian Name(s)'])


# EXTRA CREDIT WORK

# Open soccer_players.csv and append name and guardian name into lists
def to_letter(file):
    with open(file, newline='') as csvfile:
        team_reader = csv.DictReader(csvfile)
        # Loop through names and guardian names to append to lists
        for row in team_reader:
            players.append(row['Name'])
            guardians.append(row['Guardian Name(s)'])


# Write custom messages into custom file names depending on player names
def writer1(args, index):
    with open(args + ".txt", "a") as file:
        # Empty strings for use
        string = ""
        string1 = ""
        # If loop to find player team
        if players[index] in Sharks:
            string = "Sharks"
        elif players[index] in Dragons:
            string = "Dragons"
        elif players[index] in Raptors:
            string = "Raptors"
        # Custom string to write to file
        string1 = "Dear " + guardians[index] + ". " + players[index] + " will be" \
            " playing on team " + string + "!\n" + "The first practice is scheduled" \
            " for the 21st of October. See you there!"
        # Write string and close file
        file.write(string1)
        file.close()


# Function to flip name, last name and add _ in between
def name_flip(name_str):
    new_name = name_str.split(' ', 1)
    new_name1 = new_name[1].lower() + '_' + new_name[0].lower()
    return new_name1


# Main
if __name__ == '__main__':
    # Divide players by experience
    to_team('soccer_players.csv')

    # Use slices to move players evenly into teams
    Sharks = XP[:9] + NXP[:9]; XP[:9] = []; NXP[:9] = []
    Dragons = XP[:9] + NXP[:9]; XP[:9] = []; NXP[:9] = []
    Raptors = XP[:] + NXP[:]; XP = []; NXP = []

    # Use while loop to make lists into readable strings
    while count != 6:
        shark_str += ', '.join(Sharks[:3]) + '\n'
        Sharks[:3] = []
        dragon_str += ', '.join(Dragons[:3]) + '\n'
        Dragons[:3] = []
        raptor_str += ', '.join(Raptors[:3]) + '\n'
        Raptors[:3] = []
        count += 1

    # Write strings to .txt file
    writer("Sharks")
    writer(shark_str)
    writer("Dragons")
    writer(dragon_str)
    writer("Raptors")
    writer(raptor_str)

    # EXTRA CREDIT START

    # Re-populate teams
    to_letter('soccer_players.csv')
    to_team('soccer_players.csv')

    # Re-slice teams from XP and NXP lists
    Sharks = XP[:9] + NXP[:9]; XP[:9] = []; NXP[:9] = []
    Dragons = XP[:9] + NXP[:9]; XP[:9] = []; NXP[:9] = []
    Raptors = XP[:] + NXP[:]; XP = []; NXP = []

    # For loop to write files
    for names in players:
        writer1(name_flip(names), more)
        more += 1

