import socketserver
import os
import json

import asyncio

sk_host=os.environ['sk_host']
sk_port=os.environ['sk_port']

from collector import ejecuta 

class RWebsock(socketserver.StreamRequestHandler):

    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        self.data = self.rfile.readline().strip()
        print("{} wrote:".format(self.client_address[0]))
        # Likewise, self.wfile is a file-like object used to write back
        # to the client
       
 
        if self.data == b'':
            pass
        else: 
            self.wfile.write(b'Que grande eres Uli !!!')
            vector =  self.data.decode('utf8').split('|')
        
            print(vector)
            
            if vector[0] == 'ingresar':

                dictio = {'version': vector[1], 'epoch':vector[2],'action':vector[3],'operator':vector[4]}
                dictio.update({'retardo':vector[5],'email_origen':vector[6],'sensible':vector[7],'sfile':vector[8]})
                dictio.update({'tipo_estadistica':vector[9],'latitud':vector[10],'longitud':vector[11],'dep':vector[12],'m1_magnitud':vector[13],'m1_tipo':vector[14]})
                dictio.update({'fecha_origen':vector[15],'ano_sfile':vector[16],'mes_sfile':vector[17],'dia_sfile':vector[18],'pup':vector[19],'m5':vector[20],'m20':vector[21]})
                dictio.update({'origen':vector[22],'no':vector[23]})

            elif vector[0] == 'modificar':

                dictio = {'sf':vector[1], 'yr':vector[2], 'mo':vector[3], 'tipo':vector[4], 'email':vector[5], 'delay':vector[6], 'sensible':vector[7]} 
            
            asyncio.run(ejecuta(vector[0], {vector[0]: dictio}))

if  __name__ == "__main__":



    HOST, PORT = sk_host , int(sk_port) 

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), RWebsock) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
   


