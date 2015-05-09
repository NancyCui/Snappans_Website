#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#--------------------------------------------------------------
#
# Snappans Database
#
# Install database for Snappans.
#
#--------------------------------------------------------------
#
# Date:     2015-04-25
#
# Author:   Guanyu Tao & Ningxin Cui
#
#

import os
import sys
import MySQLdb

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONF_DIR = os.path.join( BASE_DIR, 'conf')
os.sys.path.insert(0, CONF_DIR)

from conf import CONFIG

#--------------------------------------------------------------
# Global Constants & Vars
#--------------------------------------------------------------
INSTALL_SQL = """
SET time_zone = "+08:00";

CREATE TABLE IF NOT EXISTS `users_pwd` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS `users` (
  `user_id` int(11) NOT NULL,
  `email` varchar(255) NULL,
  `phone` varchar(20) NULL,
  `nick_name` varchar(30) NOT NULL,
  `user_type` tinyint(1) NOT NULL DEFAULT '1' COMMENT '浏览用户默认1',
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`user_id`),
  FOREIGN KEY(`user_id`) REFERENCES users_pwd(`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `traders_status` (
  `trader_id` int(11) NOT NULL,
  `verify_status` tinyint(1) NOT NULL DEFAULT '0' COMMENT '未认证商家默认0',
  PRIMARY KEY (`trader_id`),
  FOREIGN KEY(`trader_id`) REFERENCES users_pwd(`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `follow` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `follow_id` int(11) NOT NULL,
  `follower_id` int(11) NOT NULL,
  `follow_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY(`follow_id`) REFERENCES users_pwd(`user_id`),
  FOREIGN KEY(`follower_id`) REFERENCES users_pwd(`user_id`)
)ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `message` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) NOT NULL,
  `receiver_id` int(11) NOT NULL,
  `message` datetime NOT NULL,
  PRIMARY KEY (`message_id`),
  FOREIGN KEY(`sender_id`) REFERENCES users_pwd(`user_id`),
  FOREIGN KEY(`receiver_id`) REFERENCES users_pwd(`user_id`)
)ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `invitation_codes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `invitation_code` varchar(30) NOT NULL,
  `code_type` tinyint(1) NOT NULL DEFAULT '0' COMMENT '验证码未分配默认0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `inviation_relationship` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `inviter_id` int(11) NOT NULL,
  `invitee_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY(`inviter_id`) REFERENCES users_pwd(`user_id`),
  FOREIGN KEY(`invitee_id`) REFERENCES users_pwd(`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `model_address` (
  `address_id` int(11) NOT NULL AUTO_INCREMENT,
  `model_id` int(11) NOT NULL,
  `country` varchar(30) NOT NULL,
  `city` varchar(30) NOT NULL,
  `street` varchar(100) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`address_id`),
  FOREIGN KEY(`model_id`) REFERENCES users_pwd(`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `trader_id` int(11) NOT NULL,
  `model_id` int(11) NOT NULL,
  `tracking_num` varchar(50) NOT NULL,
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY(`trader_id`) REFERENCES users_pwd(`user_id`),
  FOREIGN KEY(`model_id`) REFERENCES users_pwd(`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `trader_offer` (
  `trader_offer_id` int(11) NOT NULL AUTO_INCREMENT,
  `trader_id` int(11) NOT NULL,
  `expired_time` datetime NOT NULL,
  `deadline` datetime NOT NULL,
  `create_time` datetime NOT NULL,
  `description` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  `country` varchar(30) NOT NULL,
  `city` varchar(30) NOT NULL,
  PRIMARY KEY (`trader_offer_id`),
  FOREIGN KEY(`trader_id`) REFERENCES users_pwd(`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `trader_offer_relationship` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model_id` int(11) NOT NULL,
  `offer_id` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY(`model_id`) REFERENCES users_pwd(`user_id`),
  FOREIGN KEY(`offer_id`) REFERENCES trader_offer(`trader_offer_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `model_offer` (
  `model_offer_id` int(11) NOT NULL AUTO_INCREMENT,
  `model_id` int(11) NOT NULL,
  `expired_time` datetime NOT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `country` varchar(30) NOT NULL,
  `city` varchar(30) NOT NULL,
  `create_time` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`model_offer_id`),
  FOREIGN KEY(`model_id`) REFERENCES users_pwd(`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `model_offer_relationship` (
  `id` int(11) NOT NULL  AUTO_INCREMENT,
  `trader_id` int(11) NOT NULL,
  `offer_id` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY(`trader_id`) REFERENCES users_pwd(`user_id`),
  FOREIGN KEY(`offer_id`) REFERENCES model_offer(`model_offer_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `albums` (
  `album_id` int(11) NOT NULL AUTO_INCREMENT,
  `album_name` varchar(30) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`album_id`),
  FOREIGN KEY(`user_id`) REFERENCES users_pwd(`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `photos` (
  `photo_id` int(11) NOT NULL AUTO_INCREMENT,
  `photo_url` varchar(1024) NOT NULL,
  `create_time` datetime NOT NULL,
  `photo_type` tinyint(1) NOT NULL DEFAULT '1' COMMENT '普通图片默认1',
  `description` longtext DEFAULT NULL,
  `repost_num` int(11) DEFAULT NULL,
  `like_num` int(11) DEFAULT NULL,
  `country` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `album_id` int(11) NOT NULL,
  `item_url` varchar(1024) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`photo_id`),
  FOREIGN KEY(`album_id`) REFERENCES albums(`album_id`),
  FOREIGN KEY(`user_id`) REFERENCES users(`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `photo_comments` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `photo_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `reply_id` int(11) DEFAULT NULL COMMENT '回复的comment_id可为空',
  `photo_comment` longtext NOT NULL,
  PRIMARY KEY (`comment_id`),
  FOREIGN KEY(`photo_id`) REFERENCES photos(`photo_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;
"""

def install_db(db_params):
    if not db_params["user"]:
        print "Cannot connect to DB, you need to supply correct db params."
        print "Got db params: %s" % db_params
    else:   
        try:    
            conn = MySQLdb.connect(**db_params)
            conn.autocommit(True)
            print "connect success, installing tables"
            cur = conn.cursor()
            cur.execute(INSTALL_SQL)
            print "Congratulations! All Done!"
        except Exception,e:
            errno = e.args[0]
            errmsg = e.args[1]
            print "Got db params: %s" % db_params
            if errno == 2014:
                return # ignore it

            print "Error %d: %s" % (errno, errmsg) 
            if "unknown database" in errmsg.lower():
                print "You can try this:\n\tCREATE DATABASE %s CHARACTER SET %s COLLATE %s_general_ci;" % (db_params['db'], db_params['charset'], db_params['charset'])
                sys.exit(-1)

def main():
    install_db(CONFIG['database'])

#--------------------------------------------------------------
#
# Main routines
#
#--------------------------------------------------------------
if __name__ == '__main__':
   main()

