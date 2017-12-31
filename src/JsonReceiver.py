from urllib.request import urlopen


class JsonReceiver:
    accountKey = "?api_key="
    rootUrl = "https://na1.api.riotgames.com/"

    def __init__(self, key):
        self.accountKey += key

    def get_json_summoner_info(self, account_id):
        summoner_url = "/lol/summoner/v3/summoners/by-account/" + str(account_id)
        full_url = urlopen(self.rootUrl + summoner_url + self.accountKey)
        return full_url.read()

    def get_json_summoner_match(self,account_id):
    	summoner_url = "/lol/match/v3/matchlists/by-account/" + str(account_id) + "/recent"
    	full_url = urlopen(self.rootUrl + summoner_url + self.accountKey)
    	return full_url.read()
    def get_json_winning_info(self,summoner_id):
    	summoner_url = "/lol/league/v3/positions/by-summoner/" + str(summoner_id)
    	full_url = urlopen(self.rootUrl + summoner_url + self.accountKey)
    	return full_url.read()
    def get_json_game_info(self,game_Id):
    	summoner_url = "/lol/match/v3/matches/" + str(game_Id)
    	full_url = urlopen(self.rootUrl + summoner_url + self.accountKey)
    	return full_url.read()