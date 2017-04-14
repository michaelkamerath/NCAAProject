from math import expm1, fabs
class Model(object):
    # Our model is in the form Win Percentage = e^v / 1 + e^v
    # In this case, our v is:
    #  points * predictor1 + fg_percentage * predictor2 + fgs_attempted * predictor3 + ...
    #  We will start out with an educated guess on what are the most important factors
    #  are and then run our fitness function to adjust all of the predictors to try and
    #  find better models
    def __init__(self):
        points_per_game = 0
        fg_percentage = 0
        fgs_attempted = 0
        three_ptr_percentage = 0
        three_ptrs_attempted = 0
        offensive_rebounds = 0
        total_rebounds = 0
        assists = 0
        stls = 0
        blks = 0
        turnovers = 0
        foul = 0
        allowed_points = 0
        points_predictor = 4.0
        fg_percentage_predictor = 25.0
        fgs_attempted_predictor = 2.0
        three_ptr_percentage_predictor = 15.0
        three_ptrs_attempted_predictor = 1.0
        offensive_rebounds_predictor = 1.5
        total_rebounds_predictor = 1.0
        assists_predictor = .5
        stls_predictor = .5
        blks_predictor = .5
        turnovers_predictor = 1.0
        foul_predictor = .3
        allowed_points_predictor = 2.0

        altering_value = points_per_game * points_predictor + fg_percentage * fg_percentage_predictor \
                        + fgs_attempted * fgs_attempted_predictor + three_ptr_percentage * three_ptr_percentage_predictor \
                        + three_ptrs_attempted * three_ptrs_attempted_predictor + offensive_rebounds * offensive_rebounds_predictor \
                        + total_rebounds * total_rebounds_predictor + assists * assists_predictor + stls * stls_predictor \
                        + blks * blks_predictor + turnovers * turnovers_predictor + foul * foul_predictor \
                        + allowed_points * allowed_points_predictor

        team1_percentage = expm1(altering_value) / (1 + expm1(altering_value))
        team2_percentage = expm1(altering_value) / (1 + expm1(altering_value))

        model = expm1(fabs(team2_percentage - team1_percentage)) / (1 + expm1(team2_percentage - team1_percentage))


    def adjust_model(self):
        return 0

