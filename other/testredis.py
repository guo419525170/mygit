#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
import time
import redis
from redis.sentinel import Sentinel
l=threading.Lock()
sentinel = Sentinel([('172.17.100.50', 26379),('172.17.100.50', 26479)],socket_timeout=0.5)
def subtraction():
 
	for a in range(50000):
        	name = 'zhoumeng' + str(a)
		key = 'xiaoyu' + str(a) 
		try:
    			master = sentinel.master_for('mymaster', socket_timeout=0.5, password='123')
    			master.set(name, key)
    			slave = sentinel.slave_for('mymaster', socket_timeout=0.5, password='123')
    			r_ret = slave.get(name)
		except Exception as e:
			print ' 报错', e
		else:
			print(r_ret)
if __name__ == '__main__':
    thread=[]
    for x in range(20):
        t=threading.Thread(target=subtraction())
        thread.append(t)
        t.start()
    for x in thread:
        t.join()
