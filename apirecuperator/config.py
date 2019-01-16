#! /usr/bin/python3
# -*- coding: utf-8 -*-

""" Conf Module """

import os
import sys
import json
import logging


class Conf():
    """ Config Class that's reading config.json file and get value from it. """
    def __init__(self, config_file_path):
        if not os.path.isfile(config_file_path):
            logging.error('ERROR: Config file not found.')
            sys.exit(2)

        with open(config_file_path, 'r') as json_data_file:
            self.config = json.load(json_data_file)

    @property
    def logstash(self):
        logstash = self.config.get('logstash')
        if not logstash:
            logging.warning('Config param, logstash not defined.')
        return logstash

    @property
    def mongodb(self):
        mongodb = self.config.get('mongodb')
        if not mongodb:
            logging.warning('Config param, mongodb not defined.')
        return mongodb

    @property
    def log(self):
        log = self.config.get('log')
        if not log:
            logging.warning('Config param, log not defined.')
        return log
