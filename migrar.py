import psycopg2
import rethinkdb as r
import os

rt_host=os.environ['rt_host']
rt_port=os.environ['rt_port']
rt_db=os.environ['rt_db']

conn_r = r.connect(host=rt_host, port=rt_port, db=rt_db)
print(conn_r)

try:
    connect_str = "dbname='publico' user='sysop' host='10.54.217.83'"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    # create a new table with a single column called "name"
 
    sql = """

          select sfile,
          t.nombre as tipo,
          latitud,
          longitud,
          dep,
          m1_magnitud as mag,
          m1_tipo,
          email_origen,
          fecha_origen,
          extract(year from fecha_origen) as ano_sfile,
          extract(month from fecha_origen) as mes_sfile,
          pub_origen,
          action,
          opera,
          version,
          s.nombre as sensible,
          pup,
          m20,
          m5,
          estaciones 
          from eventos , sensible s, tipo_estadistica t
          where s.sensible=sensible_fk
          and t.tipo_estadistica = tipo_estadistica_fk
          order by fecha_origen desc;

    """

    cursor.execute(sql)
    # run a SELECT statement - no data in there, but we can try it
    for row in cursor.fetchall():

        js = {"sfile":row[0]}
        js.update({"tipo_estadistica":row[1]})
        js.update({"latitud":row[2]})
        js.update({"longitud":row[3]})
        js.update({"dep":row[4]})
        js.update({"m1_magnitud":row[5]})
        js.update({"m1_tipo":"%s" % row[6]})
        if row[7] is None:
            js.update({"email_origen":None})
        else:
            js.update({"email_origen":row[7]})
        js.update({"fecha_origen":r.iso8601(str(row[8]).replace(' ','T')+"+00")})
        js.update({"ano_sfile":int(row[9])})  
        js.update({"mes_sfile":int(row[10])})  
        js.update({"retardo":row[11]})
        js.update({"action":"%s" % row[12].replace(' ','')})
        js.update({"operator":"%s" % row[13]})
        js.update({"version":int(row[14])-1})
        if row[15]=='Si':
            js.update({"sensible":'yes'})
        else:
            js.update({"sensible":None})
        if row[16]=='s':
            js.update({"pup":"yes"})
        else:
            js.update({"pup":None})
        if row[17]=='s':
            js.update({"m20":"yes"})
        else:
            js.update({"m20":None})
        if row[18]=='s':
            js.update({"m5":"yes"})
        else:
            js.update({"m5":None})
        js.update({"origen":"seisan"}) 
        js.update({"no":row[19]}) 
        print(js) 
        r.table("prueba").insert(js).run(conn_r)
       
      
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)

conn.close() 

conn_r.close()
