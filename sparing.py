def fondskonto(c0, i, r, andel):
    c = c0 + i
    c *= (andel * r[0] + (1-andel) * r[1])
    return c

