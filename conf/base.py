#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#--------------------------------------------------------------
#
# Base handlers.
#
#--------------------------------------------------------------
#
# Date:             2015-05-09
# Author:           Guanyu Tao & Ningxin Cui
#
#

__version__ = "0.0.1"
__version_info__ = __version__.split('.')

import tornado.web
from tornado.escape import json_encode

#--------------------------------------------------------------
# Global Constants & Vars
#--------------------------------------------------------------

#--------------------------------------------------------------
# Global Functions
#--------------------------------------------------------------

#--------------------------------------------------------------
# Classes
#--------------------------------------------------------------

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    @property
    def rc(self):
        return self.application.rc

    def jsonOk(self, d=None):
        d_ = {"errno": 0, "msg": "ok"}
        if d:
            d_.update(d)
        self.set_header("Content-Type", "application/json")
        self.finish(json_encode(d_))

    def jsonError(self, d=None):
        d_ = {"errno": -1, "msg": "unknown error"}
        if d:
            d_.update(d)
        self.set_header("Content-Type", "application/json")
        self.finish(json_encode(d_))

