from common.constants import mods
from objects import glob

def isRankable(m):
	"""
	Checks if `m` contains unranked mods

	:param m: mods enum
	:return: True if there are no unranked mods in `m`, else False
	"""
	# I am a wizard.... feel free to make sense of this and do a better job (merge req are welcome)
	if "_unranked-mods" not in glob.conf.extra:
		glob.conf.extra["_unranked-mods"] = sum([getattr(mods, key) for key, value in
												glob.conf.extra["common"]["rankable-mods"].items() if not value
												]) # Store the unranked mods mask into glob

	# I know bitmasks... so get that old trash out of here ktnxbye
	return m & ~glob.conf.extra["_unranked-mods"] == m and m & 8320 != 8320

def readableGameMode(gameMode):
	"""
	Convert numeric gameMode to a readable format. Can be used for db too.

	:param gameMode:
	:return:
	"""
	# TODO: Same as common.constants.gameModes.getGameModeForDB, remove one
	if gameMode == 0:
		return "std"
	elif gameMode == 1:
		return "taiko"
	elif gameMode == 2:
		return "ctb"
	else:
		return "mania"

def readableMods(__mods: int):
	"""
	Return a string with readable std mods.
	Used to convert a mods number for oppai

	:param __mods: mods bitwise number
	:return: readable mods string, eg HDDT
	"""
	r = ""
	if __mods == mods.NOMOD: return r
	if __mods & mods.NOFAIL > 0: r += "NF"
	if __mods & mods.EASY > 0: r += "EZ"
	if __mods & mods.TOUCHSCREEN > 0: r += "TD"
	if __mods & mods.HIDDEN > 0: r += "HD"
	if __mods & mods.HARDROCK > 0: r += "HR"
	if __mods & mods.SUDDENDEATH > 0: r += "SD"
	if __mods & mods.DOUBLETIME > 0: r += "DT"
	if __mods & mods.RELAX > 0: r += "RX"
	if __mods & mods.HALFTIME > 0: r += "HT"
	if __mods & mods.NIGHTCORE > 0 or __mods & 576 > 0: r = r.replace("DT", "NC") #576 = DT, NC
	if __mods & mods.FLASHLIGHT > 0: r += "FL"
	if __mods & mods.AUTOPLAY > 0: r += "AU(AUTO)"
	if __mods & mods.SPUNOUT > 0: r += "SO"
	if __mods & mods.RELAX2 > 0: r += "AP"
	if __mods & mods.PERFECT > 0 or __mods & 16416 > 0: r = r.replace("SD", "PF") #16416 = SD, PF
	if __mods & mods.KEY4 > 0: r += "K4"
	if __mods & mods.KEY5 > 0: r += "K5"
	if __mods & mods.KEY6 > 0: r += "K6"
	if __mods & mods.KEY7 > 0: r += "K7"
	if __mods & mods.KEY8 > 0: r += "K8"
	if __mods & mods.KEYMOD > 0: r += "KEYMOD" #?
	if __mods & mods.FADEIN > 0: r += "FI"
	if __mods & mods.RANDOM > 0: r += "RD"
	if __mods & mods.LASTMOD > 0: r += "LASTMOD" #?
	if __mods & mods.KEY9 > 0: r += "K9"
	if __mods & mods.KEY10 > 0: r += "K10"
	if __mods & mods.KEY1 > 0: r += "K1"
	if __mods & mods.KEY3 > 0: r += "K3"
	if __mods & mods.KEY2 > 0: r += "K2"
	if __mods & mods.SCOREV2 > 0: r += "SV2(v2)"
	if __mods & mods.MIRROR > 0: r += "MR"
	return r

def readableModsReverse(__mods: str):
    if len(__mods.upper().replace("K10", "")) % 2: __mods = "^^"
    if "K10" in __mods: __mods = __mods.replace("K10", "") + "K10"
    modsEnum = 0
    for r in [__mods[i:i+3].upper() if __mods[i:i+3].upper() == "K10" else __mods[i:i+2].upper() for i in range(0, len(__mods) if not "K10" in __mods else len(__mods) - 1, 2)]:
        if r not in ["NO", "NF", "EZ", "TD", "HD", "HR", "SD", "DT", "HT", "NC", "FL", "SO", "PF", "RX", "AP", "K4", "K5", "K6", "K7", "K8", "FI", "RD", "K9", "K10", "K1", "K3", "K2", "v2", "MR"]:
            return "Invalid mods. Allowed mods: NO, NF, EZ, TD, HD, HR, SD, DT, HT, NC, FL, SO, PF, RX, AP, K4, K5, K6, K7, K8, FI, RD, K9, K10, K1, K3, K2, v2(SV2), MR. Do not use spaces for multiple mods."
        if r == "NO": return 0
        elif r == "NF": modsEnum += mods.NOFAIL
        elif r == "EZ": modsEnum += mods.EASY
        elif r == "TD": modsEnum += mods.TOUCHSCREEN
        elif r == "HD": modsEnum += mods.HIDDEN
        elif r == "HR": modsEnum += mods.HARDROCK
        elif r == "SD": modsEnum += mods.SUDDENDEATH
        elif r == "DT": modsEnum += mods.DOUBLETIME
        elif r == "RX": modsEnum += mods.RELAX
        elif r == "HT": modsEnum += mods.HALFTIME
        elif r == "NC": modsEnum += 576 #576 = DT, NC
        elif r == "FL": modsEnum += mods.FLASHLIGHT
        elif r == "AT": modsEnum += mods.AUTOPLAY
        elif r == "SO": modsEnum += mods.SPUNOUT
        elif r == "AP": modsEnum += mods.RELAX2
        elif r == "PF": modsEnum += 16416 #16416 = SD, PF
        elif r == "K4": modsEnum += mods.KEY4
        elif r == "K5": modsEnum += mods.KEY5
        elif r == "K6": modsEnum += mods.KEY6
        elif r == "K7": modsEnum += mods.KEY7
        elif r == "K8": modsEnum += mods.k8
        #elif r == "KEYMOD": modsEnum += mods.KEYMOD
        elif r == "FI": modsEnum += mods.FADEIN
        elif r == "RD": modsEnum += mods.RANDOM
        #elif r == "LASTMOD": modsEnum += mods.LASTMOD
        elif r == "K9": modsEnum += mods.KEY9
        elif r == "K10": modsEnum += mods.KEY10
        elif r == "K1": modsEnum += mods.KEY1
        elif r == "K3": modsEnum += mods.KEY3
        elif r == "K2": modsEnum += mods.KEY2
        elif r == "v2": modsEnum += mods.SCOREV2
        elif r == "MR": modsEnum += mods.MIRROR
    return modsEnum