import arduino_control as ac
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create server
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler,
                        allow_none=True) as server:
    server.register_introspection_functions()
    board = ac.board_connect(ac.Arduino.AUTODETECT)

    # Register functions
    def write_led(state: int):
        ac.write_led(board, state)

    server.register_function(write_led)

    # Run the server's main loop
    server.serve_forever()