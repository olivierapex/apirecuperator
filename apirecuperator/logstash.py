#! /usr/bin/python3
# -*- coding: utf-8 -*-

""" Logstash sender Module """

import logging
import logstash


# Attention Here, this module is compatible with version 2.
class Logstashsender():
    """ Simple class that is pushing log to logstash. You can also disable this and use filebeat. """
    def __init__(self, config):
        self.logger = logging.getLogger('python-logstash-logger')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logstash.TCPLogstashHandler(config['host'], config['port'], version=config['version']))

    def send_json(self, data):
        """ Send log as JSON format to logstash. """
        self.logger.info('Api Recuperator', extra=data)
