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

CONFIG = {
        ##############
        #  
        # Database
        #
        ##############
        "database": {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "ningxin",
            "passwd": "watson",
            "db":"snappans",
            "charset": "utf8"
            },
        "resultset_capacity": 5000,
        "redis": {
            "host": "127.0.0.1",
            #"host": "112.126.75.226",
            "port": 6379,
            "db": 0,
            "charset": "utf8"
        },
        "web_port": "8000",
}