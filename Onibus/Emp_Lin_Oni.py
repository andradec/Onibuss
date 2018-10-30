import scrapy

import Empresa from Onibus
import Linha from Onibus
import Onibus from Onibus

class Emp_Lin_Oni(scrapy.item):

    CNPJ = Empresa.CNPJ
    Linha = Nome.Linhas
    CodOnibus = Onibus.CodOnibus