# -*- coding: utf-8 -*-
import mechanize
# import sys, logging
#
# logger = logging.getLogger("mechanize")
# logger.addHandler(logging.StreamHandler(sys.stdout))
# logger.setLevel(logging.DEBUG)

class SendData(object):
    def __init__(self, person):
        self.booking_number = person.booking_number
        self.name = person.name
        self.last_name = person.last_name
        self.sex = person.sex
        self.passport_number = person.passport_number
        self.delivery_needed = person.delivery_needed
        self.citizenship = person.citizenship
        self.birth_date = person.birth_date
        self.entry_date = person.entry_date
        self.exit_date = person.exit_date
        self.kids = person.kids
        self.transport = person.transport
        self.email = person.email
        self.address = person.address
        self.cities = person.cities
        self.if_double = person.if_double
        self.html = None
        self.br = mechanize.Browser()


    def open_page(self,page):
        r = self.br.open(page)
        self.html = r.read()


    def fill_data(self):
        self.br.set_handle_equiv(True)
        self.br.set_handle_gzip(True)
        self.br.set_handle_redirect(True)
        self.br.set_handle_referer(True)
        self.br.set_handle_robots(False)

        self.br.addheaders = [
            ('User-agent',
             'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) '
             'Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

        last_items = 3  # how many items should we get
        #login
        self.open_page('http://travelrussia.su/en/login.php')
        self.br.select_form(nr=0)
        self.br.form['email'] = 'cubahostel@gmail.com'
        self.br.form['password'] = '67be1'

        self.br.submit()

        if self.delivery_needed:
            delivery = '40'
        else:
            delivery = '53'
        self.open_page('http://travelrussia.su/en/visa.tourist.php')




        self.br.select_form(nr=0)
        self.br.form['citizenship'] = [str(self.citizenship), ]
        self.br.form['supplier2'] = [delivery, ]
        # self.br.form['da_country'] = [delivery_country,]
        # self.br.form['da_zip'] = [zip_index]
        # self.br.form['da_city'] = [city]
        # self.br.form['da_address'] = [address]
        # self.br.form['da_phone'] = [phone]
        self.br.form['sex'] = [self.sex, ]
        self.br.form['firstname'] = self.name
        self.br.form['lastname'] = self.last_name
        if len(str(self.birth_date.day)) == 2:
            self.br.form['bdd'] = [str(self.birth_date.day),]
        else:
            self.br.form['bdd'] = ['0' + str(self.birth_date.day)]
        if len(str(self.birth_date.month)) == 2:
            self.br.form['bdm'] = [str(self.birth_date.month),]
        else:
            self.br.form['bdm'] = ['0' + str(self.birth_date.month)]
        self.br.form['bdy'] = str(self.birth_date.year)
        self.br.form['passportnumber'] = self.passport_number
        self.br.form.find_control('visaissues').readonly = False
        self.br.form['visaissues'] = str(self.entry_date)
        self.br.form.find_control('visaexpires').readonly = False
        self.br.form['visaexpires'] = str(self.exit_date)
        self.br.form['city1'] = ['2',]
        self.br.form.find_control('hchoise1').readonly = False
        self.br.form['hchoise1'] = 'Cuba Hostel'
        # self.br.submit()

