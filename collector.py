import socketserver
import rethinkdb as r
import os
import json
import asyncio

from rthkdb.continuos import Continuos

rt_host=os.environ['rt_host']
rt_port=os.environ['rt_port']
rt_db=os.environ['rt_db']

def isNone(v, func=None):

    if v=='None':
        return None 
    else:
        if func == None:
            return v
        else:
            return comandos.get(func)(v) 

def isTrue(v):
    if v == 'true':
        return True;
    else:
        return None;

async def sensible(dictio):

    dictio['yr'] = isNone(dictio['yr'],'int') 
    dictio['mo'] = isNone(dictio['mo'],'int') 

    con = Continuos()
    con.ejecutar({'message':{'table':'analisis','option':'sensible', 'dictio': dictio}})
    del(con)   

async def modificar(dictio):

    # 'dictio': {'sfile': '11-1607-03L.S201906', 'yr': '2019', 'mo': '6', 'tipo_estadistica': 'preliminar', 'email_origen': '10.9', 'sensible': 'None'}

    dictio['yr'] = isNone(dictio['yr'],'int') 
    dictio['mo'] = isNone(dictio['mo'],'int') 
    dictio['email_origen'] = isNone(dictio['email_origen'],'float')
    dictio['sensible'] = isTrue(dictio['sensible'])
 
    con = Continuos()
    con.ejecutar({'message':{'table':'analisis','option':'update', 'dictio': dictio}})
    del(con)   

async def ingresar(dictio):

    dictio['version'] = isNone(dictio['version'],'int')
    dictio['epoch'] = isNone(dictio['epoch'],'int')
    dictio['no'] = isNone(dictio['no'],'int')
   
    dictio['retardo'] = isNone(dictio['retardo'],'float')
    dictio['email_origen'] = isNone(dictio['email_origen'],'float')
    dictio['latitud'] = isNone(dictio['latitud'],'float')
    dictio['longitud'] = isNone(dictio['longitud'],'float')
    dictio['dep'] = isNone(dictio['dep'],'float')
    dictio['m1_magnitud'] = isNone(dictio['m1_magnitud'],'float')
    dictio['up'] = isNone(dictio['up'],'int')
    
    dictio['fecha_origen'] = r.iso8601(dictio['fecha_origen'])

    dictio['ano_sfile'] = isNone(dictio['ano_sfile'],'int')
    dictio['mes_sfile'] = isNone(dictio['mes_sfile'],'int')
    dictio['dia_sfile'] = isNone(dictio['dia_sfile'],'int')

    dictio['m5'] = isTrue(dictio['m5'])
    dictio['m20'] = isTrue(dictio['m20'])
    dictio['sensible'] = isTrue(dictio['sensible'])

    dictio['operator'] = dictio['operator'].strip()
    
    con = Continuos()
    # print(dictio)
    con.ejecutar({'message':{'table':'analisis','option':'insert', 'dictio': dictio}})
    del(con)   

comandos = {'ingresar': ingresar, 'modificar': modificar, 'sensible': sensible, 'float': float, 'int': int}

async def ejecuta(functio,dictio):
  
    await comandos.get(functio)(dictio[functio])
 
if __name__ == "__main__":

    pass


