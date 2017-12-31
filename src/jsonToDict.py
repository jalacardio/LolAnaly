import json
from JsonReceiver import JsonReceiver



class JsonToDict:
	jr = JsonReceiver("RGAPI-004a6fb4-cbd1-42dc-91e6-d5d40933108e")

	def getSummonerName(self,accountid):
		input = self.bts(self.jr.get_json_summoner_info(accountid))
		spdict = json.loads(input)
		return str(spdict["name"])

	def getSummonerLevel(self,accountid):
		input = self.bts(self.jr.get_json_summoner_info(accountid))
		spdict = json.loads(input)
		return str(spdict["summonerLevel"])

	def getSummonerId(self,accountid):
		input = self.bts(self.jr.get_json_summoner_info(accountid))
		spdict = json.loads(input)
		return(spdict["id"])

	def getMatches(self,accountid):
		input = self.bts(self.jr.get_json_summoner_match(accountid))
		spdict = json.loads(input)
		matches = list(spdict["matches"])
		gameid_list = []
		for match in matches:
			gameid_list.append(match["gameId"])
		return gameid_list


	def winRates(self, summonerId):
		input = self.bts(self.jr.get_json_winning_info(summonerId))
		spdict = json.loads(input)
		wr = spdict[0]["wins"]/(spdict[0]["wins"]+spdict[0]["losses"])
		return wr

	def playerRank(self,summonerId):
		input = self.bts(self.jr.get_json_winning_info(summonerId))
		spdict = json.loads(input)
		rank = spdict[0]["tier"] + " " + spdict[0]["rank"]
		return rank

	def getParticipantId(self, gameId, accountid):
		input = self.bts(self.jr.get_json_game_info(gameId))
		spdict = json.loads(input)
		playerList = spdict["participantIdentities"]
		for player in playerList:
			if(player["player"]["accountId"] == accountid):
				partId = player["participantId"]
		return partId

	def playerKDA(self, partId,gameId):
		input = self.bts(self.jr.get_json_game_info(gameId))
		spdict = json.loads(input)
		participants = spdict["participants"]
		stats = participants[partId-1]

		print(stats["stats"]["kills"], "/",stats["stats"]["deaths"], "/", stats["stats"]["assists"] )

	def bts(self,input):
		return str(input,'utf-8')

name = JsonToDict()
print("Summoner ID:", name.getSummonerName(211349596))
level = JsonToDict()
#print("Level:", level.getSummonerLevel("211349596"))
num = JsonToDict()
#print (num.getMatches("211349596"))

print("%.2f"%(num.winRates(48423009)))
print(num.playerRank(48423009))
num.playerKDA(7, 2680404511)