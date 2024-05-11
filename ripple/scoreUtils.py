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

def readableMods(__mods):
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