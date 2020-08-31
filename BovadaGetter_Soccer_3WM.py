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
			# event_type = event['displayGroups'][0]['description']
			# if event_type != "Game Lines":
			# 	continue
			
			try:
				bet_type = event['displayGroups'][0]['markets'][2]['description']
				if bet_type != "3-Way Moneyline":
					continue
				age = ((datetime.now()-datetime.fromtimestamp((event['lastModified']/1000))).total_seconds())/60
				team1 = event['displayGroups'][1]['markets'][0]['outcomes'][0]['description']
				team2 = event['displayGroups'][1]['markets'][0]['outcomes'][1]['description']
				time = datetime.fromtimestamp((event['startTime']/1000)).date().__str__()
				game = team1+"-"+team2
				for outcome in event['displayGroups'][0]['markets'][2]['outcomes']:
					row = {}
					row['age']= age
					row['date'] = time
					row['game'] = game.encode('utf8').decode('utf8')
					long_game = row['game']
					teams = long_game.split('-')
					short_game = (teams[0][:3]).upper()+"-"+(teams[1][:3]).upper()
					row['game'] = short_game
					row['team'] = outcome['description'].encode('utf8').decode('utf8')
					row['price'] = outcome['price']['decimal']
					row['probability'] = (1/float(row['price']))
					row['key'] = time+" "+game+" 3wm"
					row['type'] = bet_type
					row['league'] = "Soccer"
					# print("{0} ({1}) - {2:2.2f}%".format(row.team, row.price, row.bovada_p))
					outcomes.append(row)
			except:
				continue
	return outcomes


if "-v" in sys.argv:
	outcomes = getData()
	print("BOVADA DATA --------------")
	for row in outcomes:
		print("{0} {1} {2} {3} {4}".format(row["date"], row["game"], row["team"], row["probability"], row['type']))
