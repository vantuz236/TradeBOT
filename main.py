import recon
import level_detector
import level_filtration

def main():
    dayly_bars = recon.get_all_frames("BTCUSDT").get("d")
    exts = level_detector.ext_search(dayly_bars)
    prelevels = level_detector.get_prelevel(exts)
    good_low_levels, good_high_levels = level_filtration.levels_audite(prelevels, dayly_bars)
    #goodlevels_prices = [x[-1] for x in goodlevels]
    lowprices = [x[-1] for x in good_low_levels]
    highprices = [x[-1] for x in good_high_levels]

    return [lowprices, highprices]

print(main())