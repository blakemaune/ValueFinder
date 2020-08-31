#Team Converter
nfl_names=["Arizona Cardinals","Atlanta Falcons","Baltimore Ravens","Buffalo Bills","Carolina Panthers","Chicago Bears","Cincinnati Bengals","Cleveland Browns","Dallas Cowboys","Denver Broncos","Detroit Lions","Green Bay Packers","Houston Texans","Indianapolis Colts","Jacksonville Jaguars","Kansas City Chiefs","Los Angeles Chargers","Los Angeles Rams","Miami Dolphins","Minnesota Vikings","New England Patriots","New Orleans Saints","New York Giants","New York Jets","Oakland Raiders","Philadelphia Eagles","Pittsburgh Steelers","Seattle Seahawks","San Francisco 49ers","Tampa Bay Buccaneers","Tennessee Titans","Washington Redskins"]
nfl_abbs=["ARI","ATL","BAL","BUF","CAR","CHI","CIN","CLE","DAL","DEN","DET","GB","HOU","IND","JAX","KC","LAC","LAR","MIA","MIN","NE","NO","NYG","NYJ","OAK","PHI","PIT","SEA","SF","TB","TEN","WAS"]
nba_names=["Atlanta Hawks","Brooklyn Nets","Boston Celtics","Charlotte Hornets","Chicago Bulls","Cleveland Cavaliers","Dallas Mavericks","Denver Nuggets","Detroit Pistons","Golden State Warriors","Houston Rockets","Indiana Pacers","Los Angeles Clippers","Los Angeles Lakers","Memphis Grizzlies","Miami Heat","Milwaukee Bucks","Minnesota Timberwolves","New Orleans Pelicans","New York Knicks","Oklahoma City Thunder","Orlando Magic","Philadelphia 76ers","Phoenix Suns","Portland Trail Blazers","Sacramento Kings","San Antonio Spurs","Toronto Raptors","Utah Jazz","Washington Wizards"]
nba_abbs=["ATL","BKN","BOS","CHA","CHI","CLE","DAL","DEN","DET","GSW","HOU","IND","LAC","LAL","MEM","MIA","MIL","MIN","NOP","NYK","OKC","ORL","PHI","PHX","POR","SAC","SAS","TOR","UTA","WAS"]

class TeamConverter:
	def __init__(self):
		self.nfl = {}
		self.nba = {}
		self.nhl = {}
		self.mlb = {}
		self.mls = {}
		self.epl = {}

		# print("Initializing teamconverter...")
		for i in range(len(nfl_names)):
			self.doubleMap(self.nfl, nfl_names[i], nfl_abbs[i])
		# print("Mapped NFL Names")
		for i in range(len(nba_names)):
			self.doubleMap(self.nba, nba_names[i], nba_abbs[i])
		#print("Mapped NBA Names")		

	def doubleMap(self, dictionary, key, value):
		dictionary[key]=value
		dictionary[value]=key

	def convert(self, dictionary, input):
		try:
			out = dictionary[input]
		except:
			out = "(error) "+input
		return out

	def sayHi(self):
		print("Hi")


