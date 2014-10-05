from vweb.htmltable import HtmlTable
from vweb.html import *

class ContainersForm2(object):

    def get(self):
        intro = p('What container types do you want?:', id='form2Intro')

        single_jar = input(type='textfield', name='single_jar', size=5)
        single_jar_text = span('Single Jar', id='single_jar_text')

        multiple_jars = input(type='textfield', name='multiple_jars', size=5)
        multiple_jars_text = span('Multiple Jars', id='multiple_jars_text')

        patient_scrap_mailer = input(type='textfield', 
                                     name='patient_scrap_mailer', size=5)
        patient_scrap_mailer_text = span('Patient Scrap Mailer', 
                                         id='patient_scrap_mailer_text')

        table = HtmlTable()
        table.addRow(['Qty'               , 'Container type'])
        table.addRow([single_jar          , single_jar_text])
        table.addRow([multiple_jars       , multiple_jars_text])
        table.addRow([patient_scrap_mailer, patient_scrap_mailer_text])
                     
        # next/prev
        prev2 = span('&lt;Prev', id='prev2', class_='textButton')
        next2 = span('Next>', id='next2', class_='textButton')

        return div(''.join([intro,
                            table.getTable(),
                            prev2 + ' | ' + next2]),
                   
                   id='order_form2')

