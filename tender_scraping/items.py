# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class tenderAd(scrapy.Item):
    # define the fields for your item here like:
    ad_id = scrapy.Field()
    title = scrapy.Field()
    purchase_form = scrapy.Field()
    purchase_kind = scrapy.Field()

    pub_date = scrapy.Field()
    start_date = scrapy.Field()
    end_date = scrapy.Field()
    lots_nb = scrapy.Field()
    ad_amount = scrapy.Field()
    status = scrapy.Field()
    
    link = scrapy.Field()
    
    purchase_type = scrapy.Field()
    incomplete_way = scrapy.Field()
    
    organizer = scrapy.Field()
    org_legal_adress = scrapy.Field()
    
    org_repname = scrapy.Field()
    org_reppos = scrapy.Field()
    org_phone = scrapy.Field()
    org_email = scrapy.Field()
    org_bankcred = scrapy.Field()
    org_creator = scrapy.Field()

    invited_supplier = scrapy.Field()
    priznak = scrapy.Field()

    lot_link = scrapy.Field()
    
class tenderLot(scrapy.Item):
    # define the fields for your item here like:
    ad_id = scrapy.Field()

    lot_id = scrapy.Field()
    lot_organizer = scrapy.Field()
    lot_name = scrapy.Field()
    lot_addcharact = scrapy.Field()

    lot_status = scrapy.Field()
    lot_BIN_organizer = scrapy.Field()
    lot_organizer = scrapy.Field()
    lot_TRUcode = scrapy.Field()
    lot_TRUname = scrapy.Field()
    lot_finsource = scrapy.Field()
    lot_advperc = scrapy.Field()
    lot_deladdress = scrapy.Field()
    lot_deldate = scrapy.Field()
    lot_incoterms = scrapy.Field()

    lot_incoterms = scrapy.Field()
    lot_itemprice = scrapy.Field()
    lot_quantity = scrapy.Field()
 
    lot_repname = scrapy.Field()
    lot_reppos = scrapy.Field()
    lot_repphone = scrapy.Field()
    lot_repemail = scrapy.Field()
    lot_bankreq = scrapy.Field()
    
class tenderDoc(scrapy.Item):
    # define the fields for your item here like:
    ad_id = scrapy.Field()
    
    doc_name = scrapy.Field()
    doc_obligatory = scrapy.Field()