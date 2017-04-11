#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: richman
# @Date:   2017-04-01 18:55:23
# @File:	annotate.py
# @Last Modified by:   richman
# @Last Modified time: 2017-04-02 13:47:42
# @Mail: heinrich.dinkel@gmail.com

import subprocess
import argparse
import threading
parser = argparse.ArgumentParser()
""" Arguments: inputfilelist """
parser.add_argument('inputfilelist',type=argparse.FileType('r'))

args = parser.parse_args()

def play(f):
	print(f)
	subprocess.check_call(["aplay",f])

def play_background(f):
	threading.Thread(target=play,args=(f,)).start()

def output(lines,transcripts,f='transcript'):
	print "\nWriting {} recordings ... to {} ".format(len(lines),f)
	with open(f,'w') as wp:
		for i in xrange(len(transcripts)):
			wp.write("{} {}\n".format(lines[i],transcripts[i]))

def raw_input_append(text):
	new_text = raw_input("\nPlease enter what u heard: {}\n".format(text))
	return "{} {}".format(text,new_text)

def loadtranscripts(f):
	transcripts = []
	lines = []
	with open(f,'r') as rp:
		for line in rp:
			splits=line.rstrip('\n').split()
			lines.append(splits[0].strip())
			transcripts.append(" ".join(splits[1:]))
	return lines,transcripts

lines, transcripts = loadtranscripts("transcript")
try:
	for i,line in enumerate(args.inputfilelist):
		line = line.rstrip('\n').strip()
		if line in lines:
			print "{} already seen in transcripts .. skipping".format(line)
			continue
		lines.append(line)
		play_background(line)
		transcript=""
		transcript = raw_input_append(transcript)
		out = raw_input("Again? [y/n] ")
		while out != "n":
			play_background(line)
			transcript = raw_input_append(transcript)
			out = raw_input("Again? [y/n] ")
		transcripts.append(transcript)
except KeyboardInterrupt:
	pass
finally:
	output(lines, transcripts)

		