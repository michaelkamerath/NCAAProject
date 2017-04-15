from math import expm1, fabs


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

        self.altering_value = self.points_per_game * self.points_predictor + self.fg_percentage * self.fg_percentage_predictor \
                              + self.fgs_attempted * self.fgs_attempted_predictor + self.three_ptr_percentage * self.three_ptr_percentage_predictor \
                              + self.three_ptrs_attempted * self.three_ptrs_attempted_predictor + self.offensive_rebounds * self.offensive_rebounds_predictor \
                              + self.total_rebounds * self.total_self.rebounds_predictor + self.assists * self.assists_predictor + self.stls * self.stls_predictor \
                              + self.blks * self.blks_predictor + self.turnovers * self.turnovers_predictor + self.foul * self.foul_predictor \
                              - self.allowed_points * self.allowed_points_predictor

    def predict_winner(self, team1_stats, team2_stats):
        return True

    def adjust_model(self):
        return 0
