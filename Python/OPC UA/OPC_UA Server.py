import sys
sys.path.insert(0, "..")
import time
from opcua import ua, Server

if __name__ == "__main__":

    # setup our server
    server = Server()
    #server.set_endpoint("opc.tcp://0.0.0.0:8080/freeopcua/server/")
    server.set_endpoint("opc.tcp://0.0.0.0:8080")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://local.opcua.io"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    myobj = objects.add_object(idx, "MyObject")
    myvar = myobj.add_variable(idx, "MyVariable", 6.7)
    myvar.set_writable()    # Set MyVariable to be writable by clients

    # Register the server with the LDS
    server.set_server_name("Python OPC UA Server")
    server.set_application_uri("urn:http://local.opcua.io:OPCUAServer")
    server.product_uri = "urn:http://local.opcua.io:OPCUAServer"
    server.discovery_urls = ["opc.tcp://localhost:8080"]

    # starting!
    server.start()

    try:
        count = 0
        while True:
            time.sleep(1)
            count += 0.1
            myvar.set_value(count)
    finally:
        #close connection, remove subscriptions, etc
        server.stop()