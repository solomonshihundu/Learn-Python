#Begin Portion 1#
import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for load in self.connections.values():
            total += load
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
    
#End Portion 1#

########################################################################################
#Testing Server
#server = Server()
#server.add_connection("192.168.1.1")
#print(server.load())

#server.close_connection("192.168.1.1")
#print(server.load())

########################################################################################
#Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        self.connections[connection_id] = server

        # Add the connection to the server
        #print("Connection ID : {conn_id}".format(conn_id = connection_id))
        server.add_connection(connection_id)

        self.ensure_availability()

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        server = self.connections[connection_id]

        # Close the connection on the server
        server.close_connection(connection_id)

        # Remove the connection from the load balancer
        self.servers.remove(server)

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        total_load = 0
        server_count = len(self.servers)
        #print("Number of Servers is: {no_servers}".format(no_servers = server_count))
        avg = 0
        for server in self.servers:
            total_load += server.load()      
        
        avg = total_load/server_count
        return avg

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        
        #print("Availability : {my_load}".format(my_load = self.avg_load()))
        #print(type(self.avg_load))
        
        if self.avg_load() > 50:
            self.servers.append(Server())

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
#End Portion 2#

########################################################################################
#Testing Load Balancer

l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print("Avg Load: {avg_load:.2f}".format(avg_load = l.avg_load()))

#l.add_connection("fdca:83d2::f2")
#print("Avg Load: {avg_load:.2f}".format(avg_load = l.avg_load()))

l.servers.append(Server())
print("Avg Load with More Server: {avg_load:.2f}".format(avg_load = l.avg_load()))

#l.close_connection("fdca:83d2::f20d")
#print(l.avg_load())

print("Adding connections")
for connection in range(20):
    l.add_connection(connection)
print(l)

#print(l.avg_load())

########################################################################################


