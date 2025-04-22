def teamWonTossAndMatches(matches):
    result = {}
    for match in matches :
        tossWin = match['toss_winner']
        matchWinner = match['winner']
        if tossWin == matchWinner :
            if tossWin in  result :
                result[tossWin] += 1
            else :
                result[tossWin] = 1
    return result