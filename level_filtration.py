

BREAKEDOWN_DIF = 0.01

def levels_audite(prelevels, dayly_bars, dif = BREAKEDOWN_DIF):
    low_prelevels, high_prelevels = prelevels
    good_highlevels = []
    good_lowlevels = []
    # логика детекта пробоя уровня поддержки
    for prelevel in low_prelevels:
        lastbar_index = dayly_bars.index(prelevel[-2])
        prelevel_cost = prelevel[-1]
        for dayly_bar_index in range(lastbar_index +1, len(dayly_bars)):
            if dayly_bars[dayly_bar_index].get("close") < prelevel_cost * (1-dif):
                break
        else:
            good_lowlevels.append(prelevel)

    # логика детекта уровней сопротивления

    for prelevel in high_prelevels:
        lastbar_index = dayly_bars.index(prelevel[-2])
        prelevel_cost = prelevel[-1]
        for dayly_bar_index in range(lastbar_index+1, len(dayly_bars)):
            if dayly_bars[dayly_bar_index].get("close") > prelevel_cost * (1+dif):
                break
        else:
            good_highlevels.append(prelevel)

    return [good_lowlevels, good_highlevels]

