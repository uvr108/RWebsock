from rthkdb.continuos import Continuos
import rethinkdb as r

import os

if __name__ == "__main__":


    """

    [indice] OR [between]

    """

    kw = {'message':{'table': 'triggers', 'option': 'select'}}

    """

    indice = {'anomes':[2019,5]}

    val = [*indice.values()][0]
    inx = [*indice.keys()][0]
    ind = [val,inx]

    kw['message'].update({'indice': ind}) 
    """

    """    
    between = {'anomes':[[2019,3],[2019,4]]}  

    val = [*between.values()][0]
    inx = [*between.keys()][0]
    bet = [val[0],val[1],inx]
    
    kw['message'].update({'between': bet})

    """

    """
    betweenISO = {'fecha_origen':['2019-04-01T00:00:00+00:00','2019-04-01T23:59:59+00:00']}  

    val = [*betweenISO.values()][0]
    inx = [*betweenISO.keys()][0]
    iso = [val[0],val[1],inx]

    kw['message'].update({'betweenISO': iso})
 
    """

    order = {'sfile':'desc','version':'desc'}
    key = [*order.keys()]
    val = [*order.values()]

    print(key)
    print(val)

    # print(kw)

    """  
    cons = Continuos()
    data = cons.ejecutar(kw)
    del(cons)

    for d in data:
        print(d)
    """

