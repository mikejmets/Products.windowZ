# -*- coding: utf-8 -*-
#
# File: Window.py
#
# Copyright (c) 2007 by Jean Rodrigo Ferri
# Generator: ArchGenXML
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """Jean Rodrigo Ferri <jeanrodrigoferri@yahoo.com.br>"""
__docformat__ = "plaintext"

import html2text
from plone.dexterity.content import Item
from plone.registry.interfaces import IRegistry
from Products.windowZ.interfaces import IWindow
from urllib import parse
import urllib.request
from zope.component import queryUtility
from zope.interface import implementer
from ZODB.POSException import ConflictError


def registry_record(key):
    registry = queryUtility(IRegistry)
    return registry["Products.windowZ.interfaces.IWindowZSettings." + key]


@implementer(IWindow)
class Window(Item):
    """A Window is a content type that shows one URL inside an iFrame
    in a page of the site.
    """

    def SearchableText(self):
        """Format the title, description and the provided page's content to
        be cataloged by portal_catalog, if user checked
        catalog_page_content option.
        """
        if self.catalog_page_content:
            try:
                self.getProxies()  # open proxy connection
                remote_url = self.remote_url()
                page = urllib.request.urlopen(remote_url)
                page_body = page.read()
                content_type = page.info().type
            except ConflictError:
                raise
            except Exception:
                page_body = ""
                content_type = None
            try:
                page_content = self._processPageBody(page_body, content_type)
            except IndexError:
                page_content = ""
        else:
            page_content = ""
        return "%s %s %s" % (self.Title(), self.Description(), page_content)

    # Methods from Interface IWindow

    def getProxies(self):
        """Open proxy HTTP connection if it was set in the registry."""
        http_proxy = registry_record("http_proxy")
        if http_proxy:
            try:
                proxies = {"http": http_proxy}
                # proxy_support = urllib2.ProxyHandler(proxies)
                # opener = urllib2.build_opener(proxy_support)
                # urllib2.install_opener(opener)
                proxy_support = urllib.request.ProxyHandler(proxies)
                opener = urllib.request.build_opener(proxy_support)
                urllib.request.install_opener(opener)
            except Exception:
                pass

    def getPageHeight(self):
        """Returns page_height or the default value from the registry."""
        if self.page_height:
            return self.page_height
        else:
            page_height = registry_record("page_height")
            if page_height:
                return page_height
        return "500px"

    def remote_url(self):
        """Returns the Window URL the field remoteUrl prefixed with
        base_url if it's selected by user.
        """
        if self.use_base_url:
            base_url = registry_record("base_url")
            url = "%s%s" % (base_url, self.remoteURL)
        else:
            url = self.remoteURL
        if self.inherit_protocol:
            scheme = parse.urlsplit(self.REQUEST.get("SERVER_URL"))[0]
            parts = list(parse.urlsplit(url))
            parts[0] = scheme
            url = parse.urlunsplit(parts)
        return url

    def getPageWidth(self):
        """Returns page_width or the default value from the registry."""
        if self.page_width:
            return self.page_width
        else:
            page_width = registry_record("page_width")
            if page_width:
                return page_width
        return "100%"

    def _processPageBody(self, page_body, content_type):
        """Process the link body with strip-o-gram library catching only the
        page content.
        """
        if content_type and "html" not in content_type:
            return ""
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_images = True
        page_content = h.handle(page_body)
        return page_content
