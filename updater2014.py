#!/usr/local/bin/python

#updater v. 1.1

# updater creates a new file from a template, changes the dates and calculates
# class meetings.
# To do:  	upload to server;  get/change syllabus page; add/process cw and other
#			comments automatically

#			this update: syllabus

#			updater -c cs3 -t moncw -s "<b>Lab 202:</b> lab0923 today"
#				this call would get the version from the local store, and replace
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
month = 9
day = 1
year = 2014

debug = 1
debug1 = 1

def main(argv):

	global month, day, year, debug
	try:
		opts, args = getopt.getopt(argv, "m:d:y:h", ["month=", "day=", "year=", "help="])
	except  getopt.GetoptError:
		print 'option error'
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if debug:
			print opt, arg
		if len(opts) < 3:
			print 'arg error'
			usage()
			sys.exit(2)
		elif opt in ("-m", "--month"):
			month = arg
		elif opt in ("-d", "--day"):
			day = arg
		elif opt in ("-y", "--year"):
			year = arg
		elif opt in ("-h", "--help"):
			usage()
			sys.exit(2)
			
	doDates()


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
	print '\t selects a class to update from {CS1, CALCAB, DISCRETE, APCS, ALL} with ALL as the default'
	print '-m=NUM --month=NUM'
	print '\t the month [1 - 12]'
	print '-d=NUM --day=NUM'
	print '\t the day [1 - 31]'
	print '-y=NUM --year=NUM'
	print '\t the year with 2014 being the default'
	print ''


def doDates():	
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
	filename = mondate.strftime('%Y%m%d') + '.html'
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

def updatesyllabus():
	filepath = '/Users/bhgray/Sites/tos/html/cs/'
	filenames = ['/cs3syll.shtml', '/cs2asyll.shtml', 'cs2bsyll.shtml']
	for filename in filenames:
		n = filepath + filename
		f = open(n, 'r')
		f1 = f.read()
		tagstring = '<!-- #update -->'
		mondate = date(eval(year), eval(month), eval(day))
		monstring = mondate.strftime('%m/%d/%y')
		fridate = mondate + timeinterval(days=4)
		fristring = fridate.strftime('%m/%d/%y')
		updatestring = monstring + ' - ' + fristring
		if debug1:
			print updatestring
		#f1 = re.sub(tagstring, updatestring, f1)
		


if __name__ == "__main__":
	main(sys.argv[1:])