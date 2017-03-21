--- Example Queries ---
--- Gets points from the home and opposing team ---
SELECT a.team, a.opponent, a.pts, a.pts_allowed
	FROM all_stats AS a;

--- Gets the teams and opponents, both of their field goal
--- percentages and if the hometeam won where the home team
--- had greater than 40 percent shooting and the away team
--- had less than 30 percent shooting
SELECT a.team,
	   a.opponent,
       a.fgm/a.fga AS 'Home FG Percentage',
       a.opp_fgm/a.opp_fga AS 'Away FG Percentage',
       a.pts > a.pts_allowed AS 'Hometeam Win'
	FROM all_stats AS a
    WHERE a.fgm/a.fga > 0.40
    AND  a.opp_fgm/a.opp_fga < 0.30;

--- Gets the team, opponent, seeds of both teams, round
--- and whether the number one seed won. NOTE: the higher
--- seed is always the home team so this is all of the games
--- that one seeds played in.
SELECT a.team,
	   a.opponent,
       a.Home_Seed,
       a.Away_Seed,
       a.Round,
       a.pts > a.pts_allowed as 'Hometeam Win'
	FROM all_stats AS a
    WHERE a.Home_Seed = 1;