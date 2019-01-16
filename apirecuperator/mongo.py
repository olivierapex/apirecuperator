#! /usr/bin/python3
# -*- coding: utf-8 -*-

""" MongoDB logger Module """

from pymongo import MongoClient


class Mongo():
    """
        Simple Class that is managin MongoDB connection and insert log to it.
        TO DO (please help yourself):
            - Changing general exception to specific one.
    """
    def __init__(self, config):
        conn_info = ('mongodb://' + config['user'] + ':' + config['pass'] + '@' + config['host'] + '/' + config['db'])
        self.conn = self.__connection(conn_info)

    @staticmethod
    def __connection(conn_info):
        """ Connection Function. Return connection Information or False. """
        try:
            return MongoClient(conn_info)
        except Exception:
            return False

    def insert_one(self, data):
        """ Inser function as mongo. """
        try:
            return self.conn.recuperator.logger.insert_one(data)
        except Exception:
            return False
