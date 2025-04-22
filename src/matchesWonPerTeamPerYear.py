def matchesWonPerTeamPerYear(matches) :
    result = {}
    for match in matches :
        season  = match['season']
        team = match['winner']
        if season not in result :
            result[season] = {}
            
        if team in result[season] :
            result[season][team] += 1
        else:
            result[season][team] = 1
    return result