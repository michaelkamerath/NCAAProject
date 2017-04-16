from collections import defaultdict
import pandas as pd


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
        self.all_stats = pd.DataFrame()
        self.all_teams = []
        self.all_years = []

    # Adds data obtained from the csv files to this class
    # It will later be used to calculate averages for the
    # season.
    #  prerequisites - none
    #  arguments:
    #    team: Name of team
    #    year: the year being considered when collecting statistics
    #    frame: the data frame containing information about the team
    def setup(self, team, year, frame):
        self.game_stats[team, year] = frame

    def read_in_data(self):
        game_stats = pd.read_csv('All_Data/09_14_game_stats.csv')
        game_info = pd.read_csv('All_Data/09_14_game_info.csv')

        self.all_stats = pd.merge(game_stats, game_info, left_on="game_id", right_on="Game_ID")

        all_teams = self.all_stats.team.unique()

        all_years = self.all_stats.year.unique()

        self.all_teams = sorted(all_teams)
        self.all_years = sorted(all_years)

    def populate_game_stats(self, team1, year):
        self.game_stats[team1, year] = self.all_stats.ix[
            ((self.all_stats['team'] == team1) | (self.all_stats['opponent'] == team1))
            & (self.all_stats['year'] == year)]

    def create_stats(self, team, year):
        #print(self.game_stats[team, year])
        pts = 0
        fgm = 0
        fga = 0
        t_3pm = 0
        t_3pa = 0
        oreb = 0
        reb = 0
        ast = 0
        stl = 0
        blk = 0
        turnover = 0
        pf = 0
        pts_allowed = 0
        total_games = 0
        for column in self.game_stats[team, year]:
            if column == 'pts':
                for game in self.game_stats[team, year][column]:
                    pts += game
                    total_games += 1
            if column == 'fgm':
                for game in self.game_stats[team, year][column]:
                    fgm += game
            if column == 'fga':
                for game in self.game_stats[team, year][column]:
                    fga += game
            if column == 't_3pm':
                for game in self.game_stats[team, year][column]:
                    t_3pm += game
            if column == 't_3pa':
                for game in self.game_stats[team, year][column]:
                    t_3pa += game
            if column == 'oreb':
                for game in self.game_stats[team, year][column]:
                    oreb += game
            if column == 'reb':
                for game in self.game_stats[team, year][column]:
                    reb += game
            if column == 'ast':
                for game in self.game_stats[team, year][column]:
                    ast += game
            if column == 'stl':
                for game in self.game_stats[team, year][column]:
                    stl += game
            if column == 'blk':
                for game in self.game_stats[team, year][column]:
                    blk += game
            if column == 'turnover':
                for game in self.game_stats[team, year][column]:
                    turnover += game
            if column == 'pf':
                for game in self.game_stats[team, year][column]:
                    pf += game
            if column == 'pts_allowed':
                for game in self.game_stats[team, year][column]:
                    pts_allowed += game

        self.season_averages[team, year] = [pts/total_games, fgm/total_games, fga/total_games, t_3pa/total_games,
                                            t_3pm/total_games, oreb/total_games, reb/total_games, ast/total_games,
                                            stl/total_games, blk/total_games, turnover/total_games, pf/total_games,
                                            pts_allowed/total_games]

        return self.season_averages[team, year]




