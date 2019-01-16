# API Recuperator

## Requirements
  Python3 Bro !

### Description

 This is a simple python service that is taking any HTTP request and log it to local, mongo or logstash ! (you can right modules for more.)
 The goal was to receive and analyse calls from other services that you cannot look at the code and you have no idea what is gonna do.
 By example, you can replace Apple or Google callback pointing URL to your server running this app and you will receive the exact log of what their callback bad look like.
 I hope this will save you some time !


### Usage

  By default, UWSGI gonna run under the port 9090.
  To install run "python3 setup install"
  To start the service run "sudo /etc/init.d/apirecuperator start". Yes init.d service. Please help youself and make a systemd file :) .
  Default URL "http://127.0.0.1:9090/api/recuperator" 

### Platform

 - Tested against Ubuntu 16 and 18, but can run on Centos or any Linux Distro with python3.

## Atributes

  See config.json.example.
  You can modify the default config file under "/etc/apirecuperator/config.json".
  changed "enabled" attribute to true, if you wan to active a module, like logstatsh. You also need to populate server host, port, etc.
  Look like this, pretty simple:
    {
      "logstash": {
          "enabled": false,
          "host": "",
          "port": 5500,
          "version": 3
      },
      "mongodb": {
          "enabled": false,
          "host": "",
          "db": "",
          "coll": "",
          "user": "",
          "pass": ""
      },
      "log": {
          "path": "/var/log/apirecuperator/local-query.log"
      }
    }

### config

  Configuration by cities, using node.override attributes.

## Authors and maintainers

  Originally written by Olivier Giroux

## License

  Dude seriously, ... if this helped you, do the fuck you want with the code !
  You can pay me a beer one day if you like :)
