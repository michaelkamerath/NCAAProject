import pandas as pd
import TeamStatistics as ts
import numpy as np

game_stats = pd.read_csv('All_Data/09_14_game_stats.csv')
game_info = pd.read_csv('All_Data/09_14_game_info.csv')

all_stats = pd.merge(game_stats, game_info, left_on="game_id", right_on="Game_ID")

all_teams = all_stats.team.unique()

all_years = all_stats.year.unique()

all_teams = sorted(all_teams)
all_years = sorted(all_years)

#print(all_teams)
#print(all_years)

unc_2008 = all_stats.ix[((all_stats['team'] == 'North Carolina') | (all_stats['opponent'] == 'North Carolina'))
                        & (all_stats['year'] == 2008)]

al_huntsville_2008 = all_stats.ix[
    ((all_stats['team'] == 'AL-Huntsville') | (all_stats['opponent'] == 'AL-Huntsville'))
    & (all_stats['year'] == 2008)]

team_stats = ts.TeamStatistics()
team_stats.setup('North Carolina', 2008, unc_2008)

team_stats.create_stats('North Carolina', 2008)
