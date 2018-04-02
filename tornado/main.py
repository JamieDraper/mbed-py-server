# uses tornedo websocket server

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket


class WSHandler(tornado.websocket.WebSocketHandler):
	# called when client sends request to server to start a ws, and both have preformed ws handhake
    def open(self):
    	# log to terminal 
        print 'new connection'
        # send message to client that has connected to websocked
        self.write_message("Hello World")

	# called when message received from client
    def on_message(self, message):
        print 'message received %s' % message

    # called when connection closed
    def on_close(self):
      print 'connection closed'


#### set up http server ####
'''
An instance of tornado.web.Application is passed to the HTTP Server. 
When the server receives a request of the form: var ws = new WebSocket("ws://localhost:8888/ws");
, it will instantiate a WSHandler object. Note the "ws" at the end of the url. 
This is useful for the client side implementation.
'''
application = tornado.web.Application([
    (r'/ws', WSHandler),
])
 
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
 