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
        game_stats = pd.read_csv('All_Data/Teams.csv')
        game_info = pd.read_csv('All_Data/RegularSeasonDetailedResults.csv')

        self.all_stats = pd.merge(game_stats, game_info, left_on="TeamID", right_on="WTeamID")

        all_teams = self.all_stats.TeamName.unique()

        all_years = self.all_stats.Season.unique()

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
        home = []

        for game in self.game_stats[team, year]['team']:
            if game == team:
                home.append(1)
            else:
                home.append(0)

        for column in self.game_stats[team, year]:
            if column == 'pts':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if home[iterator]:
                        pts += game
                    total_games += 1
                    iterator += 1
            if column == 'fgm':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if home[iterator]:
                        fgm += game
                    iterator += 1
            if column == 'fga':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if home[iterator]:
                        fga += game
                    iterator += 1
            if column == 't_3pm':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if home[iterator]:
                        t_3pm += game
                    iterator += 1
            if column == 't_3pa':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if home[iterator]:
                        t_3pa += game
                    iterator += 1
            if column == 'oreb':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if home[iterator]:
                        oreb += game
                    iterator += 1
            if column == 'reb':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if home[iterator]:
                        reb += game
                    iterator += 1
            if column == 'ast':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if home[iterator]:
                        ast += game
                    iterator += 1
            if column == 'stl':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if home[iterator]:
                        stl += game
                    iterator += 1
            if column == 'blk':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if home[iterator]:
                        blk += game
                    iterator += 1
            if column == 'turnover':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if home[iterator]:
                        turnover += game
                    iterator += 1
            if column == 'pf':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if home[iterator]:
                        pf += game
                    iterator += 1
            if column == 'pts_allowed':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if home[iterator]:
                        pts_allowed += game
                    iterator += 1
                    # opponent
            if column == 'pts_allowed':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if not home[iterator]:
                        pts += game
                    iterator += 1
            if column == 'opp_fgm':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if not home[iterator]:
                        fgm += game
                    iterator += 1
            if column == 'opp_fga':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if not home[iterator]:
                        fga += game
                    iterator += 1
            if column == 'opp_t_3pm':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if not home[iterator]:
                        t_3pm += game
                    iterator += 1
            if column == 'opp_t_3pa':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if not home[iterator]:
                        t_3pa += game
                    iterator += 1
            if column == 'opp_oreb':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if not home[iterator]:
                        oreb += game
                    iterator += 1
            if column == 'opp_reb':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if not home[iterator]:
                        reb += game
                    iterator += 1
            if column == 'opp_ast':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if not home[iterator]:
                        ast += game
                    iterator += 1
            if column == 'opp_stl':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if not home[iterator]:
                        stl += game
                    iterator += 1
            if column == 'opp_blk':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if not home[iterator]:
                        blk += game
                    iterator += 1
            if column == 'opp_turnover':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if not home[iterator]:
                        turnover += game
                    iterator += 1
            if column == 'opp_pf':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if not home[iterator]:
                        pf += game
                    iterator += 1
            if column == 'pts':
                iterator = 0
                for game in self.game_stats[team, year][column]:
                    if not home[iterator]:
                        pts_allowed += game
                    iterator += 1

        self.season_averages[team, year] = [pts/total_games, fgm/total_games, fga/total_games, t_3pa/total_games,
                                            t_3pm/total_games, oreb/total_games, reb/total_games, ast/total_games,
                                            stl/total_games, blk/total_games, turnover/total_games, pf/total_games,
                                            pts_allowed/total_games]

        return self.season_averages[team, year]




