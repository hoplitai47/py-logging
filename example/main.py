#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import logging

from logging_util import *
initialize_logging_ini('./conf/logconf.ini', simple_logger_on_fail=True)

from msg_printer import printer as msg_printer

LOG = logging.getLogger('main')


def main():
    LOG.info('--------------')
    LOG.info('Program start')

    msg_printer.run()

    LOG.info('Program exit')


if __name__ == '__main__':
    sys.exit(main())



