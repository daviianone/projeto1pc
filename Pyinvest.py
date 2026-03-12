import math
import random
import datetime
import statistics
import locale
locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')
capital = float(input('capital inicial: '))
aporte = float(input('Aporte mensal'))
meses = float(input('Prazo(meses): '))
cdi_anual = float(input('CDI Anual%:'))/100
perc_cdb = float(input('Percentual do CDI- CDB(&): '))/100
perc_Lci= float(input('percentual do CDI - LCI (&): '))/100
taxa_fii= float(input('rentabilidade do FII(&): '))/100
meta = float(input(Meta financeira (R$): '))
#conversao CDI
cdi mensal= math.pow(1=cdi_anual), 1/12) -1
#total investido
total_investido = capital + (aporte *meses)
#CDB
taxa cdb = cdi_mensal *perc_cdb
montante+cdb = (capital *math.pow(1+taxa_cdb), meses))+(aporte *meses)
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb *0.085)

#LCI
taxa_lci = cdi_mensal *perc_Lci
montante_lci= (capital * math.pow((1+taxa_lci),meses))+(aporte * meses)

#poupança
taxa_poupança = 0.005
montante_poupança = (capital * math.pow((1+taxa_poupança), meses))+(aporte * meses)

