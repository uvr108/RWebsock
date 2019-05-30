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
            
            if vector[0] == 'ingresar':

                dictio = {'version': vector[1], 'epoch':vector[2],'action':vector[3],'operator':vector[4]}
                dictio.update({'retardo':vector[5],'email_origen':vector[6],'sensible':vector[7],'sfile':vector[8]})
                dictio.update({'tipo_estadistica':vector[9],'latitud':vector[10],'longitud':vector[11],'dep':vector[12],'m1_magnitud':vector[13],'m1_tipo':vector[14]})
                dictio.update({'fecha_origen':vector[15],'pup':vector[16],'m5':vector[17],'m20':vector[18]})
                dictio.update({'origen':vector[19],'no':vector[20]})

            elif vector[0] == 'modificar':

                dictio = {'sf':vector[1],'tipo':vector[2],'email':vector[3],'delay':vector[4],'sensible':vector[5]}
            
            asyncio.run(ejecuta(vector[0], {vector[0]: dictio}))

if  __name__ == "__main__":



    HOST, PORT = sk_host , int(sk_port) 

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), RWebsock) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
   


