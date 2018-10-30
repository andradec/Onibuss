# -*- coding: utf-8 -*-
import scrapy

class LinhasSpider(scrapy.Spider):

    name = 'Linhas'    
    start_urls = ['http://www.ctaonline.com.br/index.php/linhas.html']

    def parse_links(self, response):
        empresa = response.xpath('//div[contains(@class, "grid3 column first last ex-odd multi-module-column sidebar-a")]')
        for cat in empresa:
            teste = cat.xpath('//div[contains(@class, "block module")]/div[contains(@class, "content")]/ul/li/a')            
            for li in teste:
                link = li.xpath('./@href').extract_first()
                yield scrapy.Request (
                    url =  link,
                    callback=self.parse_paginas
                )
    def parse_paginas(self, response, url):
        
        yield scrapy.Request(
            'http://www.ctaonline.com.br%s' %url, 
            callback=self.parse_conteudo
        )
                      
        
            # yield scrapy.Request(
            #     link = 'http://www.ctaonline.com.br%s' % link,               
            #     callback=self.parse_category
            # )

            # yield scrapy.Request(
            #     link = next_page.extract_first(), callback = self.parse_links
            # )
            
    def parse_conteudo(self, response):

        ##pagina toda
        itinerarios = response.xpath('//*[@id="component"]/div/article/section[2]/div/div/div/div/div/div/div/div/div')    
        ##titulo
        title = response.xpath('//*[@id="component"]/div/article/header/h1/a/text()').extract_first()

        ##Rotas
        for iot in itinerarios:
            rota = iot.xpath('//div[contains(@class, "wpb_wrapper")]/p')
            for iott in rota:
                Rotas = iott.xpath('./text()').extract_first()
                if Rotas != None:
                    print(Rotas)

        ##Organização dos Horários
        for p in itinerarios:
            var = p.xpath('.//p')
            for pp in var:
                organiza_horarios = pp.xpath('.//span/text()').extract()
                print(organiza_horarios)

        ##Recuperação de Horários
        for p in itinerarios:
            var = p.xpath('.//table')
            for pp in var:
                var1 = pp.xpath('.//tr')
                for ppp in var1:
                    horarios = ppp.xpath('.//td/span/text()').extract()
                    print(horarios)

        yield {
            'title': title,
            'Rotas': Rotas,
            'Organização de Horários': organiza_horarios,
            'Horários': horarios,
        }

    # for iot in itinerarios:
    #     teste = iot.xpath('//div[contains(@class, "wpb_wrapper")]/p[1]/text()').extract_first()

