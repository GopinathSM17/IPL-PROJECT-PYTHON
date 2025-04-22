def matchesPerSeason(matches):
    result = {}
    for match in matches :
        season = match['season']
        if season in result :
            result[season] += 1
        else :
            result[season] = 1
    return result