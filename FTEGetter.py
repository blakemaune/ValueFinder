import requests
import csv
from TeamConverter import TeamConverter

tc = TeamConverter()

# 538 Getter
def getData(league):
	league_obj = leagueSelector(league)
	url = league_obj['url']
	mapper = league_obj['mapper']
	
	response = requests.get(url).text
	lines = response.splitlines()
	reader = csv.DictReader(lines)

	outcomes = []
	for game in reader:
		if game['score1'] or not game['elo_prob1']:
			continue
		else:
			# CONSIDER FIX - REVERSED MATCHUPS
			matchup = game['team2']+"-"+game['team1']
			#matchup = game['team1']+"-"+game['team2']

			# Handle result for team 1 win
			row = {}
			row['date'] = game['date']
			row['game'] = matchup
			row['team'] = tc.convert(mapper, game['team1'])
			row['probability'] = float(game['elo_prob1'])
			row['key'] = game['date']+" "+matchup
			row['league'] = league
			outcomes.append(row)

			# Handle result for team 2 win
			row = {}
			row['date'] = game['date']
			row['game'] = matchup
			row['team'] = tc.convert(mapper, game['team2'])
			row['probability'] = float(game['elo_prob2'])
			row['key'] = game['date']+" "+matchup
			row['league'] = league
			outcomes.append(row)
	return outcomes

def leagueSelector(league):
	selector={
		'nfl': {'url':"https://projects.fivethirtyeight.com/nfl-api/nfl_elo_latest.csv", 'mapper': tc.nfl},
		'nba': {'url':"https://projects.fivethirtyeight.com/nba-model/nba_elo_latest.csv", 'mapper': tc.nba}
	}
	out = selector[league]
	# print(out)
	return out

# outcomes = getData()
# print("538 DATA -----------------")
# for row in outcomes:
# 	print("{0} {1} {2} {3} {4}".format(row['date'],row['game'],row['team'],row['probability'],row['key']))