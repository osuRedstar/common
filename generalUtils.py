import string
import random
import hashlib
from functools import partial
from common.log import logUtils as log

import dill

from common.constants import mods
from time import localtime, strftime

def randomString(length = 8):
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

def stringToBool(s):
	"""
	Convert a string (True/true/1) to bool

	:param s: string/int value
	:return: True/False
	"""
	return s == "True" or s == "true" or s == "1" or s == 1

def fileMd5(filename):
	"""
	Return filename's md5

	:param filename: name of the file
	:return: file md5
	"""
	with open(filename, mode='rb') as f:
		d = hashlib.md5()
		for buf in iter(partial(f.read, 128), b''):
			d.update(buf)
	return d.hexdigest()

def stringMd5(s):
	"""
	Return string's md5

	:param s: input string
	:return: `string`'s md5
	"""
	d = hashlib.md5()
	d.update(s.encode("utf-8"))
	return d.hexdigest()

def getAcc(play_mode: int, count_300: int, count_100: int, count_50: int, gekis_count: int, katus_count: int, misses_count: int) -> int:
	if play_mode == 0: #Std
		total_notes = count_300 + count_100 + count_50 + misses_count
		accuracy = (300 * count_300 + 100 * count_100 + 50 * count_50) / (300 * total_notes) * 100
	elif play_mode == 1: #Taiko
		total_notes = count_300 + count_100 + misses_count
		accuracy = (count_300 + 0.5 * count_100) / total_notes * 100
	elif play_mode == 2: #CTB
		total_notes = count_300 + count_100 + count_50 + misses_count + katus_count #+ gekis_count + katus_count
		accuracy = (count_300 + count_100 + count_50) / total_notes * 100
	elif play_mode == 3: #Mania
		total_notes = gekis_count + count_300 + katus_count + count_100 + count_50 + misses_count
		accuracy = (300 * (gekis_count + count_300) + 200 * katus_count + 100 * count_100 + 50 * count_50) / (300 * total_notes) * 100
	else: accuracy = 0 #?
	return accuracy

def getRank(gameMode=None, __mods=None, acc=None, c300=None, c100=None, c50=None, cmiss=None, *, score_=None):
	"""
	Return a string with rank/grade for a given score.
	Used mainly for tillerino

	:param gameMode: game mode number
	:param __mods: mods value
	:param acc: accuracy
	:param c300: 300 hit count
	:param c100: 100 hit count
	:param c50: 50 hit count
	:param cmiss: misses count
	:param score_: score object. Optional.
	:return: rank/grade string
	"""
	if score_ is not None:
		return getRank(score_.gameMode, score_.mods, score_.accuracy, score_.c300, score_.c100, score_.c50, score_.cMiss)
	total = c300 + c100 + c50 + cmiss
	hdfl = (__mods & mods.HIDDEN > 0) or (__mods & mods.FLASHLIGHT > 0)

	def ss():
		return "XH" if hdfl else "X"

	def s():
		return "SH" if hdfl else "S"

	if gameMode == 0:
		# osu!std
		if acc == 100:
			return ss()
		if c300 / total > 0.90 and c50 / total < 0.1 and cmiss == 0:
			return s()
		if (c300 / total > 0.80 and cmiss == 0) or (c300 / total > 0.90):
			return "A"
		if (c300 / total > 0.70 and cmiss == 0) or (c300 / total > 0.80):
			return "B"
		if c300 / total > 0.60:
			return "C"
		return "D"
	elif gameMode == 1:
		# TODO: taiko rank
		return "A"
	elif gameMode == 2:
		# CtB
		if acc == 100:
			return ss()
		if 98.01 <= acc <= 99.99:
			return s()
		if 94.01 <= acc <= 98.00:
			return "A"
		if 90.01 <= acc <= 94.00:
			return "B"
		if 98.01 <= acc <= 90.00:
			return "C"
		return "D"
	elif gameMode == 3:
		# osu!mania
		if acc == 100:
			return ss()
		if acc > 95:
			return s()
		if acc > 90:
			return "A"
		if acc > 80:
			return "B"
		if acc > 70:
			return "C"
		return "D"

	return "A"

def getTimestamp():
	"""
	Return current time in YYYY-MM-DD HH:MM:SS format.
	Used in logs.

	:return: readable timestamp
	"""
	return strftime("%Y-%m-%d %H:%M:%S", localtime())

def hexString(s):
	"""
	Output `s`'s bytes in DEX
	:param s: string
	:return: string with HEX values
	"""
	return ":".join("{:02x}".format(ord(str(c))) for c in s)

def strContains(s, w):
	"""
	Check if `w` is in `s`

	:param s: haystack
	:param w: needle
	:return: True if `w` is in `s`, otherwise False
	"""
	return (' ' + w + ' ') in (' ' + s + ' ')

def getTotalSize(o):
	"""
	Get approximate object size using dill

	:param o: object
	:return: approximate bytes size
	"""
	try:
		return len(dill.dumps(o, recurse=True))
	except:
		log.error("Error while getting total object size!")
		return 0