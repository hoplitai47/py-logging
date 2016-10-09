#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import logging
import logging.config


def initialize_logging_ini(path, simple_logger_on_fail=False):
    try:
        logging.config.fileConfig(path)
    except Exception as ex:
        if simple_logger_on_fail == False:
            raise Exception('Cannot read logging configuration .ini file: \'{}\''.str(ex))
        else:
            logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(levelname)s [%(name)s] %(message)s')
            LOG = logging.getLogger('logging_util')
            LOG.warning('Cannot read logging configuration .ini file: {}, fallback to basic console logger'.format(str(path)))


if __name__ == '__main__':
    initialize_logging_ini()





