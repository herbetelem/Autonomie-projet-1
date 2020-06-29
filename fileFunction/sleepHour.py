def sleepHour(nbHeure, statSommeil, statSoif, statFaim):
    statSommeil = statSommeil + nbHeure * 6
    statFaim = statFaim - nbHeure * 1
    statSoif = statSoif - nbHeure * 2
    return statSommeil, statFaim, statSoif