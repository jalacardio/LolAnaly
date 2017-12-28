import urllib2


class JsonReceiver:
    accountKey = "?api_key="
    rootUrl = "https://na1.api.riotgames.com/"

    def __init__(self, key):
        self.accountKey += key

    def get_json_summoner_info(self, account_id):
        summoner_url = "/lol/summoner/v3/summoners/by-account/" + account_id
        f = urllib2.urlopen(self.rootUrl + summoner_url + self.accountKey)
        return f.read()


jr = JsonReceiver("RGAPI-9e18de3a-cb58-4628-9465-42a2278808c7")
res = jr.get_json_summoner_info("211349596")
print(res)