import json
import rethinkdb as r

with open('triggers.json') as f:
    data = json.load(f)

keys = ["action","ano_sfile","dep","dia_sfile","email_origen","epoch","fecha_utc","id","latitud","longitud","m1_magnitud","m1_tipo","m20","m5","mes_sfile","no","operator","origen","pup","retardo","sensible","sfile","tipo_estadistica","version"]

for js in data:
    out={} 
    
    """
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
        elif p=='origen':
            out.update({p:k})
        elif p=='pup':
            out.update({p:k})
        elif p=='retardo':
            out.update({p:float(k)})
        elif p=='sfile':
            out.update({p:k})
        elif p=='tipo_estadistica':
            out.update({p:k})
    """
    for p,k in js.items():
        if p=='action':
            out.update({p:k.replace(' ','')})
        elif p=='version':
            out.update({p:k*1})
    print(out) 
