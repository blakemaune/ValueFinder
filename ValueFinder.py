import datetime
import requests
import csv
import sys
from BovadaGetter import getData as getBovada
from FTEGetter import getData as get538
from BovadaGetter_Soccer import getData as getBovada_soccer
from FTEGetter_Soccer import getData as get538_soccer
from TeamConverter import TeamConverter
from TheCompiler import analyze


# Print them to file
with open('hidden_gems.csv', mode='w') as csv_file:
	fieldnames = ['date', 'game', 'pick', 'p538', 'price', 'pBOV', 'value', 'league']
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	writer.writeheader()

	print("{0}\t{1}\t{2}\tp538\toBOV\tpBOV\tValue\tLeague".format("Date".ljust(10), "Game".ljust(7), "Pick".ljust(16)))
	if "nfl" in sys.argv:
		nflRows = analyze('nfl')
		for row in nflRows:
			print("{0}\t{1}\t{2}\t{3:2.2f}%\t{4:1.3}\t{5:2.2f}%\t{6:1.3f}\t{7}".format(row['date'],row['game'],(row['pick']).ljust(16),100*row['p538'],row['price'],100*row['pBOV'],row['value'],row['league']))
			writer.writerow(row)
	if "nba" in sys.argv:
		nbaRows = analyze('nba')
		for row in nbaRows:
			print("{0}\t{1}\t{2}\t{3:2.2f}%\t{4:1.3}\t{5:2.2f}%\t{6:1.3f}\t{7}".format(row['date'],row['game'],(row['pick']).ljust(16),100*row['p538'],row['price'],100*row['pBOV'],row['value'],row['league']))
			writer.writerow(row)
	if "soc_dnb" in sys.argv or "soccer_dnb" in sys.argv:
		socRows_dnb = analyze('soccer_dnb')
		for row in socRows_dnb:
			print("{0}\t{1}\t{2}\t{3:2.2f}%\t{4:1.3}\t{5:2.2f}%\t{6:1.3f}\t{7}".format(row['date'],row['game'],(row['pick']).ljust(16),100*row['p538'],row['price'],100*row['pBOV'],row['value'],row['league']))
			writer.writerow(row)
	if "soc_3wm" in sys.argv or "soccer_3wm" in sys.argv:
		socRows_3wm = analyze('soccer_3wm')
		for row in socRows_3wm:
			print("{0}\t{1}\t{2}\t{3:2.2f}%\t{4:1.3}\t{5:2.2f}%\t{6:1.3f}\t{7}".format(row['date'],row['game'],(row['pick']).ljust(16),100*row['p538'],row['price'],100*row['pBOV'],row['value'],row['league']))
			writer.writerow(row)
