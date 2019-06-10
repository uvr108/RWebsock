from rthkdb.continuos import Continuos
import rethinkdb as r

import os

if __name__ == "__main__":


    """

    [indice] OR [between]

    {
     'table': 'ratio','option': 'select',
     'between': {'yrjl':[['2019', '001'], ['2019', '015']]},
     'order': 'yrjl',
     'pluck': ['yr', 'jl', {'data': ['Norte', 'N.Chico', 'Valpo', 'Zona.C', 'Sur', 'Ext.S']}]
     }


    """

    kw = {'message':{'table': 'informes', 'option': 'select'}}

    """

    indice = {'anomes':[2019,5]}

    val = [*indice.values()][0]
    inx = [*indice.keys()][0]
    ind = [val,inx]

    kw['message'].update({'indice': ind})
    """
    """
    between = [['2019','001'],['2019','015'],'yrjl']

    kw['message'].update({'between': between})
    """
    """

    betweenISO = ['2019-05-27T00:00:00+00:00','2019-05-27T23:59:59+00:00', 'fecha_origen']

    kw = {'message':{'table': 'triggers', 'option': 'select'}}
    kw['message'].update({'betweenISO': betweenISO})
    """



    """

    order = []
    orden = {'yrjl':'desc'}

    for k,v in orden.items():
        order.append(getattr(r,v)(k))



    """

    """
    kw = {'message':{'table': 'ratio', 'option': 'select'}}
    kw['message'].update({'get_julian': [['2019-01-01','2019-01-07'],'yrjl']})
    """

    """

    where = {'sfile': '31-2330-10L.S201901'}

    kw['message'].update({'where': where})

    """
    """

    kw['message'].update({'pluck': ['yr', 'jl', {'data': ['Norte', 'N.Chico', 'Valpo', 'Zona.C', 'Sur', 'Ext.S']}]})
    """

    """
    kw['message'].update({'order': order})
    kw['message'].update({'limit': 30})
    kw['message'].update({'distinct': True})

    """

    kw['message'].update({'pluck':['fecha_origen','zona']})
    # kw['message'].update({'limit': 100})
    # kw['message'].update({'or':{'zona':['Norte','N.Chico','Zona.C','Sur','Valpo','Ext.S']}})
    kw['message'].update({'or':{'zona':['Valpo']}})

    cons = Continuos()

    data = cons.ejecutar(kw)
    del(cons)

    for d in data:
        print(d)
