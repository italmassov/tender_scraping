#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 22:18:18 2017

@author: kuanysh
"""
import scrapy
from tender_scraping.items import tenderAd, tenderLot, tenderDoc
import urlparse

class tenderSpider(scrapy.Spider):
    name = "tender"

    def start_requests(self):
        urls = [
            'https://v3bl.goszakup.gov.kz/ru/searchanno',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def text_strip(self, txt):
        txt = ''.join(txt).replace('\n','').strip()
        while '  ' in txt:
            txt = txt.replace('  ', ' ')
            
        return txt 
        

    def parse(self, response):
        rows = response.xpath('//table[contains(@class, "table-bordered")]/descendant::tr')
        print 'rows', len(rows)
        
        for row in rows:
            item = tenderAd()
            item['ad_id'] = self.text_strip(row.xpath('./td[1]/text()').extract())
            item['organizer'] = self.text_strip(row.xpath('./td[2]/text()').extract())
            item['title'] = self.text_strip(row.xpath('./td[3]/descendant::text()').extract())
            item['purchase_form'] = self.text_strip(row.xpath('./td[4]/text()').extract())
            item['purchase_kind'] = self.text_strip(row.xpath('./td[5]/text()').extract())
            item['start_date'] = self.text_strip(row.xpath('./td[6]/text()').extract())
            item['end_date'] = self.text_strip(row.xpath('./td[7]/text()').extract())
            item['lots_nb'] = self.text_strip(row.xpath('./td[8]/text()').extract())
            item['ad_amount'] = self.text_strip(row.xpath('./td[9]/text()').extract())
            item['status'] = self.text_strip(row.xpath('./td[10]/text()').extract())
            item['link'] = urlparse.urljoin(response.url, self.text_strip(row.xpath('./td[3]/a/@href').extract()))
            
            # parse link for additional data
            item = scrapy.Request(url=item['link'], callback=self.parse_link, 
                           meta={'item':item})

            yield item

        return
        
    def parse_link(self, response):
        item = response.meta['item']

        desc_dict = {'purchase_type': u"Тип закупки", 'incomplete_way': u'Способ несостоявшейся закупки', 
        'org_legal_adress': u'Юр. адрес организатора', 'org_repname': u'ФИО представителя',
        'org_reppos':u"Должность", 'org_phone':u"Контактный телефон", 'org_email': "E-Mail", 
        'org_bankcred':u"Банковские реквизиты", 'org_creator': u"Создатель объявления	",
        'invited_supplier':u"Приглашенный поставщик", 'priznak':u"Признаки"}
        
        for curKey in desc_dict.keys():
            item[curKey] = self.text_strip(response.xpath(u"//th[text()='%s']/following-sibling::td[1]/text()" % desc_dict[curKey]).extract())
        
        # collect lots
        lot_link = urlparse.urljoin(response.url, '?tab=lots')
        item['lot_link'] = lot_link
                         
        lots = scrapy.Request(url=item['lot_link'], callback=self.parse_lots, meta={'ad_id':item['ad_id']})

        return item, lots 

    def parse_lots(self, response):
        lotRows = response.xpath('//table[contains(@class, "table-striped")]/tr')
        
        lots = []
        for lotRow in lotRows:
            lot = tenderLot()
            lot['ad_id'] = response.meta['ad_id']
        
            lots.append(lot)
            
        return lots