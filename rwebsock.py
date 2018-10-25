import socketserver
import rethinkdb as r
import os
import json

import asyncio

from rthkdb.continuos import Continuos

rt_host=os.environ['rt_host']
rt_port=os.environ['rt_port']
rt_db=os.environ['rt_db']
ws_port=os.environ['ws_port']

conn = r.connect(host=rt_host, port=rt_port, db=rt_db)

from collector import main 

class RWebsock(socketserver.StreamRequestHandler):

    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        self.data = self.rfile.readline().strip()
        #print("{} wrote:".format(self.client_address[0]))
        #print(self.data)
        # Likewise, self.wfile is a file-like object used to write back
        # to the client

        if self.data == b'':
            pass
        else: 
            #self.wfile.write(collector(r,self.data))
            self.wfile.write(asyncio.run(main(r,self.data)))
            #self.wfile.write(self.data.upper())


if __name__ == "__main__":


    #collector(r,**kw)

    HOST, PORT = rt_host , int(ws_port) 

    #print(query(r,**kw))   

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), RWebsock) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
   


