import socketserver
import rethinkdb as r
import os
import json
#import logging
import asyncio

from rthkdb.continuos import Continuos

rt_host=os.environ['rt_host']
rt_port=os.environ['rt_port']
rt_db=os.environ['rt_db']

conn = r.connect(host=rt_host, port=rt_port, db=rt_db)

async def version(r,bdata,table):

    sfile = bdata[1]
    yr = bdata[2]
    mo = bdata[3]
    tipo = bdata[4]
    email = bdata[5]
    delay = float(bdata[6])
    sensible = bdata[7]

    if sensible == 'no':
        if email == 'no' and sensible == 'no':
            kw={'table':table,'get_all':{'flag':'count','where': {'sfile': sfile },'indice':{'anomes':{'ano_sfile': int(yr), 'mes_sfile': int(mo)}}}};

        elif email == 'yes' and sensible == 'no':
            where = {'sfile': sfile,'tipo_estadistica':tipo }

            if tipo == 'final':

                where.update({'pup':'yes'})
            kw={'table':table,'update':{'setea':{'email_origen': delay}, 'where': where,'indice':{'anomes':{'ano_sfile': int(yr), 'mes_sfile': int(mo)}}}};

    elif sensible == 'yes':

        kw={'table':table,'update':{'setea':{'sensible': 'yes'}, 'where': { 'sfile': sfile,'tipo_estadistica': 'final', 'pup' : 'yes' },'indice':{'anomes':{'ano_sfile': int(yr), 'mes_sfile': int(mo)}}}}

    return consultar(r,kw) 


async def preliminar(r,bdata,table):


    nombre = bdata[1]
    yr = bdata[2]
    mo = bdata[3]
      
    kw={'table':table,'get_all':{'flag':'count','where': {'sfile': nombre,'tipo_estadistica':'preliminar' },'indice':{'anomes':{'ano_sfile': int(yr), 'mes_sfile': int(mo)}}}};
    return consultar(r,kw)

async def ingresar(r,bdata,table):

    ins = {}

    for a in  bdata:
        if a == '':
            pass
        else: 
            out = a.split(':')
            if out[0] == 'ingresar':
                pass
            else:

                valor = out[1].split(';')

                if valor[0] == 'None':
                    valor[0]=None 
                elif valor[1] == 'float':
                    valor[0]=float(valor[0])
                elif valor[1] == 'int': 
                    valor[0]=int(valor[0])
                elif valor[1] == 'datetime': 
                    valor[0]=valor[0].replace(' ','T')+"+00"
                    valor[0]=valor[0].replace('=',':')
                    valor[0]=r.iso8601(valor[0])

                ins.update({out[0]:valor[0]})
    r.table(table).insert(ins).run(conn)

    return b'1'

def consultar(r,kw):

    cons = Continuos()
    cons.ejecutar(r,**kw)
    output=cons.output
    cons.__del__()

    return str(output).encode('utf8')

async def main(r,data):

    bdata = data.decode('utf8').split('|') 

    if bdata[0] == 'version':
        return await version(r,bdata,'triggers')
        #return b'1' 
    elif bdata[0] == 'preliminar':
        return await preliminar(r,bdata,'triggers')
    elif bdata[0] == 'ingresar':
        return await ingresar(r,bdata,'triggers')    


if __name__ == "__main__":

    pass


