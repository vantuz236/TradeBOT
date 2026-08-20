import recon
#[{'time': 1777507200000, 'open': 75780.0, 'high': 76669.14, 'low': 75323.65, 'close': 76346.57, 'volume': 10381.81607},
DIF = 0.1

dayly_bars = recon.get_all_frames("BTCUSDT").get("d")

def ext_search(bars):
    high_exts = []
    low_exts = []
    exts = []
    for bar in range(1, len(bars) -1):
        if bars[bar-1].get("high") < bars[bar].get("high") > bars[bar+1].get("high"):
            high_exts.append(bars[bar])
        if bars[bar-1].get("low") > bars[bar].get("low") < bars[bar+1].get("low"):
            low_exts.append(bars[bar])

    exts.append(low_exts)
    exts.append(high_exts)
    return exts


def get_prelevel(exts):
    high_levels = [[exts[1][0]]]
    low_levels = [[exts[0][0]]]
    for bar in exts[1][1:]:
        for group in high_levels:
            group_price = sum([x.get("high") for x in group])/len(group)
            if group_price * (1 - DIF) < bar.get("high") < group_price * (1+DIF):
                group.append(bar)
                break
            high_levels.append([bar])





#print(get_level(ext_search(dayly_bars)))
