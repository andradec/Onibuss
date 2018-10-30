import scrapy

import Itinerario from Onibus
import Horario from Onibus
import Linhas from Onibus

class Segmento(scrapy.Item):
  
    Nome = scrapy.Field()
    Logradouro = scrapy.Field()
    sequencia = scrapy.Field()
    Horario = Horario.Hora
    Linha = Nome.Linhas
  



