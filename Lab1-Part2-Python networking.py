#!/usr/bin/env python
# coding: utf-8

# ---------------------------------------------------------------------------------------------------------------------------
# Part2
# ---------------------------------------------------------------------------------
# ## python networking 

# ###  In this Tutorial you will use the Module "ipaddress" that will help you to deal with ip addresses and network prefixes with more  ease.
# 
#  Firstly take a look on the documentation of the module in the pdf file attached, Then perform the following tasks 

# In[1]:


#!pip install ipaddress
import ipaddress
# Code Starts Here 
# using the ipaddress module
# 1-print the number of hosts in the network 192.168.70.0/24 (0.5 mark)
# 2- print the network mask(prefix) of the network 192.168.70.0/24 in both formats (0.5 mark)
# hint refer to the additional attribute section in the pdf

network = ipaddress.ip_network("192.168.70.0/24")
no_hosts = 0;
for x in network.hosts():
    no_hosts +=1 
#no_hosts =254.
print(no_hosts)

print(network.netmask)
print(network.hostmask)


# In[2]:


# 2-print the hosts in the network 192.168.70.0/24 (0.5 mark)
for x in network.hosts():
    print(x)


# In[3]:


# 3-take an ip address from the user and check and prints a message indicating wether
# this address belongs to the network 192.168.70.0/24 or not (0.5 mark)

ip_address = input()
input_network = 0
    
input_network = ipaddress.ip_network(ip_address, strict = False)
    

host_in = ipaddress.ip_interface(ip_address)
host = ipaddress.ip_interface("192.168.70.0/24")
network = '192.168.70.0/24'
print(str(host_in.network))
if ipaddress.ip_address(ip_address) in ipaddress.ip_network(network):
    print("The IP address belongs to the network 192.168.70.0/24")
else:
    print("The IP address doesn't belong to the network 192.168.70.0/24")


# In[4]:


# 4- define function Routing_Table() (4 marks)
# the function returns and (prints) the routing table as a list of networks and relatve egress interfaces
# the function should aske the user for the number of required interfaces first 
# then it asks the user to fill them accordingly 
# if the user entered the character 'd' as an egress interface then the function set this as default interface 
# in all cases the routing table should contain a default egress interface
# Your Code Starts Here 

def Routing_Table():
    no_interfaces = int(input())
    interfaces = dict()
    for i in range(no_interfaces):
        network = input()
        egress_interface = input()
        interfaces[network] = egress_interface
    print(interfaces)
    return interfaces

#uncomment this line for function call
Routing_Table()  


# In[65]:


# 5- define function Forward() (4 marks)
# the function takes as input the routing table as returend from function Routing_Table() and an ip address as string.
# the function should perform the longest prefix match between the ip and the reouting table
# then the function should decide (return and print) the suitable interface to forward the packet with the input ip to.
# the function should print the input routing table aswell
# Your Code Starts Here 

def Forward(routing_table,ip_address):
    n = len(routing_table)
    adds = list(routing_table.keys())
    for i in range(n-1):
        network = adds[i]
        if ipaddress.ip_address(ip_address) in ipaddress.ip_network(network):
            return routing_table[network]
    return routing_table['d']
# DL={'192.168.0.0/24' : 'Serial 0','192.168.0.0/16': 'Serial 1', '170.200.30.192/26': 'Serial 2', '150.20.70.0/24': 'Default','d':'Default'}
# ip_address = "135.46.63.10"
# ip_address2 = "135.46.57.14"
# ip_address3= "135.46.52.2"
# ip_address4 = "192.53.40.7"
# ip_address5="192.53.56.7"
# result =Forward(DL,ip_address5)
# print(result)


# In[66]:



# DL=Routing_Table()
DL={'192.168.0.0/24' : 'Serial 0','192.168.0.0/16': 'Serial 1', '170.200.30.192/26': 'Serial 2', '150.20.70.0/24': 'Default','d':'Default'}
print(DL)


# test the function Routing_table() with the following test case 
# 
# number of interfaces=4
# 
# Network1: 192.168.0.0/24  --> Serial0
# 
# Network2: 192.168.0.0/16  --> Serial1
# 
# Network3: 150.20.70.0/24  --> Default
# 
# Network4: 170.200.30.192.0/26  --> Serial 2
# 
# please note that the routing table should always contain a default entry 
# 

# In[67]:


Forward(DL,'192.169.0.1')


# In[68]:


Forward(DL,'192.169.50.1')


# In[69]:


Forward(DL,'150.20.70.2')


# In[70]:


Forward(DL,'190.169.0.1')


# In[ ]:





# In[ ]:





# In[ ]:




