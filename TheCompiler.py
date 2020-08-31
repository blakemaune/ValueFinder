import datetime
from BovadaGetter import getData as getBovada
from FTEGetter import getData as get538
# IMPORTANT - Change the import to change settings for soccer
from BovadaGetter_Soccer import getData as getBovada_soccer_dnb
from FTEGetter_Soccer import getData as get538_soccer_dnb
from BovadaGetter_Soccer_3WM import getData as getBovada_soccer_3wm
from FTEGetter_Soccer_3WM import getData as get538_soccer_3wm


def analyze(league):
	if league=="soccer_3wm":
		bovada = getBovada_soccer_3wm()
		fivethirtyeight = get538_soccer_3wm()
	elif league=="soccer_dnb":
		bovada = getBovada_soccer_dnb()
		fivethirtyeight = get538_soccer_dnb()
	else:
		bovada = getBovada(league)
		fivethirtyeight = get538(league)

	rows = []
	for f in fivethirtyeight:
		for b in bovada:
			# print("Comparing\n"+f['key']+" to "+b['key'])
			fKey = f['key'].encode('utf8').decode('utf8')
			bKey = b['key'].encode('utf8').decode('utf8')
			if fKey == bKey:
				if f['team'] == b['team']:
					# print("found match in result")
					pb = b['probability']
					pf = f['probability']

					row = {}
					row['date']=f['date']
					row['game']=f['game']
					row['pick']=f['team']
					row['p538']=pf
					row['pBOV']=pb
					row['value']=(pf-pb)/(pf)
					row['price']=b['price']
					row['league']=f['league']
					rows.append(row)
					break
	return rows

# rows=analyze('nba')
# print("{0}\t{1}\t{2}\tp538\toBOV\tpBOV\tValue".format("Date".ljust(10), "Game".ljust(7), "Pick".ljust(16)))
# for row in rows:
	print("{0}\t{1}\t{2}\t{3:2.2f}%\t{4:1.3}\t{5:2.2f}%\t{6:1.3f}".format(row['date'],row['game'],(row['pick']).ljust(16),100*row['p538'],row['price'],100*row['pBOV'],row['value']))