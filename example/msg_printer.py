#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

LOG = logging.getLogger('msg_printer_logger')


class printer(object):
    @staticmethod
    def run():
        LOG.info('msg_printer main() function')


