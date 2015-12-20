# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from rmi.site.testing import RMI_SITE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that rmi.site is properly installed."""

    layer = RMI_SITE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if rmi.site is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'rmi.site'))

    def test_browserlayer(self):
        """Test that IRmiSiteLayer is registered."""
        from rmi.site.interfaces import (
            IRmiSiteLayer)
        from plone.browserlayer import utils
        self.assertIn(IRmiSiteLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = RMI_SITE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['rmi.site'])

    def test_product_uninstalled(self):
        """Test if rmi.site is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'rmi.site'))
