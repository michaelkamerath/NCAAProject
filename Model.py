from math import expm1, fabs
import TeamStatistics as ts

stats_class = ts.TeamStatistics()
stats_class.read_in_data()

class Model(object):
    # Our model is in the form Win Percentage = e^v / 1 + e^v
    # In this case, our v is:
    #  points * predictor1 + fg_percentage * predictor2 + fgs_attempted * predictor3 + ...
    #  We will start out with an educated guess on what are the most important factors
    #  are and then run our fitness function to adjust all of the predictors to try and
    #  find better models
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
        self.points_predictor = 4.0
        self.fg_percentage_predictor = 25.0
        self.fgs_attempted_predictor = 2.0
        self.three_ptr_percentage_predictor = 15.0
        self.three_ptrs_attempted_predictor = 1.0
        self.offensive_rebounds_predictor = 1.5
        self.total_rebounds_predictor = 1.0
        self.assists_predictor = .5
        self.stls_predictor = .5
        self.blks_predictor = .5
        self.turnovers_predictor = 1.0
        self.foul_predictor = .3
        self.allowed_points_predictor = 2.0
        
        self.altering_value = 0

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
        return 0

    def compute_v_value(self):
        self.altering_value = (self.points_per_game * self.points_predictor + self.fg_percentage * self.fg_percentage_predictor \
                              + self.fgs_attempted * self.fgs_attempted_predictor + self.three_ptr_percentage * self.three_ptr_percentage_predictor \
                              + self.three_ptrs_attempted * self.three_ptrs_attempted_predictor + self.offensive_rebounds * self.offensive_rebounds_predictor \
                              + self.total_rebounds * self.total_rebounds_predictor + self.assists * self.assists_predictor + self.stls * self.stls_predictor \
                              + self.blks * self.blks_predictor + self.turnovers * self.turnovers_predictor + self.foul * self.foul_predictor \
                              - self.allowed_points * self.allowed_points_predictor) / 100


    def compare_model(self):
        winning_bracket_2014 = [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1,
                                1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1,

                                1, 0, 1, 1, 1, 0, 0, 1,
                                1, 0, 1, 0, 0, 0, 1, 0,

                                1, 1, 0, 0,
                                1, 0, 1, 0,

                                1, 0,
                                0, 1,

                                0,
                                0,

                                1]
        model_bracket_2014 = []

        model_bracket_2014.append(self.simulate_game('Florida', 'Albany'))
        model_bracket_2014.append(self.simulate_game('Colorado', 'Pittsburgh'))
        model_bracket_2014.append(self.simulate_game('VCU', 'SF Austin'))
        model_bracket_2014.append(self.simulate_game('UCLA', 'Tulsa'))
        model_bracket_2014.append(self.simulate_game('Ohio State', 'Dayton'))
        model_bracket_2014.append(self.simulate_game('Syracuse', 'W Michigan'))
        model_bracket_2014.append(self.simulate_game('New Mexico', 'Stanford'))
        model_bracket_2014.append(self.simulate_game('Kansas', 'E Kentucky'))
        model_bracket_2014.append(self.simulate_game('Virginia', 'Coast Carolina'))
        model_bracket_2014.append(self.simulate_game('Memphis', 'G. Washington'))
        model_bracket_2014.append(self.simulate_game('Cincinnati', 'Harvard'))
        model_bracket_2014.append(self.simulate_game('Michigan State', 'Delaware'))
        model_bracket_2014.append(self.simulate_game('North Carolina', 'Providence'))
        model_bracket_2014.append(self.simulate_game('Iowa State', 'N Carolina Cent'))
        model_bracket_2014.append(self.simulate_game('Connecticut', "Saint Joseph's"))
        model_bracket_2014.append(self.simulate_game('Villanova', 'Milwaukee'))
        model_bracket_2014.append(self.simulate_game('Arizona', 'Weber State'))
        model_bracket_2014.append(self.simulate_game('Gonzaga', 'Oklahoma St'))
        model_bracket_2014.append(self.simulate_game('Oklahoma', 'North Dakota St'))
        model_bracket_2014.append(self.simulate_game('San Diego State', 'New Mexico St'))
        model_bracket_2014.append(self.simulate_game('Baylor', 'Nebraska'))
        model_bracket_2014.append(self.simulate_game('Creighton', 'LA-Lafayette'))
        model_bracket_2014.append(self.simulate_game('Oregon', 'BYU'))
        model_bracket_2014.append(self.simulate_game('Wisconsin', 'American U'))
        model_bracket_2014.append(self.simulate_game('Wichita State', 'Cal Poly'))
        model_bracket_2014.append(self.simulate_game('Kentucky', 'Kansas St'))
        model_bracket_2014.append(self.simulate_game('Saint Louis', 'NC State'))
        model_bracket_2014.append(self.simulate_game('Louisville', 'Manhattan'))
        model_bracket_2014.append(self.simulate_game('Massachusetts', 'Tennessee'))
        model_bracket_2014.append(self.simulate_game('Duke', 'Mercer'))
        model_bracket_2014.append(self.simulate_game('Texas', 'Arizona State'))
        model_bracket_2014.append(self.simulate_game('Michigan', 'Wofford'))

        model_bracket_2014.append(self.simulate_game('Florida', 'Pittsburgh'))
        model_bracket_2014.append(self.simulate_game('SF Austin', 'UCLA'))
        model_bracket_2014.append(self.simulate_game('Dayton', 'Syracuse'))
        model_bracket_2014.append(self.simulate_game('Stanford', 'Kansas'))
        model_bracket_2014.append(self.simulate_game('Virginia', 'Memphis'))
        model_bracket_2014.append(self.simulate_game('Harvard', 'Michigan State'))
        model_bracket_2014.append(self.simulate_game('North Carolina', 'Iowa State'))
        model_bracket_2014.append(self.simulate_game('Connecticut', 'Villanova'))
        model_bracket_2014.append(self.simulate_game('Arizona', 'Gonzaga'))
        model_bracket_2014.append(self.simulate_game('North Dakota St', 'San Diego State'))
        model_bracket_2014.append(self.simulate_game('Baylor', 'Creighton'))
        model_bracket_2014.append(self.simulate_game('Oregon', 'Wisconsin'))
        model_bracket_2014.append(self.simulate_game('Wichita State', 'Kentucky'))
        model_bracket_2014.append(self.simulate_game('Saint Louis', 'Louisville'))
        model_bracket_2014.append(self.simulate_game('Tennessee', 'Mercer'))
        model_bracket_2014.append(self.simulate_game('Texas', 'Michigan'))

        model_bracket_2014.append(self.simulate_game('Florida', 'UCLA'))
        model_bracket_2014.append(self.simulate_game('Dayton', 'Stanford'))
        model_bracket_2014.append(self.simulate_game('Virginia', 'Michigan State'))
        model_bracket_2014.append(self.simulate_game('Iowa State', 'Connecticut'))
        model_bracket_2014.append(self.simulate_game('Arizona', 'San Diego State'))
        model_bracket_2014.append(self.simulate_game('Baylor', 'Wisconsin'))
        model_bracket_2014.append(self.simulate_game('Kentucky', 'Louisville'))
        model_bracket_2014.append(self.simulate_game('Tennessee', 'Michigan'))

        model_bracket_2014.append(self.simulate_game('Florida', 'Dayton'))
        model_bracket_2014.append(self.simulate_game('Michigan State', 'Connecticut'))
        model_bracket_2014.append(self.simulate_game('Arizona', 'Wisconsin'))
        model_bracket_2014.append(self.simulate_game('Kentucky', 'Michigan'))

        model_bracket_2014.append(self.simulate_game('Florida', 'Connecticut'))
        model_bracket_2014.append(self.simulate_game('Wisconsin', 'Kentucky'))

        model_bracket_2014.append(self.simulate_game('Connecticut', 'Kentucky'))

        success = 0

        if len(model_bracket_2014) == len(winning_bracket_2014):
            for iterator in range(0, len(model_bracket_2014)):
                if model_bracket_2014[iterator] == winning_bracket_2014[iterator]:
                    success += 1
        else:
            print("Error!  Length of Model and Winner Brackets are not equal!")

        accuracy_of_model = success/len(model_bracket_2014)

        return accuracy_of_model


    def simulate_game(self, team1_name, team2_name):
        year = 2014
        stats_class.populate_game_stats(team1_name, year)
        stats_class.create_stats(team1_name, year)
        stats_class.populate_game_stats(team2_name, year)
        stats_class.create_stats(team2_name, year)

        result = self.predict_winner(stats_class.season_averages[team1_name, year],
                                      stats_class.season_averages[team2_name, year])

        return result
