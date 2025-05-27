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
	if gameMode == 0: return "std"
	elif gameMode == 1: return "taiko"
	elif gameMode == 2: return "ctb"
	else: return "mania"

def readableMods(__mods: int) -> str:
	"""
	Return a string with readable std mods.
	Used to convert a mods number for oppai

	:param __mods: mods bitwise number
	:return: readable mods string, eg HDDT
	"""
	r = ""
	if __mods == mods.NOMOD: return ""
	if __mods & mods.NOFAIL: r += "NF"
	if __mods & mods.EASY: r += "EZ"
	if __mods & mods.TOUCHSCREEN: r += "TD" #(NV)
	if __mods & mods.HIDDEN: r += "HD"
	if __mods & mods.HARDROCK: r += "HR"
	if __mods & mods.SUDDENDEATH: r += "SD"
	if __mods & mods.DOUBLETIME: r += "DT"
	if __mods & mods.RELAX: r += "RX"
	if __mods & mods.HALFTIME: r += "HT"
	if __mods & mods.NIGHTCORE: r = r.replace("DT", "NC") if "DT" in r else r + "NC" #576 = DT, NC
	if __mods & mods.FLASHLIGHT: r += "FL"
	if __mods & mods.AUTOPLAY: r += "AT"
	if __mods & mods.SPUNOUT: r += "SO"
	if __mods & mods.RELAX2: r += "AP"
	if __mods & mods.PERFECT: r = r.replace("SD", "PF") if "SD" in r else r + "PF" #16416 = SD, PF
	if __mods & mods.KEY4: r += "K4"
	if __mods & mods.KEY5: r += "K5"
	if __mods & mods.KEY6: r += "K6"
	if __mods & mods.KEY7: r += "K7"
	if __mods & mods.KEY8: r += "K8"
	#if __mods & mods.KEYMOD: r += "KEYMOD" #?
	if __mods & mods.FADEIN: r += "FI"
	if __mods & mods.RANDOM: r += "RD"
	#if __mods & mods.LASTMOD: r += "LASTMOD" #?
	if __mods & mods.KEY9: r += "K9"
	if __mods & mods.COOP: r += "CP"
	if __mods & mods.KEY1: r += "K1"
	if __mods & mods.KEY3: r += "K3"
	if __mods & mods.KEY2: r += "K2"
	if __mods & mods.SCOREV2: r += "V2" #(SV2)
	if __mods & mods.MIRROR: r += "MR"
	return r

def readableModsReverse(__mods: str) -> int:
	modsEnum = 0
	for r in [__mods[i:i+2].upper() for i in range(0, len(__mods), 2)]:
		if r not in ["NO", "NF", "EZ", "TD", "HD", "HR", "SD", "DT", "HT", "NC", "FL", "SO", "PF", "RX", "AP", "K4", "K5", "K6", "K7", "K8", "FI", "RD", "K9", "CP", "K1", "K3", "K2", "V2", "MR"]:
			return "Invalid mods. Allowed mods: NO, NF, EZ, TD(NV), HD, HR, SD, DT, HT, NC, FL, SO, PF, RX, AP, K4, K5, K6, K7, K8, FI, RD, K9, CP, K1, K3, K2, V2(SV2), MR. Do not use spaces for multiple mods."
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
		elif r == "NC": modsEnum += mods.NIGHTCORE + mods.DOUBLETIME #576 #576 = DT, NC
		elif r == "FL": modsEnum += mods.FLASHLIGHT
		elif r == "AT": modsEnum += mods.AUTOPLAY
		elif r == "SO": modsEnum += mods.SPUNOUT
		elif r == "AP": modsEnum += mods.RELAX2
		elif r == "PF": modsEnum += mods.PERFECT + mods.SUDDENDEATH #16416 #16416 = SD, PF
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
		elif r == "CP": modsEnum += mods.COOP
		elif r == "K1": modsEnum += mods.KEY1
		elif r == "K3": modsEnum += mods.KEY3
		elif r == "K2": modsEnum += mods.KEY2
		elif r == "V2": modsEnum += mods.SCOREV2
		elif r == "MR": modsEnum += mods.MIRROR
	return modsEnum