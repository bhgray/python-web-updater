#!/usr/local/bin/python

#updater v. 1.0

# updater creates a new file from a template, changes the dates and calculates
# class meetings.
# To do:  	upload to server;  get/change syllabus page; add/process cw and other
#			comments automatically
#			updater -c cs3 -t moncw -s "<b>Lab 202:</b> lab0923 today"
#				this call would get the version from the server, and replace
#				the moncw tag with the string shown.
#			updater -c cs3 -a "Test on friday!!!"
#				this call would get the homepage from the server (cs3syll.shtml)
#				and add an annoucement with today's date.  Date override would 
#				be available thus:
#			updater -c cs3 --backdate 09/05/05 -a "Test on friday!!!"

import re, sys, getopt

from datetime import timedelta, date
from time import strptime, strftime

theclass = ''
month = 1
day = 1
year = 2000
letterday = ''

debug = 0

def main(argv):

	global theclass, month, day, year, letterday, debug
	try:
		opts, args = getopt.getopt(argv, "c:m:d:y:l:h", ["class=","month=", "day=", "year=","letterday=", "help"])
	except  getopt.GetoptError:
		print 'option error'
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if debug:
			print opt, arg
		if len(opts) < 5:
			print 'arg error'
			usage()
			sys.exit(2)
		if opt in ("-c", "--class"):
			arg1 = arg.lower()
			if arg1 in ("cs3", "cs2a", "cs2b", "all"):
				theclass = arg1
			else:
				print 'class error'
				usage()
				sys.exit(2)
		elif opt in ("-m", "--month"):
			month = arg
		elif opt in ("-d", "--day"):
			day = arg
		elif opt in ("-y", "--year"):
			year = arg
		elif opt in ("-l", "--letterday"):
			letterday = arg
		elif opt in ("-h", "--help"):
			usage()
			sys.exit(2)
	createTemplates()


def usage():
	print ''
	print 'Usage:  python updater [-h | -c= | -m= | -d= | -y= | -l=]'
	print ''
	print '\t updater creates stub html files for the weekly assignment pages'
	print ''
	print 'Options:'
	print '-h --h'
	print '\t help (this screen)'
	print '-c=CLASS --class=CLASS'
	print '\t selects a class to update from {CS3, CS2A, CS2B, ALL} with ALL as the default'
	print '-m=NUM --month=NUM'
	print '\t the month [1 - 12]'
	print '-d=NUM --day=NUM'
	print '\t the day [1 - 31]'
	print '-y=NUM --year=NUM'
	print '\t the year with 2005 being the default'
	print '-l={A | B | C | D | E | F} --letterday={A | B | C | D | E | F}'
	print '\t choose the letter day'
	print ''

def createTemplates():
	if debug:
		print 'in createTemplates()'
		print 'evaluating variables'
		print theclass
		print month
		print day
		print year
		print letterday
	if theclass in ("all", "cs3"):
		doCS3()
	if theclass in ("all", "cs2a"):
		doCS2a()
	if theclass in ("all", "cs2b"):
		doCS2b()

def doCS3():
	if debug:
		print 'in doCS3()'
	f = open('cs3template.shtml', 'r')
	ld = ['C', 'D', 'E', 'F']
	doDates('cs3', f, ld)
	
def doCS2a():
	if debug:
		print 'in doCS2a()'
	f = open('cs2atemplate.shtml', 'r')
	ld = ['A', 'B', 'C', 'D']
	doDates('cs2a', f, ld)

def doCS2b():
	if debug:
		print 'in doCS2b()'
	f = open('cs2btemplate.shtml', 'r')
	ld = ['A', 'B', 'E', 'F']
	doDates('cs2b', f, ld)

def doDates(c, f, ld):	
	from datetime import date
	import os
	
	global theclass, month, day, year, letterday, debug
	#calc mondays date
	if debug:
		print 'in doDates'
		print month.isdigit()
		print year.isdigit()
		print day.isdigit()
	mondate = date(eval(year), eval(month), eval(day))
	#create filename
	filename = c + mondate.strftime('%Y%m%d') + '.shtml'
	#create file
	f1 = open(makepath(filename), 'w')
	#populate the file with the selected template
	f1 = f.read()
	f.close()
	tagString = '<!-- #weekdate -->'
	f1 = re.sub(tagString, mondate.strftime('%m/%d/%y'), f1)
	#loop through the tags and put in dates
	datetags = [('mondate', 0), ('tuedate', 1), ('weddate', 2), ('thudate', 3), ('fridate', 4)]
	for tag, offset in datetags:
		tagString = '<!-- #' + tag + ' -->'
		date = mondate + timedelta(days=offset)
		datestring = date.strftime('%m/%d/%y')
		lettertemp = convertLD(letterday, offset)
		datestring = datestring + ' (' + lettertemp + ' day)'
		if debug:
			print tagString
			print tag, offset
			print datestring
		f1 = re.sub(tagString, datestring, f1)
		if lettertemp not in ld:
			f1 = doLD(date.weekday(), f1)
	newfile = open(makepath(filename), 'w')
	newfile.write(f1)
	newfile.close()
	
def doLD(d, f1):
	weekdays = ['mon', 'tue', 'wed', 'thu', 'fri']
	tags = [weekdays[d] + 'cw', weekdays[d] + 'details']
	if debug:
		print 'in doLD() --> no class meeting'
	for tag in tags:
		tags = [weekdays[d] + 'cw', weekdays[d] + 'details']
		tagstring = '<!-- #' + tag + ' -->'
		if debug:
			print tagstring
		f1 = re.sub(tagstring, '<b>no class meeting</b>', f1)
	return f1
	
def convertLD(n, i):
	if i == 0:
		return n
	if n == 'A':
		return 'B'
	elif n == 'B':
		return 'C'
	elif n == 'C':
		return 'D'
	elif n == 'D':
		return 'E'
	elif n == 'E':
		return 'F'
	elif n == 'F':
		return 'A'

def convertLD(n, i):
	days = ['A', 'B', 'C', 'D', 'E', 'F']
	dayindex = days.index(n)
	return days[(dayindex+i) % len(days)]	

def makepath(path):

    """ creates missing directories for the given path and
        returns a normalized absolute version of the path.

    - if the given path already exists in the filesystem
      the filesystem is not modified.

    - otherwise makepath creates directories along the given path
      using the dirname() of the path. You may append
      a '/' to the path if you want it to be a directory path.

    from holger@trillke.net 2002/03/18
    """

    from os import makedirs
    from os.path import normpath,dirname,exists,abspath

    dpath = normpath(dirname(path))
    if not exists(dpath): makedirs(dpath)
    return normpath(abspath(path))


if __name__ == "__main__":
	main(sys.argv[1:])