from vweb.htmltable import HtmlTable
from vweb.html import *

class ContainersForm2(object):

    def get(self):
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

