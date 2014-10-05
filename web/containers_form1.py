from vweb.html import *

class ContainersForm1(object):

    def get(self):

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

