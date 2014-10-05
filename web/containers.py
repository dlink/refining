#!/usr/bin/env python
# -*- coding: utf-8 -*-

from vweb.htmlpage import HtmlPage
from vweb.htmltable import HtmlTable
from vweb.html import *

class Containers(HtmlPage):
    def __init__(self):
        HtmlPage.__init__(self, 'Order Containers')
        self.javascript_src = [
            '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js',
            'js/containers.js']
        self.style_sheets = ['css/order_form.css']

    def getHtmlContent(self):
        return \
            self.getHeader() + \
            self.getBody() + \
            self.getFooter()

    def getHeader(self):
        return div(img(src='images/landis_header.jpg'),
                   class_='header')

    def getBody(self):
        return div(
            self.getMenu() + \
            self.getOrderForms(),
            class_='pageBody')

    def getMenu(self):
        return ''
        #return div(
        #    '[menu]',
        #    class_='menu')

    def getOrderForms(self):
        from containers_form1 import ContainersForm1
        from containers_form2 import ContainersForm2
        from containers_form3 import ContainersForm3
        return \
            ContainersForm1().get() + \
            ContainersForm2().get() + \
            ContainersForm3().get()

    def getFooter(self):
        return ''
        #return div(
        #    p('© 2014 Landis Refining Co, Inc., All Rights Reserved'),
        #    class_='footer')

Containers().go()
