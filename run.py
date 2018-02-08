#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,time
logo = """
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$Y/'$$$$P'a$$$$$$$$$$$$$$$$
$$$$$$$$$",` /,/,mT$$$$ d$$$$$$$$$$$$$$$$$
$$$$$l',` , '/d$$$$P^$a `^a`W$$$$$$$$$$$$$
$$l', ` ,   |d$$$P^$'   _  _ ==~a$$$$$$$$$
$l.`  .     \'i$^4'   _eP$$$$$$$$$$$$$$$$$
l '  .         /   ,  $$$$' `$~$$$$$$$$$$$
; ' ,              l /^' .,$oa$$$$$$$$$$$$
b ' ,        .     (_ ,1$$$$$$'$$$$$$$$$$$
$ , ,      .;       _$$$$$$$P $a$$$$$$$$$$
$, ,`    .$Ly        lM"^ ,  ,$$$$$$$'$$$$
$$, ,`   d$Liy      /'   edb $$$$$$$'$$$$$
$$$$,,'. $$$Li     (    d$$$$$$$$$$'$$$$$$
$$$$$$,' v$$$Li4.   `  `Q$$$$$$$P',$$$$$$$
$$$$$$$$,$$$$$$$L44., . .     ,,;d$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$ IP Monster $$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$ Vaild IP Generator $$$$$$$$$$$$$$$$$$$$$
$ By : WazeHell $$$$$$$$$$$$$$$$$$$$$$$$$$
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
print(logo)
port = raw_input("port :")
pro = raw_input("TCP Or UDP ? eg. tcp :")
name = raw_input("Service Name eg . smb :")
filename = raw_input("File To Save IP :")
threads = raw_input("Threads Number :")
def nse_file(port,pro,name,filename):
    lol = 'description=[[ \n'
    lol += 'Valid IP Generator \n'
    lol += 'With Port '+port+'/'+pro+' \n'
    lol += 'Script By : WazeHell \n'
    lol += ']] \n'
    lol += 'author = "WazeHell" \n'
    lol += 'license = "Same as Nmap--See http://nmap.org/book/man-legal.html" \n'
    lol += 'categories = {"default", "discovery", "external", "intrusive"} \n'
    lol += 'require "shortport" \n'
    lol += 'portrule = shortport.portnumber('+port+', "'+pro+'", "open") \n'
    lol += 'action = function(host, port) \n'
    lol += '	file = io.open ("'+filename+'","a+") \n'
    lol += '	file:write (host.ip.."\n") \n'
    lol += '	file:flush() \n'
    lol += '	file:close() \n'
    lol += 'end'
    return lol

def bat_file(name,port,threads):
    dp = '@echo off \n'
    dp += 'for /l %%%x in (1,1,'+threads+') do ( \n'
    dp += 'start "'+name+'" /HIGH nmap -n -Pn -p T:'+port+' -T5 --script '+name+'.nse -iR 0 \n'
    dp += ') \n'
    dp += 'exit'
    return dp
time.sleep(1)
print("Monster is ready ! pls wait")
nse_to_go = nse_file(port,pro,name,filename)
bat_to_go = bat_file(name,port,threads)
bat_filee = open('run.bat', 'w+')
nse_filee = open(name+'.nse', 'w+')
bat_filee.write(bat_to_go)
bat_filee.close()
nse_filee.write(nse_to_go)
nse_filee.close()
print("it's must start now ! pls make sure you have nmap in your machine")
time.sleep(3)
os.system("run.bat")
