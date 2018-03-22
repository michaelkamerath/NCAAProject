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
        
        # Stores the games for a team during a certain season.
        # The combination of TeamID and season are the key to the dictionary
        # Example usage: self.__game_stats[1168, 2008]['ColumnName']
        self.__game_stats = defaultdict(lambda: [0, 0])
        
        # Season averages is populated and then used by the model to
        # predict the winner of whatever matchup specified.
        self.__season_averages = defaultdict(lambda : [0,0])
        
        self.__teams = pd.DataFrame()
        
        # Stores all of the statistics for each game played through every
        # Season from 1985 to the present
        self.__game_infos = pd.DataFrame()
        
        # all_teams is just an alphabetical list of all NCAA D1 teams from
        # 1985 on.
        self.__all_teams = []
        
        # all_years is used by the GUI to populate the possible years field
        self.__all_years = []

    # Adds data obtained from the csv files to this class
    # It will later be used to calculate averages for the
    # season.
    #  prerequisites - none
    #  arguments:
    #    team: Name of team
    #    year: the year being considered when collecting statistics
    #    frame: the data frame containing information about the team
    def setup(self, team, year, frame):
        self.__game_stats[team, year] = frame

    # Gets all the information from the CSV files.
    # Teams and individual game infos are the most important part of this step.
    # Also sets up the all_teams and all_years lists to be used by the GUI.
    #  prerequisites - none
    #  arguments: - none
    #  return: none
    def read_in_data(self):
        self.__teams = pd.read_csv('All_Data/Teams.csv', encoding="utf-8")
        self.__game_infos = pd.read_csv('All_Data/RegularSeasonDetailedResults_Prelim2018.csv', encoding="utf-8")
        
        all_teams = self.__teams.TeamName.unique()

        all_years = self.__game_infos.Season.unique()

        self.__all_teams = sorted(all_teams)
        self.__all_years = sorted(all_years)

    # Based on the team and year, this function will populate the game_stats
    # frame with the teams stats from the season. The create_stats function then
    # uses the info obtained from this function.
    #  prerequisites - read_in_data has completed
    #  arguments:
    #    team1: The team whose stats you want to populate
    #    year: The season to apply those stats
    #  return: none
    
    def populate_game_stats(self, team1, year):
        team_id = self.get_team_id(team1)
        self.__game_stats[team_id, year] = self.__game_infos.ix[
            ((self.__game_infos['WTeamID'] == team_id) | (self.__game_infos['LTeamID'] == team_id))
            & (self.__game_infos['Season'] == year)]
    
    # Convenience function to get the teamID based on a team name
    #  prerequisites - read_in_data has completed
    #  arguments:
    #    team_name: The name of an NCAA team (must be in all_teams list)
    #  return: The team_id associated with an NCAA team
    
    def get_team_id(self, team_name):
        row = self.__teams.loc[self.__teams['TeamName'] == team_name]
        return row.iloc[0,0]
    
    # Convenience function to get the teamName based on its teamID
    #  prerequisites - read_in_data has completed
    #  arguments:
    #    team_id: The teamID of an NCAA team
    #  return: The teamName associated with a particular teamID
    
    def get_team_name(self, team_id):
        row = self.__teams.loc[self.__teams['TeamID'] == team_id]
        return row.iloc[0,0]
    
    # Getter for the all_teams member variable
    #  prerequisites - read_in_data has completed
    #  arguments: none
    #  return: The list of all NCAA teams
    def get_all_teams(self):
        return self.__all_teams
    
    # Getter for the all_years member variable
    #  prerequisites - read_in_data has completed
    #  arguments: none
    #  return: The list of all seasons the data contains
    def get_all_years(self):
        return self.__all_years
    
    def get_team_season_averages(self, team, year):
        return self.__season_averages[team, year]
        
    # Populates the season_averages for a team during a specific season
    #  prerequisites -populate_game_stats function has been called
    #  for the team and season.
    #  arguments:
    #    team: The name of an NCAA team
    #    year: The season that NCAA team played
    #  return: The averages for that team for the season.
    
    def create_stats(self, team, year):
        #print(self.__game_stats[team, year])
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
        team_id = self.get_team_id(team)

        for game in self.__game_stats[team_id, year]['WTeamID']:
            if game == team_id:
                home.append(1)
            else:
                home.append(0)

        for column in self.__game_stats[team_id, year]:
            if column == 'WScore':
                iterator = 0
                for game in self.__game_stats[team_id, year][column]:
                    if home[iterator]:
                        pts += game
                    total_games += 1
                    iterator += 1
            if column == 'WFGM':
                iterator = 0
                for game in self.__game_stats[team_id, year][column]:
                    if home[iterator]:
                        fgm += game
                    iterator += 1
            if column == 'WFGA':
                iterator = 0
                for game in self.__game_stats[team_id, year][column]:
                    if home[iterator]:
                        fga += game
                    iterator += 1
            if column == 'WFGM3':
                iterator = 0
                for game in self.__game_stats[team_id, year][column]:
                    if home[iterator]:
                        t_3pm += game
                    iterator += 1
            if column == 'WFGA3':
                iterator = 0
                for game in self.__game_stats[team_id, year][column]:
                    if home[iterator]:
                        t_3pa += game
                    iterator += 1
            if column == 'WOR':
                iterator = 0
                for game in self.__game_stats[team_id, year][column]:
                    if home[iterator]:
                        oreb += game
                    iterator += 1
            if column == 'WDR':
                iterator = 0
                for game in self.__game_stats[team_id, year][column]:
                    if home[iterator]:
                        reb += game
                    iterator += 1
            if column == 'WAst':
                iterator = 0
                for game in self.__game_stats[team_id, year][column]:
                    if home[iterator]:
                        ast += game
                    iterator += 1
            if column == 'WStl':
                iterator = 0
                for game in self.__game_stats[team_id, year][column]:
                    if home[iterator]:
                        stl += game
                    iterator += 1
            if column == 'WBlk':
                iterator = 0
                for game in self.__game_stats[team_id, year][column]:
                    if home[iterator]:
                        blk += game
                    iterator += 1
            if column == 'WTO':
                iterator = 0
                for game in self.__game_stats[team_id, year][column]:
                    if home[iterator]:
                        turnover += game
                    iterator += 1
            if column == 'WPF':
                iterator = 0
                for game in self.__game_stats[team_id, year][column]:
                    if home[iterator]:
                        pf += game
                    iterator += 1
            if column == 'LScore':
                iterator = 0
                for game in self.__game_stats[team_id, year][column]:
                    if home[iterator]:
                        pts += game
                    iterator += 1
        
        self.__season_averages[team_id, year] = [pts/total_games, fgm/total_games, fga/total_games, t_3pa/total_games,
                                            t_3pm/total_games, oreb/total_games, reb/total_games, ast/total_games,
                                            stl/total_games, blk/total_games, turnover/total_games, pf/total_games,
                                            pts_allowed/total_games]




