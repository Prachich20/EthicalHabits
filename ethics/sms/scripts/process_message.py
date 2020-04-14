import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'ethics.settings'
import django

django.setup()
import ethics.settings as settings

import spacy
from sms.models import Sms

nlp = spacy.load('en_core_web_sm')
from phone_iso3166.country import *

from company.models import CompanyNumber, Company, Category
from master.models import MasterData

companyname = settings.PRODUCT_NAME
companies = Company.objects.filter(name=companyname)
categories = Category.objects.all()


def get_category(body):
    for cat in categories:
        if cat.keywords:
            names = [x.strip(' ') for x in cat.keywords.lower().split(',')]
            clean_body = [y.strip(' ') for y in body.split(' ')]
            has_category = set(names).intersection(clean_body)
            if len(has_category) > 0:
                return cat


def get_location(ents):
    name = location = ''
    # Create list of word tokens
    entities = [(i, i.label_, i.label) for i in ents]
    if len(entities) > 0:
        for entity in entities:
            if entity[1] == settings.PERSON:
                name = entity[0]
            if entity[1] == settings.GPE:
                location = entity[0]
    return name, location


def run():
    if companies:
        for com in companies:
            print("extract starting for {}".format(com.subgroup))
            subgroup = Company.objects.filter(name=companyname, subgroup=com.subgroup).first()
            phonenumbers = CompanyNumber.objects.filter(company_id=subgroup.id)
            for number in phonenumbers:
                num = number.number.replace('-', '').replace(' ', '').strip()
                smses = Sms.objects.filter(message_to=num, direction=settings.INBOUND)
                for sms in smses:
                    print(sms.sid)
                    master = MasterData.objects.filter(sid=sms.sid).first()
                    if not master:
                        my_doc = nlp(sms.body)
                        category = get_category(sms.body)
                        name, location = get_location(my_doc.ents)
                        print(sms.sid)

                        masterdata = MasterData()
                        masterdata.sid = sms.sid
                        masterdata.name = name
                        masterdata.location = location
                        masterdata.country = phone_country(sms.message_from)
                        masterdata.company = subgroup
                        masterdata.body = sms.body
                        masterdata.category = category
                        masterdata.critical = category.critical if category else None
                        masterdata.contact_num = sms.message_from
                        masterdata.contact_service = sms.from_service
                        masterdata.direction = sms.direction
                        masterdata.sms = sms
                        masterdata.status = sms.status
                        masterdata.date_received = sms.created
                        masterdata.account_sid = sms.account_sid
                        masterdata.to_service = sms.to_service
                        masterdata.message_to = sms.message_to
                        masterdata.save()
                        print(f"{masterdata.sid} created")


if __name__ == '__main__':
    run()
    print('completed')
