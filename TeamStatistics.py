from collections import defaultdict


class TeamStatistics(object):

    # This class contains statistics about all teams currently
    # in the data set. The game_stats from the entire season
    # for each team are kept track of so averages for the season
    # can be computed. Both of the data structures will have keys
    # that are the team name and year because together, they determine
    # what a unique season is for a team.
    def __init__(self):
        self.game_stats = defaultdict(lambda: [0, 0])
        self.season_averages = defaultdict(lambda : [0,0])

    # Adds data obtained from the csv files to this class
    # It will later be used to calculate averages for the
    # season.
    #  prerequisites - none
    #  arguments:
    #    team: Name of team
    #    year: the year being considered when collecting statistics
    #    frame: the data frame containing information about the team
    def setup(self, team, year, frame):
        self.game_stats[team, year].append(frame)

    def create_stats(self, team, year):
        for key, value, frame in 



