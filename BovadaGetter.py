import requests
import csv
from datetime import datetime
from TeamConverter import TeamConverter

tc = TeamConverter()
def getData(league):
	league_obj = leagueSelector(league)
	url = league_obj['url']
	mapper = league_obj['mapper']

	#Initialize outcomes list
	outcomes = []
	# Get the bovada odds
	source = requests.get(url).json()
	data = source[0]
	# Code for printing to a file 
	sample = open('output.json', 'w')
	sample.write(data.__str__())
	sample.close()
	# Populate outcomes
	for event in data['events']:
		try:
			event_type = event['displayGroups'][0]['description']
			if event_type != "Game Lines":
				continue
			age = ((datetime.now()-datetime.fromtimestamp((event['lastModified']/1000))).total_seconds())/60
			team1 = event['displayGroups'][0]['markets'][0]['outcomes'][0]['description']
			team1 = tc.convert(mapper, team1)
			team2 = event['displayGroups'][0]['markets'][0]['outcomes'][1]['description']
			team2 = tc.convert(mapper, team2)
			time = datetime.fromtimestamp((event['startTime']/1000)).date().__str__()
			game = team1+"-"+team2
			for outcome in event['displayGroups'][0]['markets'][0]['outcomes']:
				row = {}
				row['age']=age
				row['date'] = time
				row['game'] = game
				row['team'] = outcome['description']
				row['price'] = outcome['price']['decimal']
				row['probability'] = (1/float(row['price']))
				row['key'] = time+" "+game
				row['league'] = league
				# print("{0} ({1}) - {2:2.2f}%".format(row.team, row.price, row.bovada_p))
				outcomes.append(row)
		except:
			print("Error processing row.")
			continue
	return outcomes

def leagueSelector(league):
	selector={
		'nfl': {'url':"https://www.bovada.lv/services/sports/event/v2/events/A/description/football/nfl-playoffs", 'mapper': tc.nfl},
		'nba': {'url':"https://www.bovada.lv/services/sports/event/v2/events/A/description/basketball/nba", 'mapper': tc.nba}
	}
	out = selector[league]
	# print(out)
	return out


# outcomes = getData('nba')
# print("BOVADA DATA --------------")
# for row in outcomes:
# 	print("{0} {1} {2} {3}".format(row["date"], row["game"], row["team"], row["probability"]))



