#! /usr/bin/python3
# -*- coding: utf-8 -*-

""" Recuperator Module """

import logging
import falcon
from apirecuperator import logstash
from apirecuperator import mongo
from apirecuperator import config


class Recuperator():
    """ Recuperator Class. From Falcon library, taking all kind of HTTP query and log them with details. """
    def __init__(self, config_file_path=None):
        self.config = config.Conf(config_file_path)
        self.stash = self.config.logstash
        self.mongodb_info = self.config.mongodb
        self.log_path = self.config.log['path']
        if self.stash['enabled'] == str(True):
            self.stash = logstash.Logstashsender(self.stash)
        else:
            self.stash = None
        if self.mongodb_info['enabled'] == str(True):
            self.mongo = mongo.Mongo(self.mongodb_info)
        else:
            self.mongo = None

    @staticmethod
    def __isset(variable_to_test):
        """ Simple function that check if variable exist and not null. Return the same variable or None. """
        try:
            if variable_to_test:
                return variable_to_test
        except NameError:
            return None

    @staticmethod
    def __separate_variables_from_url(query_string_param):
        """ Get param from query string. Return a Dict with param. """
        if query_string_param:
            try:
                param_dict = {}
                for value in query_string_param.split('&'):
                    param_dict.update({value.split('=')[0]: value.split('=')[1]})
                return param_dict
            except Exception as error:
                return {'ERROR': str(error)}
        else:
            return None

    @staticmethod
    def __dict_to_string(dict_to_format):
        """ Simple fonction, wierd I know, that force a dict to string. Return the string if possible to change it or the same Dict. """
        try:
            return '"' + str(dict_to_format) + '"'
        except Exception:
            return dict_to_format

    def __get_http_info(self, req, rtype):
        """ Parse all http data request. Return a Dict of the http request. """
        headers = self.__dict_to_string(self.__isset(req.headers))
        data = self.__isset(req.bounded_stream.read())
        cookies = self.__dict_to_string(self.__isset(req.cookies))
        query_string_param = self.__dict_to_string(self.__separate_variables_from_url(req.query_string))

        try:
            if data:
                try:
                    decoded_data = data.decode('utf8')
                except Exception as exc:
                    decoded_data = str(exc)
            else:
                decoded_data = None
            resp_dict = {'API_REQUEST': rtype, 'API_HEADERS': headers, 'API_DATA': decoded_data, 'API_COOKIES': cookies, 'API_QUERY_STRING_PARAMS': query_string_param}
            return resp_dict
        except Exception as error:
            err = {'ERROR': str(error)}
            return err

    def __logger(self, data):
        """ Simple logger function. Return nothing"""
        logging.basicConfig(filename=self.log_path, filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
        if self.stash:
            self.stash.send_json(data)
        if self.mongo:
            self.mongo.insert_one(data)
        logging.info(str(data))

    def on_get(self, req, resp):
        """ Falcon Function, executing from http request. Return nothing """
        resp.status = falcon.HTTP_200
        http_info = self.__get_http_info(req, 'GET')
        self.__logger(http_info)

    def on_post(self, req, resp):
        """ Falcon Function, executing from http request. Return nothing """
        resp.status = falcon.HTTP_200
        http_info = self.__get_http_info(req, 'POST')
        self.__logger(http_info)

    def on_patch(self, req, resp):
        """ Falcon Function, executing from http request. Return nothing """
        resp.status = falcon.HTTP_200
        http_info = self.__get_http_info(req, 'PATCH')
        self.__logger(http_info)

    def on_put(self, req, resp):
        """ Falcon Function, executing from http request. Return nothing """
        resp.status = falcon.HTTP_200
        http_info = self.__get_http_info(req, 'PUT')
        self.__logger(http_info)

    def on_options(self, req, resp):
        """ Falcon Function, executing from http request. Return nothing """
        resp.status = falcon.HTTP_200
        http_info = self.__get_http_info(req, 'OPTIONS')
        self.__logger(http_info)

    def on_head(self, req, resp):
        """ Falcon Function, executing from http request. Return nothing """
        resp.status = falcon.HTTP_200
        http_info = self.__get_http_info(req, 'HEAD')
        self.__logger(http_info)

    def on_delete(self, req, resp):
        """ Falcon Function, executing from http request. Return nothing """
        resp.status = falcon.HTTP_200
        http_info = self.__get_http_info(req, 'DELETE')
        self.__logger(http_info)


def run(config_file_path=None):
    """ Run function. Return wsgi object. """
    wsgi_app = api = falcon.API()
    api.add_route('/api/recuperator', Recuperator(config_file_path))
    return wsgi_app


if __name__ == '__main__':
    wsgi_app = run()
