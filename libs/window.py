# -*- coding: utf8 -*-

# Copyright (C) 2015 - Philipp Temminghoff <phil65@kodi.tv>
# This program is Free Software see LICENSE file for details

"""
KodiDevKit is a tool to assist with Kodi skinning / scripting using Sublime Text 3
"""

from . import utils


class Window(object):
    """
    Class representing a Kodi Window
    """

    def __init__(self, path):
        self.root = utils.get_root_from_file(path)

    def get_controls(self, control_type):
        """
        yields all control nodes from window
        """
        for node in self.root.xpath(".//control[@type='%s']" % control_type):
            yield node

    def xpath(self, *args, **kwargs):
        """
        xpath function for the window xml
        """
        return self.root.xpath(*args, **kwargs)
