'''
Monitors your progress whilst you code.
'''

import os, datetime, time


def start(path_to_walk='./'):
	# Assuming ./pwd
	(_, _, files) = os.walk(path_to_walk).next()
	ft = open('out.watch', 'a+')
	ft.write('#####-----' + str(datetime.datetime.now()) + '\n')
	for f in files:
		fo = open(f, 'r')
		# print len(fo.read().split('\n'))
		c = len(fo.read().split(' '))
		if (fo.name != 'out.watch'):
			ft.write(fo.name + ',' + str(c) + '\n')
		fo.close()
	ft.close()

while 1:
	start()
	time.sleep(5)
