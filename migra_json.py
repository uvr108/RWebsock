import json
import rethinkdb as r

rt_host='127.0.0.1'
rt_port='28015'
rt_db='csn'

conn = r.connect(host=rt_host, port=rt_port, db=rt_db)

with open('triggers.json') as f:
    data = json.load(f)


for js in data:
    out={} 
    
    for p,k in js.items():
        if p=='action':
            out.update({p:k.replace(' ','')})
        elif p=='ano_sfile':
            out.update({p:k})
        elif p=='dep':
            out.update({p:float(k)})
        elif p=='dia_sfile':
            out.update({p:k})
        elif p=='email_origen':
            if k is None:
                out.update({p:None})
            else:
                out.update({p:float(k)})
        elif p=='fecha_utc':
            k=k.replace(' ','T')
            k=k.replace('/','-')
            out.update({'fecha_origen':r.iso8601(k+'+00:00')}) 
        elif p=='latitud':
            out.update({p:float(k)})
        elif p=='longitud':
            out.update({p:float(k)})
        elif p=='m1_magnitud':
            out.update({p:float(k)})
        elif p=='m1_tipo':
            out.update({p:k})
        elif p=='m20':
            out.update({p:k})
        elif p=='m5':
            out.update({p:k})
        elif p=='no':
            out.update({p:int(k)})
        elif p=='operator':
            out.update({p:k})
        elif p=='pup':
            out.update({p:k})
        elif p=='retardo':
            out.update({p:float(k)})
        elif p=='sfile':
            out.update({p:k})
        elif p=='tipo_estadistica':
            out.update({p:k})
        elif p=='version':
            out.update({p:int(k)})
        elif p=='origen':
            out.update({p:"seisan2"})
        elif p=='no':
            out.update({p:int(k)})
    
    r.table('triggers').insert(out).run(conn)

    #conn.close() 
