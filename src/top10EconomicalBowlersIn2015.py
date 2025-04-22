def top10EconomicalBowlersIn2015(matches, deliveries):
    # Step 1: Collect all match IDs from 2015
    
    print("this is the answer for the top10EconomicalBowlersIn2015 ")
    matchIds2015 = set()
    for match in matches:
        if match['season'] == '2015':
            matchIds2015.add(match['id'])

    # Step 2: Track runs conceded and legal deliveries
    runs_conceded = {}
    balls_bowled = {}

    for delivery in deliveries:
        if delivery['match_id'] in matchIds2015:
            bowler = delivery['bowler']
            total_runs = int(delivery['total_runs'])
            wide_runs = int(delivery['wide_runs'])
            noball_runs = int(delivery['noball_runs'])

            # Count legal deliveries
            if wide_runs == 0 and noball_runs == 0:
                if bowler in balls_bowled:
                    balls_bowled[bowler] += 1
                else:
                    balls_bowled[bowler] = 1

            # Count all runs conceded
            if bowler in runs_conceded:
                runs_conceded[bowler] += total_runs
            else:
                runs_conceded[bowler] = total_runs


    # Step 3: Calculate economy for each bowler
    economy = {}
    for bowler in runs_conceded:
        if bowler in balls_bowled:
            overs = balls_bowled[bowler] / 6
            econ = runs_conceded[bowler] / overs
            economy[bowler] = round(econ, 2)

    # Step 4: Sort by economy and get top 10
    top10 = dict(sorted(economy.items(), key=lambda x: x[1])[:10])
    return top10
