# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from Onibus import Itinerario
from Onibus import Linhas


class PrincipalSpider(CrawlSpider):

    name = 'Principal'
    allowed_domains = ['www.ctaonline.com.br']
    start_urls = [
        'http://http://www.ctaonline.com.br/index.php/linhas.html/'
    ]

    rules = (
        Rule(
            LinkExtractor(allow='index.php/')
        ),
        Rule(
            LinkExtractor(allow='index.php/'            
            ), callback = 'parse_conference'
        )
    )

    def parse_conteudo(self, response):




    