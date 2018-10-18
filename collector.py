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


async def collector(r,data):

    # logging.basicConfig(level=logging.DEBUG, filename="/home/ulises/RWebsock/logfile", filemode="a+",
    #                    format="%(asctime)-15s %(levelname)-8s %(message)s")
    #print("COLLECTOR : ",data)

    # logging.info('COLLECTOR %s' % data)

    bdata = data.decode('utf8').split('|') 
    #print("DBDATA : ",bdata)

    if dbdata[0] == 'version':
     
        sfile = bdata[1]
        yr = bdata[2]
        mo = bdata[3]
        tipo = bdata[4]
        email = bdata[5]
        delay = bdata[6]
        sensible = bdata[7]

        if sensible == 'no':
            if email == 'no' and sensible == 'no':
                kw={'table':'triggers','get_all':{'flag':'count','where': {'sfile': sfile },'indice':{'anomes':{'ano_sfile': int(yr), 'mes_sfile': int(mo)}}}};

            elif email == 'yes' and sensible == 'no':
                where = {'sfile': sfile,'tipo_estadistica':tipo }

                if tipo == 'final':

                    where.update({'pup':'yes'})
                kw={'table':'triggers','update':{'setea':{'email_origen': delay}, 'where': where,'indice':{'anomes':{'ano_sfile': int(yr), 'mes_sfile': int(mo)}}}};

        elif sensible == 'yes':

            kw={'table':'triggers','update':{'setea':{'sensible': 'yes'}, 'where': { 'sfile': sfile,'tipo_estadistica': 'final', 'pup' : 'yes' },'indice':{'anomes':{'ano_sfile': int(yr), 'mes_sfile': int(mo)}}}}


    elif dbdata[0] == 'preliminar':

        nombre = dbdata[1]
        yr = bdata[2]
        mo = bdata[3]
        
        kw={'table':'triggers','get_all':{'flag':'count','where': {'sfile': nombre,'tipo_estadistica':'preliminar' },'indice':{'anomes':{'ano_sfile': int(yr), 'mes_sfile': int(mo)}}}};

    cons = Continuos()

    cons.ejecutar(r,**kw)
    output=cons.output
    cons.__del__()

    return str(output).encode('utf8')


if __name__ == "__main__":

    pass


