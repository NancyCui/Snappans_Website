#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#--------------------------------------------------------------
#
# Snappans Data Initialization
#
# Install data and redis for Snappans.
#
#--------------------------------------------------------------
#
# Date:     2015-05-09
#
# Author:   Guanyu Tao & Ningxin Cui
#
#

import sys
import MySQLdb
import redis

#--------------------------------------------------------------
# Globl Constants & Functions
#--------------------------------------------------------------
REDIS_DB_PARAMS = {
        "host": "127.0.0.1",
        #"host": "112.126.75.226",
        "port": 6379,
        "db": 0,
        "charset": "utf8"
    }

MYSQL_DB_PARAMS = {
    "host": "127.0.0.1",
    #"host": "112.126.75.226",
    "port": 3306,
    "user": "ningxin",
    "passwd": "watson",
    "db": "inteluniq",
    "charset": "utf8"
    }

def main():
    idt = InstallData()
    idt.installMySQLData(MYSQL_DB_PARAMS)
    idt.installRedisData(REDIS_DB_PARAMS)





