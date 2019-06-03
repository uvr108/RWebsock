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

async def modificar(table, dictio):

    {'sf':vector[1], 'yr':vector[2], 'mo':vector[3], 'tipo':vector[4], 'email':vector[5], 'delay':vector[6], 'sensible':vector[7]} 
    print(dictio)

    where = {}
    setea = {}
    table = {}

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
    
    dictio['fecha_origen'] = r.iso8601(dictio['fecha_origen'])

    dictio['ano_sfile'] = r.iso8601(dictio['ano_sfile'],'int')
    dictio['mes_sfile'] = r.iso8601(dictio['mes_sfile'],'int')
    dictio['dia_sfile'] = r.iso8601(dictio['dia_sfile'],'int')

    dictio['m5'] = isNone(dictio['m5'])
    dictio['m20'] = isNone(dictio['m20'])
    dictio['pup'] = isNone(dictio['pup'])
    dictio['sensible'] = isNone(dictio['sensible'])

    dictio['operator'] = dictio['operator'].strip()

    con = Continuos()
    con.ingresar('triggers', dictio)
    del(con)   

comandos = {'ingresar': ingresar, 'modificar': modificar, 'float': float, 'int': int}

async def ejecuta(functio,dictio):
  
    await comandos.get(functio)(dictio[functio])
 
if __name__ == "__main__":

    pass


