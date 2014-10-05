from vweb.html import *

class ContainersForm3(object):

    def get(self):
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

