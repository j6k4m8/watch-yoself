'''
Monitors your progress whilst you code.
'''

import os, datetime, time

ignore_files = []


def get_dont_watch():
	global ignore_files
	dont = open('dont.watch', 'r+')
	ignore_files = dont.read().split('\n')
	dont.close()


def start(path_to_walk='./'):
	# Assuming ./pwd
	ft = open('out.watch', 'rb+')
	ft.seek(-1, os.SEEK_END);
	(_, _, files) = os.walk(path_to_walk).next()
	ft.write('"' + str(datetime.datetime.now()) + '": {\n')
	for f in files:
		fo = open(f, 'r')
		c = len(fo.read().split(' '))
		if (fo.name not in ignore_files):
			ft.write('"' + fo.name + '":' + str(c) + ',\n')
		fo.close()
	ft.write("}, }")
	ft.close()

ft = open('out.watch', 'w')
ft.write("var _d = {\n}")
ft.close();

get_dont_watch()
print ignore_files
try:
	while 1:
		start()
		time.sleep(10)
		print "Wrote files.\n"
except KeyboardInterrupt:
    pass
