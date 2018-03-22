from math import expm1, fabs
import TeamStatistics as ts
from collections import defaultdict

stats_class = ts.TeamStatistics()
stats_class.read_in_data()

class Model(object):
    
    # Our model is in the form Win Percentage = e^v / 1 + e^v
    # In this case, our v is:
    #  points * predictor1 + fg_percentage * predictor2 + fgs_attempted * predictor3 + ...
    #  We will start out with an educated guess on what are the most important factors
    #  are and then run our fitness function to adjust all of the predictors to try and
    #  find better models
    #  
    def __init__(self):
        self.points_per_game = 0
        self.fg_percentage = 0
        self.fgs_attempted = 0
        self.three_ptr_percentage = 0
        self.three_ptrs_attempted = 0
        self.offensive_rebounds = 0
        self.total_rebounds = 0
        self.assists = 0
        self.stls = 0
        self.blks = 0
        self.turnovers = 0
        self.foul = 0
        self.allowed_points = 0
        self.altering_value = 0
        self.accuracy = 0
        self.model_modifiers = [0.4, 25.0, 2.0, 15.0, 0.5, 1.5, 1.0, 0.5, 0.5, 0.5, 1.0, 0.3, 2.0]
        self.current_modifiers = [0.4, 25.0, 2.0, 15.0, 0.5, 1.5, 1.0, 0.5, 0.5, 0.5, 1.0, 0.3, 2.0]
        self.min_modifiers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.max_modifiers = [10.0, 30.0, 5.0, 25.0, 2.5, 3.5, 2.5, 2.0, 2.0, 2.0, 2.5, 1.0, 5.0]
        self.model_bracket_2014 = []
        self.model_bracket_2008 = []
        self.winning_bracket_2008 = \
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1,

             1, 0, 0, 0, 1, 1, 0, 1,
             1, 1, 0, 0, 1, 1, 0, 1,

             1, 1, 1, 0,
             1, 0, 1, 1,

             1, 1,
             1, 1,

             0, 1,

             1]
        self.winning_bracket_2014 = \
            [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1,
             1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1,

             1, 0, 1, 1, 1, 0, 0, 1,
             1, 0, 1, 0, 0, 0, 1, 0,

             1, 1, 0, 0,
             1, 0, 1, 0,

             1, 0,
             0, 1,

             0, 0,

             1]
        
    def predict_winner(self, team1_stats, team2_stats):
        self.points_per_game = team1_stats[0]
        self.fg_percentage = team1_stats[1]/team1_stats[2]
        self.fgs_attempted = team1_stats[2]
        self.three_ptr_percentage = team1_stats[4]/team1_stats[3]
        self.three_ptrs_attempted = team1_stats[3]
        self.offensive_rebounds = team1_stats[5]
        self.total_rebounds = team1_stats[6]
        self.assists = team1_stats[7]
        self.stls = team1_stats[8]
        self.blks = team1_stats[9]
        self.turnovers = team1_stats[10]
        self.foul = team1_stats[11]
        self.allowed_points = team1_stats[12]
        self.compute_v_value()

        team1_score = (pow(2.718, float(self.altering_value))) / (1 + pow(2.718, float(self.altering_value)))

        self.points_per_game = team2_stats[0]
        self.fg_percentage = team2_stats[1]/team2_stats[2]
        self.fgs_attempted = team2_stats[2]
        self.three_ptr_percentage = team2_stats[4]/team2_stats[3]
        self.three_ptrs_attempted = team2_stats[3]
        self.offensive_rebounds = team2_stats[5]
        self.total_rebounds = team2_stats[6]
        self.assists = team2_stats[7]
        self.stls = team2_stats[8]
        self.blks = team2_stats[9]
        self.turnovers = team2_stats[10]
        self.foul = team2_stats[11]
        self.allowed_points = team2_stats[12]
        self.compute_v_value()

        team2_score = (pow(2.718, float(self.altering_value))) / (1 + pow(2.718, float(self.altering_value)))

        if team1_score >= team2_score:
            return True
        else:
            return False

    def adjust_model(self):
        for position in range(0, len(self.model_modifiers) - 1):
            done = False
            while not done:
                if self.current_modifiers[position] < self.max_modifiers[position]:
                    self.current_modifiers[position] += 0.1
                    possible_model_value = self.compare_model()
                    if possible_model_value > self.accuracy:
                        self.accuracy = possible_model_value
                        self.model_modifiers[position] = self.current_modifiers[position]
                        print(self.accuracy)
                        print(*self.model_modifiers, sep=', ')
                else:
                    self.current_modifiers[position] = self.model_modifiers[position]
                    print("Our current model is: ", *self.current_modifiers, sep=', ')
                    done = True

    def adjust_model_down(self):
        for position in range(0, len(self.model_modifiers) - 1):
            done = False
            while not done:
                if self.current_modifiers[position] > self.min_modifiers[position]:
                    self.current_modifiers[position] -= 0.1
                    possible_model_value = self.compare_model()
                    if possible_model_value > self.accuracy:
                        self.accuracy = possible_model_value
                        self.model_modifiers[position] = self.current_modifiers[position]
                        print(self.accuracy)
                        print(*self.model_modifiers, sep=', ')
                else:
                    self.current_modifiers[position] = self.model_modifiers[position]
                    print("Our current model is: ", *self.current_modifiers, sep=', ')
                    done = True

    def compute_v_value(self):
        self.altering_value = (self.points_per_game * self.current_modifiers[0]
                               + self.fg_percentage * self.current_modifiers[1]
                               + self.fgs_attempted * self.current_modifiers[2]
                               + self.three_ptr_percentage * self.current_modifiers[3]
                               + self.three_ptrs_attempted * self.current_modifiers[4]
                               + self.offensive_rebounds * self.current_modifiers[5]
                               + self.total_rebounds * self.current_modifiers[6]
                               + self.assists * self.current_modifiers[7]
                               + self.stls * self.current_modifiers[8]
                               + self.blks * self.current_modifiers[9]
                               - self.turnovers * self.current_modifiers[10]
                               - self.foul * self.current_modifiers[11]
                               - self.allowed_points * self.current_modifiers[12]) / 100

    def compare_model(self):
        # self.model_bracket_2014.append(self.simulate_game('Florida', 'Albany'))
        # self.model_bracket_2014.append(self.simulate_game('Colorado', 'Pittsburgh'))
        # self.model_bracket_2014.append(self.simulate_game('VCU', 'SF Austin'))
        # self.model_bracket_2014.append(self.simulate_game('UCLA', 'Tulsa'))
        # self.model_bracket_2014.append(self.simulate_game('Ohio State', 'Dayton'))
        # self.model_bracket_2014.append(self.simulate_game('Syracuse', 'W Michigan'))
        # self.model_bracket_2014.append(self.simulate_game('New Mexico', 'Stanford'))
        # self.model_bracket_2014.append(self.simulate_game('Kansas', 'E Kentucky'))
        # self.model_bracket_2014.append(self.simulate_game('Virginia', 'Coast Carolina'))
        # self.model_bracket_2014.append(self.simulate_game('Memphis', 'G. Washington'))
        # self.model_bracket_2014.append(self.simulate_game('Cincinnati', 'Harvard'))
        # self.model_bracket_2014.append(self.simulate_game('Michigan State', 'Delaware'))
        # self.model_bracket_2014.append(self.simulate_game('North Carolina', 'Providence'))
        # self.model_bracket_2014.append(self.simulate_game('Iowa State', 'N Carolina Cent'))
        # self.model_bracket_2014.append(self.simulate_game('Connecticut', "Saint Joseph's"))
        # self.model_bracket_2014.append(self.simulate_game('Villanova', 'Milwaukee'))
        # self.model_bracket_2014.append(self.simulate_game('Arizona', 'Weber State'))
        # self.model_bracket_2014.append(self.simulate_game('Gonzaga', 'Oklahoma St'))
        # self.model_bracket_2014.append(self.simulate_game('Oklahoma', 'North Dakota St'))
        # self.model_bracket_2014.append(self.simulate_game('San Diego State', 'New Mexico St'))
        # self.model_bracket_2014.append(self.simulate_game('Baylor', 'Nebraska'))
        # self.model_bracket_2014.append(self.simulate_game('Creighton', 'LA-Lafayette'))
        # self.model_bracket_2014.append(self.simulate_game('Oregon', 'BYU'))
        # self.model_bracket_2014.append(self.simulate_game('Wisconsin', 'American U'))
        # self.model_bracket_2014.append(self.simulate_game('Wichita State', 'Cal Poly'))
        # self.model_bracket_2014.append(self.simulate_game('Kentucky', 'Kansas St'))
        # self.model_bracket_2014.append(self.simulate_game('Saint Louis', 'NC State'))
        # self.model_bracket_2014.append(self.simulate_game('Louisville', 'Manhattan'))
        # self.model_bracket_2014.append(self.simulate_game('Massachusetts', 'Tennessee'))
        # self.model_bracket_2014.append(self.simulate_game('Duke', 'Mercer'))
        # self.model_bracket_2014.append(self.simulate_game('Texas', 'Arizona State'))
        # self.model_bracket_2014.append(self.simulate_game('Michigan', 'Wofford'))
        # 
        # self.model_bracket_2014.append(self.simulate_game('Florida', 'Pittsburgh'))
        # self.model_bracket_2014.append(self.simulate_game('SF Austin', 'UCLA'))
        # self.model_bracket_2014.append(self.simulate_game('Dayton', 'Syracuse'))
        # self.model_bracket_2014.append(self.simulate_game('Stanford', 'Kansas'))
        # self.model_bracket_2014.append(self.simulate_game('Virginia', 'Memphis'))
        # self.model_bracket_2014.append(self.simulate_game('Harvard', 'Michigan State'))
        # self.model_bracket_2014.append(self.simulate_game('North Carolina', 'Iowa State'))
        # self.model_bracket_2014.append(self.simulate_game('Connecticut', 'Villanova'))
        # self.model_bracket_2014.append(self.simulate_game('Arizona', 'Gonzaga'))
        # self.model_bracket_2014.append(self.simulate_game('North Dakota St', 'San Diego State'))
        # self.model_bracket_2014.append(self.simulate_game('Baylor', 'Creighton'))
        # self.model_bracket_2014.append(self.simulate_game('Oregon', 'Wisconsin'))
        # self.model_bracket_2014.append(self.simulate_game('Wichita State', 'Kentucky'))
        # self.model_bracket_2014.append(self.simulate_game('Saint Louis', 'Louisville'))
        # self.model_bracket_2014.append(self.simulate_game('Tennessee', 'Mercer'))
        # self.model_bracket_2014.append(self.simulate_game('Texas', 'Michigan'))
        # 
        # self.model_bracket_2014.append(self.simulate_game('Florida', 'UCLA'))
        # self.model_bracket_2014.append(self.simulate_game('Dayton', 'Stanford'))
        # self.model_bracket_2014.append(self.simulate_game('Virginia', 'Michigan State'))
        # self.model_bracket_2014.append(self.simulate_game('Iowa State', 'Connecticut'))
        # self.model_bracket_2014.append(self.simulate_game('Arizona', 'San Diego State'))
        # self.model_bracket_2014.append(self.simulate_game('Baylor', 'Wisconsin'))
        # self.model_bracket_2014.append(self.simulate_game('Kentucky', 'Louisville'))
        # self.model_bracket_2014.append(self.simulate_game('Tennessee', 'Michigan'))
        # 
        # self.model_bracket_2014.append(self.simulate_game('Florida', 'Dayton'))
        # self.model_bracket_2014.append(self.simulate_game('Michigan State', 'Connecticut'))
        # self.model_bracket_2014.append(self.simulate_game('Arizona', 'Wisconsin'))
        # self.model_bracket_2014.append(self.simulate_game('Kentucky', 'Michigan'))
        # 
        # self.model_bracket_2014.append(self.simulate_game('Florida', 'Connecticut'))
        # self.model_bracket_2014.append(self.simulate_game('Wisconsin', 'Kentucky'))
        # 
        # self.model_bracket_2014.append(self.simulate_game('Connecticut', 'Kentucky'))

        self.model_bracket_2008.append(self.simulate_game('North Carolina', 'Mount St Mary\'s'))
        self.model_bracket_2008.append(self.simulate_game('Indiana', 'Arkansas'))
        self.model_bracket_2008.append(self.simulate_game('Notre Dame', 'George Mason'))
        self.model_bracket_2008.append(self.simulate_game('Washington St', 'Winthrop'))
        self.model_bracket_2008.append(self.simulate_game('Oklahoma', 'Saint Joseph\'s'))
        self.model_bracket_2008.append(self.simulate_game('Louisville', 'Boise State'))
        self.model_bracket_2008.append(self.simulate_game('Butler', 'South Alabama'))
        self.model_bracket_2008.append(self.simulate_game('Tennessee', 'American U'))
        self.model_bracket_2008.append(self.simulate_game('Kansas', 'Portland St'))
        self.model_bracket_2008.append(self.simulate_game('UNLV', 'Kent State'))
        self.model_bracket_2008.append(self.simulate_game('Clemson', 'Villanova'))
        self.model_bracket_2008.append(self.simulate_game('Vanderbilt', 'Siena'))
        self.model_bracket_2008.append(self.simulate_game('USC', 'Kansas St'))
        self.model_bracket_2008.append(self.simulate_game('Wisconsin', 'Mount St Mary\'s'))
        self.model_bracket_2008.append(self.simulate_game('Gonzaga', "Davidson"))
        self.model_bracket_2008.append(self.simulate_game('Georgetown', 'UMBC'))
        self.model_bracket_2008.append(self.simulate_game('Memphis', 'TX-Arlington'))
        self.model_bracket_2008.append(self.simulate_game('Mississippi St', 'Oregon'))
        self.model_bracket_2008.append(self.simulate_game('Michigan State', 'Temple'))
        self.model_bracket_2008.append(self.simulate_game('Pittsburgh', 'Oral Roberts'))
        self.model_bracket_2008.append(self.simulate_game('Marquette', 'Kentucky'))
        self.model_bracket_2008.append(self.simulate_game('Stanford', 'Cornell'))
        self.model_bracket_2008.append(self.simulate_game('Miami (FL)', 'Saint Mary\'s'))
        self.model_bracket_2008.append(self.simulate_game('Texas', 'Austin Peay'))
        self.model_bracket_2008.append(self.simulate_game('UCLA', 'Miss Valley St'))
        self.model_bracket_2008.append(self.simulate_game('BYU', 'Texas A&M'))
        self.model_bracket_2008.append(self.simulate_game('Drake', 'W Kentucky'))
        self.model_bracket_2008.append(self.simulate_game('Connecticut', 'San Diego'))
        self.model_bracket_2008.append(self.simulate_game('Purdue', 'Baylor'))
        self.model_bracket_2008.append(self.simulate_game('Xavier', 'Georgia'))
        self.model_bracket_2008.append(self.simulate_game('West Virginia', 'Arizona'))
        self.model_bracket_2008.append(self.simulate_game('Duke', 'Belmont'))

        self.model_bracket_2008.append(self.simulate_game('North Carolina', 'Arkansas'))
        self.model_bracket_2008.append(self.simulate_game('Notre Dame', 'Washington St'))
        self.model_bracket_2008.append(self.simulate_game('Oklahoma', 'Louisville'))
        self.model_bracket_2008.append(self.simulate_game('Butler', 'Tennessee'))
        self.model_bracket_2008.append(self.simulate_game('Kansas', 'UNLV'))
        self.model_bracket_2008.append(self.simulate_game('Villanova', 'Siena'))
        self.model_bracket_2008.append(self.simulate_game('Kansas St', 'Wisconsin'))
        self.model_bracket_2008.append(self.simulate_game('Davidson', 'Georgetown'))
        self.model_bracket_2008.append(self.simulate_game('Memphis', 'Mississippi St'))
        self.model_bracket_2008.append(self.simulate_game('Michigan State', 'Pittsburgh'))
        self.model_bracket_2008.append(self.simulate_game('Marquette', 'Stanford'))
        self.model_bracket_2008.append(self.simulate_game('Miami (FL)', 'Texas'))
        self.model_bracket_2008.append(self.simulate_game('UCLA', 'Texas A&M'))
        self.model_bracket_2008.append(self.simulate_game('W Kentucky', 'San Diego'))
        self.model_bracket_2008.append(self.simulate_game('Purdue', 'Xavier'))
        self.model_bracket_2008.append(self.simulate_game('West Virginia', 'Duke'))

        self.model_bracket_2008.append(self.simulate_game('North Carolina', 'Washington St'))
        self.model_bracket_2008.append(self.simulate_game('Louisville', 'Tennessee'))
        self.model_bracket_2008.append(self.simulate_game('Kansas', 'Villanova'))
        self.model_bracket_2008.append(self.simulate_game('Wisconsin', 'Davidson'))
        self.model_bracket_2008.append(self.simulate_game('Memphis', 'Michigan State'))
        self.model_bracket_2008.append(self.simulate_game('Stanford', 'Texas'))
        self.model_bracket_2008.append(self.simulate_game('UCLA', 'W Kentucky'))
        self.model_bracket_2008.append(self.simulate_game('Xavier', 'West Virginia'))

        self.model_bracket_2008.append(self.simulate_game('North Carolina', 'Louisville'))
        self.model_bracket_2008.append(self.simulate_game('Kansas', 'Davidson'))
        self.model_bracket_2008.append(self.simulate_game('Memphis', 'Texas'))
        self.model_bracket_2008.append(self.simulate_game('UCLA', 'Xavier'))

        self.model_bracket_2008.append(self.simulate_game('North Carolina', 'Kansas'))
        self.model_bracket_2008.append(self.simulate_game('Memphis', 'UCLA'))

        self.model_bracket_2008.append(self.simulate_game('Kansas', 'Memphis'))
        success = 0
        if len(self.model_bracket_2008) == len(self.winning_bracket_2008):
            for iterator in range(0, len(self.model_bracket_2008)):
                if self.model_bracket_2008[iterator] == self.winning_bracket_2008[iterator]:
                    success += 1
        else:
            print("Error!  Length of Model and Winner Brackets are not equal!")

        accuracy_of_model = success/len(self.model_bracket_2008)
        self.model_bracket_2008 = []
        return accuracy_of_model

    def simulate_game(self, team1_name, team2_name):
        year = 2008
        stats_class.populate_game_stats(team1_name, year)
        stats_class.create_stats(team1_name, year)
        stats_class.populate_game_stats(team2_name, year)
        stats_class.create_stats(team2_name, year)

        result = self.predict_winner(stats_class.get_team_season_averages(team1_name, year),
                                     stats_class.get_team_season_averages(team2_name, year))

        return result

    def print_model(self):
        print(*self.model_modifiers, sep=', ')
        print(self.accuracy)
