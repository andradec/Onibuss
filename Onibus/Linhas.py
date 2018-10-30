import scrapy
import Empresa from Onibus 
import Linhas from Onibus 

class Linhas(scrapy.Item):
 
    Nome = scrapy.Field()
    CNPJ = Empresa.CNPJ
    Nome = Linhas.Nome
  

