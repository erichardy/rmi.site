# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import rmi.site


class RmiSiteLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=rmi.site)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'rmi.site:default')


RMI_SITE_FIXTURE = RmiSiteLayer()


RMI_SITE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(RMI_SITE_FIXTURE,),
    name='RmiSiteLayer:IntegrationTesting'
)


RMI_SITE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(RMI_SITE_FIXTURE,),
    name='RmiSiteLayer:FunctionalTesting'
)


RMI_SITE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        RMI_SITE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='RmiSiteLayer:AcceptanceTesting'
)
