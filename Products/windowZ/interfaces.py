# -*- coding: utf-8 -*-
#
# File: interfaces.py
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

from plone.supermodel import model
from Products.windowZ import WindowZMessageFactory as _
from zope import schema
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IWindowZLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IWindow(model.Schema):
    """Window interface."""

    remoteURL = schema.URI(
        title=_("windowZ_label_url", default="URL"),
        description=_(
            "windowZ_help_url",
            default='The link is used almost verbatim, relative links become absolute and the strings "${navigation_root_url}" and "${portal_url}" get replaced with the real navigation_root_url or portal_url. If in doubt which one to use, please use navigation_root_url.',
        ),
    )

    page_width = schema.Text(
        title=_("windowZ_label_page_width", default="Page Width"),
        description=_(
            "windowZ_help_page_width",
            default=(
                "Enter a value for the page width. If it's not provided "
                "the page width will assumes the default value defined in "
                "the site setup. You may use %, px, em, etc."
            ),
        ),
        max_length=10,
        required=False,
    )

    page_height = schema.Text(
        title=_("windowZ_label_page_height", default="Page Height"),
        description=_(
            "windowZ_help_page_height",
            default=(
                "Enter a value for the page height. If it's not provided the "
                "page height will assumes the default value defined in the "
                "site setup. You may use %, px, em, etc."
            ),
        ),
        max_length=10,
        required=False,
    )

    hide_metadata = schema.Bool(
        default=True,
        title=_("windowZ_label_hide_metadata", default="Hide Metadata?"),
        description=_(
            "windowZ_help_hide_metadata",
            default=(
                "Check this option if you want to hide the page metadata, "
                "like title, description, print and send page icons, author, "
                "etc."
            ),
        ),
    )

    use_base_url = schema.Bool(
        title=_("windowZ_label_use_base_url", default="Use Base URL?"),
        description=_(
            "windowZ_help_use_base_url",
            default=(
                "Check this option if you want to use the base URL defined in "
                "the site setup as a prefix to the provided link."
            ),
        ),
    )

    catalog_page_content = schema.Bool(
        default=False,
        title=_("windowZ_label_catalog_page_content", default="Catalog Page Content?"),
        description=_(
            "windowZ_help_catalog_page_content",
            default=(
                "Check this option if you want to have the content of the "
                "provided page indexed in the site catalog and available "
                "in the portal search box."
            ),
        ),
    )

    show_reference = schema.Bool(
        title=_("windowZ_label_show_reference", default="Show Reference?"),
        description=_(
            "windowZ_help_show_reference",
            default=(
                "Check this option if you want to show the provided link as "
                "a reference in the bottom of the page."
            ),
        ),
    )

    inherit_protocol = schema.Bool(
        title=_("windowZ_label_inherit_protocol", "Inherit Protocol?"),
        description=_(
            "windowZ_help_inherit_protocol",
            default=(
                "Check this option if you want to inherit the "
                "URL-protocol for the iframe from the content URL "
            ),
        ),
    )


class IWindowZSettings(model.Schema):
    """Default settings for windowZ content objects"""

    page_width = schema.TextLine(
        title=_("windowZ_tool_label_page_width", default="Default Page Width"),
        description=_(
            "windowZ_tool_help_page_width",
            default=(
                "Width of the iFrame area. This is the default value for the "
                "Window content types and may be redefined individually for "
                "each Window content. You may use %, px, em, etc."
            ),
        ),
        required=True,
        default=u"100%",
    )

    page_height = schema.TextLine(
        title=_("windowZ_tool_label_page_height", default="Default Page Height"),
        description=_(
            "windowZ_tool_help_page_height",
            default=(
                "Height of the iFrame area. This is the default value for the "
                "Window content types and may be redefined individually for "
                "each Window content. You may use %, px, em, etc."
            ),
        ),
        required=False,
    )

    base_url = schema.TextLine(
        title=_("windowZ_label_base_url", default="Base URL"),
        description=_(
            "windowZ_help_base_url",
            default=(
                "Base URL provided as prefix for Window relative URLs. It's "
                "used only if the option Use Base URL? is checked."
            ),
        ),
        required=False,
        default=u"http://",
    )

    http_proxy = schema.TextLine(
        title=_("windowZ_label_http_proxy", default="HTTP Proxy"),
        description=_(
            "windowZ_help_http_proxy",
            default=(
                "If there is a proxy in front of the server you should enter "
                "the HTTP proxy address. It may seems like "
                "http://proxy_address:port or "
                "http://username:password@proxy_address:port."
            ),
        ),
        required=False,
    )
