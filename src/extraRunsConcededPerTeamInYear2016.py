def extraRunsConcededPerTeamInYear2016(matches, deliveries) :
    print("this is the problem for extraRunsConcededPerTeamInYear2016")
    matchIdsOf2016 = set()
    for match in matches:
        if match['season'] == '2016' :
            matchIdsOf2016.add(match['id'])
            
    result = {}
    for delivery in deliveries :
        if delivery['match_id'] in matchIdsOf2016 :
            team = delivery['bowling_team']
            extraRuns = int(delivery['extra_runs'])
            
            if team in result :
                result[team] += extraRuns
            else :
                result[team] = extraRuns
    return result