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
        return \
            self.getOrderForm1() + \
            self.getOrderForm2() + \
            self.getOrderForm3()

    def getOrderForm1(self):

        intro = p('Please choose the option that best describes you:')

        # customer_type
        ctvalues = {1: 'Dentist',
                    2: 'Dentist Staff',
                    3: 'Patient',
                    4: 'Jeweler'}
        ctbuttons = []
        for k,v in ctvalues.items():
            ctbuttons.append(input(type='radio', 
                                   name='customer_type', 
                                   value=k) + v + br())
        customer_type = div('\n'.join(ctbuttons),
                            id='customer_type') + br()

        # dentist name
        dentist_name = span('Dentist Name: ' +\
                           input(type='textfield', name='dentist_name'),
                           id='dentist_name_container')

        # dentist phone
        dentist_phone = span('Dentist Phone: ' +\
                            input(type='textfield', name='dentist_phone'),
                            id='dentist_phone_container')

        # dentist info
        dentist_info = div('<br>'.join([dentist_name,
                                        dentist_phone]),
                           id='dentist_info') + br()

        # next
        next1 = span('Next>', id='next1', class_='textButton')

        # put it together
        return div(''.join([intro,
                            customer_type,
                            dentist_info,
                            next1]),
                   id='order_form1')

    def getOrderForm2(self):
        intro = p('What container types do you want?:')


        single_jar  = input(type='textfield', name='single_jar', size=5)
        multiple_jars  = input(type='textfield', name='multiple_jars', size=5)
        patient_scrap_mailer  = input(type='textfield', 
                                      name='patient_scrap_mailer', size=5)

        table = HtmlTable()
        table.addHeader(['Quantity', 'Container type'])
        table.addRow([single_jar, 'Single Jars']);
        table.addRow([multiple_jars, 'Multiple Jars']);
        table.addRow([patient_scrap_mailer, 'Patient Scrap Mailer'])

                     
        # next/prev
        prev2 = span('&lt;Prev', id='prev2', class_='textButton')
        next2 = span('Next>', id='next2', class_='textButton')

        return div(''.join([intro,
                            table.getTable(),
                            prev2 + ' | ' + next2]),
                   
                   id='order_form2')

    def getOrderForm3(self):
        intro = p('Your address information')

        name = 'Your Name: ' + input(type='textfield', name='name') + br()

        business_name = 'Business Name: ' + \
            input(type='textfield', name='bussiness_name') + br()

        address = 'Address: ' + input(type='textfield', name='address') + br()

        # next/prev
        prev3 = span('&lt;Prev', id='prev3', class_='textButton')

        return div(''.join([intro,
                            name,
                            business_name,
                            address,
                            prev3]),
                   
                   id='order_form3')

    def getFooter(self):
        return ''
        #return div(
        #    p('© 2014 Landis Refining Co, Inc., All Rights Reserved'),
        #    class_='footer')

Containers().go()
