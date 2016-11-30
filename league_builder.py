if __name__ == "__main__":

    # Soccer League Builder
    # create three teams - Dragons, Sharks, and Raptors
    def league_builder():
        import csv

        assigned = list()
        dragons = list()
        raptors = list()
        sharks = list()
        teams = [{'Team' : 'Dragons'}, {'Team' : 'Raptors'}, {'Team' : 'Sharks'}]

        # Place the 18 children that have signed up for the League into balanced teams
        # Make sure there are an equal number on each team
        def add_player(team, string):
            ncount = 0
            count = 0
            for player in players:
                if player['Soccer Experience'] == 'YES' and count < divisor and player not in assigned:
                    player.update({'Team':string})
                    team.append(player)
                    assigned.append(player)
                    count += 1
                elif ncount < divisor and player not in assigned:
                    player.update({'Team':string})
                    team.append(player)
                    assigned.append(player)
                    ncount += 1

        # Write the newly balanced rosters to teams.txt file for distribution
        def write_roster(team, string):
            title = '\nThe {} Roster\n'.format(string)
            header = 'Name   | Exp |   Guardians\n________________________________________________\n'
            my_string = "{Name} | {Soccer Experience} | {Guardian Name(s)}"
            with open('teams.txt', "a") as file:
                file.write(title)
                file.write(header)

            for player in team:
                player = my_string.format(**player)
                with open('teams.txt', "a") as file:
                    file.write(player)
                    file.write('\n')
                    
        # Extra Credit: Create 18 welcome letters to guardians. For example, kenneth_love.txt.
        # Extra Credit: include players name, date and time of first practice and team names for each player
        def write_letter(player):
            txtname = '{Name}.txt'.format(**player)
            # How do I break this line to fit on the screen while keeping it in the same line of code?
            letter = 'Dear {Guardian Name(s)},\n\nWelome to the 2016/2017 Soccer League. Little {Name} will be playing for the {Team} this year.\nThe first practice is on Dec. 5th at 5:00am.... Jakarta Time... Good Luck!\n\nSincerely,\nJeffrey the Badass'.format(**player)
            with open(txtname, "w") as file:
                file.write(letter)

        # import the csv file and convert to usable data type
        with open('soccer_players.csv', newline='') as csvfile:
            artreader = csv.DictReader(csvfile)
            players = list(artreader)
            # Assuming that there will always be an even number of experienced and inexperienced players
            divisor = (int(len(players)) / int(len(teams)))/2

        add_player(dragons, 'Dragons')
        add_player(raptors, 'Raptors')
        add_player(sharks, 'Sharks')

        with open('teams.txt', "w") as file:
            file.write('Welcome to the 2016/2017 Badass Soccer League! \nBelow are the expertly balanced rosters:\n\n')

        write_roster(dragons, 'Dragons')
        write_roster(raptors, 'Raptors')
        write_roster(sharks, 'Sharks')

        for player in players:
            write_letter(player)
            
    league_builder()
