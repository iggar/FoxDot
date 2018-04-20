#!/usr/bin/env python

from distutils.core import setup

setup(name='FoxDot',
      version='0.6.2',
      description='Live coding music with SuperCollider',
      author='Ryan Kirkbride',
      author_email='ryan@foxdot.org',
      url='http://foxdot.org/',
      packages=['FoxDot',
                'FoxDot.lib',
                'FoxDot.lib.Code',
                'FoxDot.lib.Custom',
                'FoxDot.lib.Extensions',
                'FoxDot.lib.Workspace',
                'FoxDot.lib.Patterns',
                'FoxDot.lib.SCLang',
                'FoxDot.lib.Settings',
                'FoxDot.lib.Utils'],
      package_data = {'FoxDot': ['snd/*/*/*.*',
                                 'snd/_loop_/foxdot.wav',
                                 'snd/_loop_/drums130.wav',
                                 'snd/_loop_/dirty120.wav',
                                 'snd/_loop_/afro105.wav',
                                 'snd/_loop_/break170.wav',
                                 'snd/_loop_/cowbells110.wav',
                                 'snd/_loop_/robot110.wav',
                                 'snd/_loop_/techno130.wav',
                                 'osc/*.scd',
                                 'osc/sceffects/*.scd',
                                 'osc/scsyndef/*.scd',
                                 'demo/*.py',
                                 'lib/Extensions/*.json',
                                 ],
                      'FoxDot.lib.Workspace': ['img/*', 'tmp/*'],
                      'FoxDot.lib.Settings' : ['conf.txt']})
