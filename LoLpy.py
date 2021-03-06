import json
import urllib2

class LoLpy:
    """
    A library to make API calls to the official League of Legends API
    Attributes:
        api_key     Necessary to make api calls to riot. Can get one at https://developer.riotgames.com/sign-in?fhs=true
        region      What server you would like to access.
    """

    def __init__(self, api_key, region = 'na'):
        self.api_key = api_key
        self.region = region

    def makelolapicall(self, func):
        """Returns a api call to league of legends"""
        return json.loads(urllib2.urlopen('http://prod.api.pvp.net/api/lol/' + urllib2.quote(self.region + func) + '?api_key=' + urllib2.quote(self.api_key)).read())

    def makeproapicall(self, func):
        """Returns an api call to League of Legends"""
        return json.loads(urllib2.urlopen('http://prod.api.pvp.net/api/' + urllib2.quote(self.region + func) + '?api_key=' + urllib2.quote(self.api_key)).read())
        
    def get_champions(self):
        """Returns a python dictionary with all the league champions and their attributes"""
        return self.makelolapicall('/v1.1/champion')

    def get_game_by_id(self, summonerid):
        """Takes a summonerID, 
        Returns a python dictionary with information about the game a summoner is currently in and their recent games
        """
        return self.makelolapicall('/v1.1/game/by-summoner/' + str(summonerid) + '/recent')

    def get_league_by_id(self, summonerid):
        """Takes summonerID
        Returns data about the league a summoner is in
        """
        return self.makeproapicall('/v2.1/league/by-summoner/' + str(summonerid))

    def get_stats_summary_by_id(self, summonerid):
        """Takes a summonerID
        Returns summoner stats
        """
        return self.makelolapicall('/v1.1/stats/by-summoner/' + str(summonerid) + '/summary')

    def get_stats_ranked_by_id(self, summonerid):
        """Takes a summonerID
        Returns summoner ranked stats
        """
        return self.makelolapicall('/v1.1/stats/by-summoner/' + str(summonerid) + '/ranked')

    def get_summoner_masteries_by_id(self, summonerid):
        """Takes a summonerID
        Returns summoner masteries pages
        """
        return self.makelolapicall('/v1.1/summoner/' + str(summonerid) + '/masteries')

    def get_summoner_runes_by_id(self, summonerid):
        """Takes a summonerID
        Returns summoner runes pages
        """
        return self.makelolapicall('/v1.1/summoner/' + str(summonerid) + '/runes')

    def get_summoner_by_id(self, summonerid):
        """Takes a summonerID
        Returns information about a summoner
        """
        return self.makelolapicall('/v1.1/summoner/' + str(summonerid))

    def get_summoner_name_by_id(self, summonerid):
        """Takes a summonerID
        Returns a summoner name
        """
        return self.makelolapicall('/v1.1/summoner/' + str(summonerid) + '/name')

    def get_team_by_id(self, summonerid):
        """Takes a summonerID
        Returns information about teams a summoner is on
        """
        return self.makeproapicall('/v2.1/team/by-summoner' + str(summonerid))

    #############

    def get_summoner_by_name(self, name):
        """Takes a summoner name
        Returns information about the summoner
        """
        return self.makelolapicall('/v1.1/summoner/by-name/' + name)
    
    def get_game(self, name):
        """Takes a summoner name, 
        Returns a python dictionary with information about the game a summoner is currently in and their recent games
        """
        name = name.replace(' ','')
        summonerid = self.get_summoner_by_name(name)['id']
        return self.makelolapicall('/v1.1/game/by-summoner/' + str(summonerid) + '/recent')

    def get_league(self, name):
        """Takes summoner name
        Returns data about the league a summoner is in
        """
        name = name.replace(' ','')
        summonerid = self.get_summoner_by_name(name)['id']
        return self.makeproapicall('/v2.1/league/by-summoner/' + str(summonerid))

    def get_stats_summary(self, name):
        """Takes a summoner name
        Returns summoner stats
        """
        name = name.replace(' ','')
        summonerid = self.get_summoner_by_name(name)['id']
        return self.makelolapicall('/v1.1/stats/by-summoner/' + str(summonerid) + '/summary')

    def get_stats_ranked(self, name):
        """Takes a summoner name
        Returns summoner ranked stats
        """
        name = name.replace(' ','')
        summonerid = self.get_summoner_by_name(name)['id']
        return self.makelolapicall('/v1.1/stats/by-summoner/' + str(summonerid) + '/ranked')

    def get_summoner_masteries(self, name):
        """Takes a summoner name
        Returns summoner masteries pages
        """
        name = name.replace(' ','')
        summonerid = self.get_summoner_by_name(name)['id']
        return self.makelolapicall('/v1.1/summoner/' + str(summonerid) + '/masteries')

    def get_summoner_runes(self, name):
        """Takes a summoner name
        Returns summoner runes pages
        """
        name = name.replace(' ','')
        summonerid = self.get_summoner_by_name(name)['id']
        return self.makelolapicall('/v1.1/summoner/' + str(summonerid) + '/runes')

    def get_summoner(self, name):
        name = name.replace(' ','')
        summonerid = self.get_summoner_by_name(name)['id']
        return self.makelolapicall('/v1.1/summoner/' + str(summonerid))

    def get_summoner_name(self, name):
        """Takes a summoner name
        Returns information about a summoner
        """
        name = name.replace(' ','')
        summonerid = self.get_summoner_by_name(name)['id']
        return self.makelolapicall('/v1.1/summoner/' + str(summonerid) + '/name')

    def get_team(self, name):
        """Takes a summoner name
        Returns information about teams a summoner is on
        """
        name = name.replace(' ','')
        summonerid = self.get_summoner_by_name(name)['id']
        return self.makeproapicall('/v2.1/team/by-summoner' + str(summonerid))
