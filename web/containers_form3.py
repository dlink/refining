from vweb.htmltable import HtmlTable
from vweb.html import *

class ContainersForm3(object):

    def get(self):
        intro = p('Your address information')

        fields = ['Your Name',
                  'Business Name',
                  'Address',
                  'City',
                  'State',
                  'Zip',
                  'Contact Name',
                  'Email Address',
                  'Confirm Email Address',
                  'Phone Number']

        table = HtmlTable()
        for field in fields:
            name=field.lower().replace(' ', '_')
            description_name = '%s_text' % name
            description = span(field, id=description_name)
            table.addRow([description, input(type='textfield', name=name, 
                                             size=50)])

        # next/prev
        next3 = span('Next>', id='next3', class_='textButton')
        prev3 = span('&lt;Prev', id='prev3', class_='textButton')

        return div(''.join([intro,
                            table.getTable(),
                            prev3 + ' | ' + next3]),
                   
                   id='order_form3')

