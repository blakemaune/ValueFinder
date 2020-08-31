import requests
import csv
import sys
from datetime import datetime

def getData():
	url = "https://www.bovada.lv/services/sports/event/v2/events/A/description/soccer"

	#Initialize outcomes list
	outcomes = []
	# Get the bovada odds
	source = requests.get(url).json()
	
	for data in source:
		# Code for printing to a file 
		sample = open('output.json', 'w')
		sample.write(data.__str__())
		sample.close()
		# Populate outcomes
		for event in data['events']:
			try:
				bet_type = event['displayGroups'][1]['markets'][0]['description']
				if bet_type != "Draw No Bet":
					continue
			except:
				print("Error processing " + event['description'])
				continue

			try:
				age = ((datetime.now()-datetime.fromtimestamp((event['lastModified']/1000))).total_seconds())/60
				team1 = event['displayGroups'][1]['markets'][0]['outcomes'][0]['description']
				team2 = event['displayGroups'][1]['markets'][0]['outcomes'][1]['description']
				time = datetime.fromtimestamp((event['startTime']/1000)).date().__str__()
				game = team1+"-"+team2
				for outcome in event['displayGroups'][1]['markets'][0]['outcomes']:
					row = {}
					row['age']= age
					row['date'] = time
					row['game'] = game
					long_game = row['game'].encode('utf-8').decode('utf-8')
					teams = long_game.split('-')
					short_game = (teams[0][:3]).upper()+"-"+(teams[1][:3]).upper()
					row['game'] = short_game
					row['team'] = outcome['description'].encode('utf-8').decode('utf-8')
					row['price'] = outcome['price']['decimal']
					row['probability'] = (1/float(row['price']))
					row['key'] = time+" "+game+" dnb"
					row['type'] = bet_type
					row['league'] = "Soccer"
					long_league = row['league']
					words = long_league.split(' ')
					short_league = ""
					for word in words:
						short_league+=(word[:1]).lower()
					row['league'] = short_league
					# print("{0} ({1}) - {2:2.2f}%".format(row.team, row.price, row.bovada_p))
					outcomes.append(row)
			except:
				print("Error processing outcomes for" + event['description'])	
	return outcomes


if "-v" in sys.argv:
	outcomes = getData()
	print("Bovada: Processed "+len(outcomes).__str__()+" outcomes")
	print("BOVADA DATA --------------")
	for row in outcomes:
		print("{0} {1} {2} {3} {4}".format(row["date"], row["game"], row["team"], row["probability"], row['type']))
