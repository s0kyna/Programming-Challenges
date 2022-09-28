import csv 
from pathlib import Path 

csv_file = Path("Premier 16-17.csv")

def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)                  ###   skip first row (header)
            for row in reader:
                csv_contents.append(row)
    return csv_contents

def process_results(rows):
    dictionary = {}
    referees = {}
    ref_games = {}
    
    for row in rows:
        home,away,home_goals,away_goals,winner = row[1],row[2],row[3],row[4],row[5]
        if home not in dictionary:
            dictionary[home] = [0,0,0,0,0] # win,draw,lost,goal diff,points
            
        if away not in dictionary:
            dictionary[away] = [0,0,0,0,0] # win,draw,lost,goal diff,points

        ### check if it is draw            
        if winner == "D":
            dictionary[home][4] += 1
            dictionary[away][4] += 1

            dictionary[home][1] += 1
            dictionary[away][1] += 1
            
        #winner is home
        if winner == "H":
            dictionary[home][4] += 3
            dictionary[home][0] += 1
            dictionary[away][2] += 1
            
        #winner is away            
        if winner == "A":
            dictionary[away][4] += 3
            dictionary[away][0] += 1
            dictionary[home][2] += 1
            
        #calculate goal difference for home and away team
        dictionary[home][3] += int(home_goals) - int(away_goals)
        dictionary[away][3] += int(away_goals) - int(home_goals)
        
        ref = row[6]
        if ref not in referees:
            referees[ref] = 0 # Card points
        referees[ref] += int(row[15]) + int(row[16]) + (int(row[17]))*3 + (int(row[18]))*3

        if ref not in ref_games:
            ref_games[ref] = 0 # num of games
        ref_games[ref] += 1
        
    lowest_card = 999
    most_card = 0
    most_ref = ""
    least_ref = ""
    
    for keys,values in referees.items():
        if (values/ref_games[keys]) > most_card:
            most_card = values/ref_games[keys]
            most_ref = keys
            
        if (values/ref_games[keys]) < lowest_card:
            lowest_card = values/ref_games[keys]
            least_ref = keys
            
    print("Most cards ref: ",most_ref)
    print("Least cards ref: ",least_ref,"\n")
    
    dictionary = sorted(dictionary.items(), key=lambda e: e[1][4],reverse = True) #sorts dictionary
    return dictionary

def printTable(dictionary): # prints league table
    print(f"{'Team':15} {'Wins':10} {'Draws':10} {'Losses':10} {'Goal diff':10} {'Points':10}")
    for keys,values in dictionary:
        print(f"{keys:15} {values[0]:<10} {values[1]:<10} {values[2]:<10} {values[3]:<10} {values[4]:<10}")

def statistics(rows):
    stats = {}
    for row in rows:
        home,away,home_shots,away_shots,home_targets,away_targets = row[1],row[2],row[7],row[8],row[9],row[10]
        home_fouls,away_fouls = row[11],row[12]
        
        if home not in stats:
            stats[home] = [0,0,0] # shots,target,fouls
            
        if away not in stats:
            stats[away] = [0,0,0] # shots,target,fouls

        stats[home][0] += int(home_shots)
        stats[home][1] += int(home_targets)
        stats[home][2] += int(home_fouls)
        
        stats[away][0] += int(away_shots)
        stats[away][1] += int(away_targets)
        stats[away][2] += int(away_fouls)

    dirtiest = ""
    cleanest= ""
    accurate_team = ""
    least_accurate_team = ""
    
    most_fouls = 0
    least_fouls = 999
    most_accurate = 0
    least_accurate = 1
    
    for keys,values in stats.items():

        accuracy = (values[1])/(values[0])
        
        if accuracy > most_accurate:
            most_accurate = accuracy
            accurate_team = keys
            
        if accuracy < least_accurate:
            least_accurate = accuracy
            least_accurate_team = keys

        if values[2] > most_fouls:
            most_fouls = values[2]
            dirtiest = keys
            
        if values[2] < least_fouls:
            least_fouls = values[2]
            cleanest = keys

    print("Cleanest: ",cleanest)
    print("Dirtiest: ",dirtiest)
    print("Most accurate: ",accurate_team)
    print("Least accurate: ",least_accurate_team)
    return stats

if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    printTable(process_results(file_contents))
    statistics(file_contents)
