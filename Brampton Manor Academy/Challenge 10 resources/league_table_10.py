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
    return dictionary

if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    print(process_results(file_contents))
 
