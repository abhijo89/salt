# -*- coding: utf-8 -*-
'''
    integration.loader.interfaces
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Test Salt's loader
'''

# Import Python libs
from __future__ import absolute_import

# Import Salt Testing libs
from salttesting import TestCase
from salttesting.helpers import ensure_in_syspath

import integration

ensure_in_syspath('../../')

# Import Salt libs
import salt.ext.six as six
from salt.config import minion_config

import salt.loader

# TODO: the rest of the public interfaces


class raw_mod_Test(TestCase):
    '''
    Test the interface of raw_mod
    '''
    def test_basic(self):
        self.opts = minion_config(None)
        testmod = salt.loader.raw_mod(self.opts, 'test', None)
        for k, v in testmod.iteritems():
            self.assertEqual(k.split('.')[0], 'test')

    def test_bad_name(self):
        self.opts = minion_config(None)
        testmod = salt.loader.raw_mod(self.opts, 'module_we_do_not_have', None)
        self.assertEqual(testmod, {})
