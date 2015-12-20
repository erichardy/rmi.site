# -*- coding: utf-8 -*-
"""Installer for the rmi.site package."""

from setuptools import find_packages
from setuptools import setup


long_description = (
    open('README.rst').read() +
    '\n' +
    'Contributors\n' +
    '============\n' +
    '\n' +
    open('CONTRIBUTORS.rst').read() +
    '\n' +
    open('CHANGES.rst').read() +
    '\n')


setup(
    name='rmi.site',
    version='1.0a1',
    description="add on for rencontresmusicalesirlandaisestocane.fr",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='Eric Hardy',
    author_email='Eric.Hardy@univ-brest.fr',
    url='https://pypi.python.org/pypi/rmi.site',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['rmi'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'setuptools',
        'z3c.jbot',
        'plonesocial.theme==0.5.4',
        'wildcard.foldercontents==1.3.2',
        'Products.PloneFormGen==1.7.17',
        'collective.geo.mapwidget==2.3',
        'collective.geo.bundle==2.3',
        'collective.geo.behaviour==1.2',
        'collective.geo.kml==3.2',
        'collective.geo.contentlocations==3.1',
        'collective.geo.settings==3.1',
        'collective.geo.openlayers==3.1',
        'geopy==1.9.1',
        'collective.geo.geographer==2.0',
        'pygeoif==0.4.1',
        'collective.z3cform.colorpicker==1.2',
        'quintagroup.plonecaptchas==4.2',
        'quintagroup.pfg.captcha==1.0.5',
        'collective.cover==1.0a12',
        'collective.panels==1.8',
        # 'plone.tiles==1.2',
        'plone.tiles==1.5.1',
        'collective.z3cform.widgets==1.0b11',
        'collective.js.bootstrap==2.3.1.1',
        # 'collective.js.bootstrap==3.3.6',
        'flickrapi==1.4.5',
        'plone.app.drafts==1.0a2',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
