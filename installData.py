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

from conf import CONFIG
#--------------------------------------------------------------
# Globl Constants & Functions
#--------------------------------------------------------------
def main():
    idt = InstallData()
    idt.installRedisData(CONFIG['redis'])

#--------------------------------------------------------------
# Classes
#--------------------------------------------------------------
class InstallData(object):




