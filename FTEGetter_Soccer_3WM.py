import requests
import csv
import sys

def getData():
	response = requests.get('https://projects.fivethirtyeight.com/soccer-api/club/spi_matches.csv')
	content = response.content
	decoded = content.decode('utf-8')
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
			row['probability'] = float(game['prob1'])
			row['key'] = game['date']+" "+matchup+" 3wm"
			row['league'] = game['league']
			long_league = row['league']
			words = long_league.split(' ')
			short_league = ""
			for word in words:
				short_league+=(word[:1]).lower()
			row['league'] = short_league+"_3wm"
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
			row['probability'] = float(game['prob2'])
			row['key'] = game['date']+" "+matchup+" 3wm"
			row['league'] = game['league']
			long_league = row['league']
			words = long_league.split(' ')
			short_league = ""
			for word in words:
				short_league+=(word[:1]).lower()
			row['league'] = short_league+"_3wm"
			outcomes.append(row)

			# Handle result for Draw
			row = {}
			row['date'] = game['date']
			row['game'] = matchup
			long_game = row['game']
			teams = long_game.split('-')
			short_game = (teams[0][:3]).upper()+"-"+(teams[1][:3]).upper()
			row['game'] = short_game
			row['team'] = "Draw"
			row['probability'] = float(game['probtie'])
			row['key'] = game['date']+" "+matchup+" 3wm"
			row['league'] = game['league']
			long_league = row['league']
			words = long_league.split(' ')
			short_league = ""
			for word in words:
				short_league+=(word[:1]).lower()
			row['league'] = short_league+"_3wm"
			outcomes.append(row)
	return outcomes

if "-v" in sys.argv:
	outcomes = getData()
	for row in outcomes:
		print("{0} {1} {2} {3} {4}".format(row['date'],row['game'],row['team'],row['probability'],row['key']))