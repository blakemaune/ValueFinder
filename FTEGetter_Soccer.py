import requests
import csv
import sys
import os

def getData():
	response = requests.get('https://projects.fivethirtyeight.com/soccer-api/club/spi_matches.csv')
	content = response.content
	# print(type(content))
	decoded = content.decode('utf-8')
	# print(type(decoded))
	lines = decoded.split('\n')
	reader = csv.DictReader(lines)

	outcomes = []
	for game in reader:
		if game['score1'] or not game['prob1']:
			continue
		else:
			# CONSIDER FIX - REVERSED MATCHUPS
			# matchup = game['team2']+"-"+game['team1']
			matchup = game['team1']+"-"+game['team2']

			# Handle result for team 1 win
			row = {}
			row['date'] = game['date']
			row['game'] = matchup
			long_game = row['game']
			teams = long_game.split('-')
			short_game = (teams[0][:3]).upper()+"-"+(teams[1][:3]).upper()
			row['game'] = short_game
			row['team'] = game['team1']
			row['probability'] = float(game['prob1'])+float(game['probtie'])
			row['key'] = game['date']+" "+matchup+" dnb"
			row['league'] = game['league']
			long_league = row['league']
			words = long_league.split(' ')
			short_league = ""
			for word in words:
				short_league+=(word[:1]).lower()
			row['league'] = short_league
			outcomes.append(row)

			# Handle result for team 2 win
			row = {}
			row['date'] = game['date']
			row['game'] = matchup
			long_game = row['game']
			teams = long_game.split('-')
			short_game = (teams[0][:3]).upper()+"-"+(teams[1][:3]).upper()
			row['game'] = short_game
			row['team'] = game['team2']
			row['probability'] = float(game['prob2'])+float(game['probtie'])
			row['key'] = game['date']+" "+matchup+" dnb"
			row['league'] = game['league']
			long_league = row['league']
			words = long_league.split(' ')
			short_league = ""
			for word in words:
				short_league+=(word[:1]).lower()
			row['league'] = short_league
			outcomes.append(row)
	# print("538: Populated "+len(outcomes).__str__()+" outcomes")
	return outcomes

def UnicodeDictReader(utf8_data, **kwargs):
    csv_reader = csv.DictReader(utf8_data, **kwargs)
    for row in csv_reader:
        yield {unicode(key, 'utf-8'):unicode(value, 'utf-8') for key, value in row.iteritems()}

if "-v" in sys.argv:
	outcomes = getData()
	for row in outcomes:
		print("{0} {1} {2} {3} {4}".format(row['date'],row['game'],row['team'],row['probability'],row['key']))