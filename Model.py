from collections import defaultdict


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
        self.altering_value = 0
        self.accuracy = 0
        self.model_modifiers = [4.0, 25.0, 2.0, 15.0, 1.0, 1.5, 1.0, 0.5, 0.5, 0.5, 1.0, 0.3, 2.0]
        self.current_modifiers = [4.0, 25.0, 2.0, 15.0, 1.0, 1.5, 1.0, 0.5, 0.5, 0.5, 1.0, 0.3, 2.0]
        self.max_modifiers = [10.0, 30.0, 5.0, 25.0, 2.5, 3.5, 2.5, 2.0, 2.0, 2.0, 2.5, 1.0, 5.0]

    def predict_winner(self, team1_stats, team2_stats):
        team1_score = 0
        team2_score = 0
        print("Team 1 Average Season Stats:")
        print(team1_stats)
        print("Team 2 Average Season Stats: ")
        print(team2_stats)

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
        for position, element in enumerate(self.model_modifiers):
            if self.current_modifiers[position] < self.max_modifiers[position]:
                self.current_modifiers[position] += 0.1
                possible_model_value = self.compare_model()
                if possible_model_value > self.accuracy:
                    self.accuracy = possible_model_value
                    self.model_modifiers[position] = self.current_modifiers[position]

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
