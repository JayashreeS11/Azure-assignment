# Azure-assignment
The following are completed:

1. A storage account (jayashrees11storage) is created in Azure,
   inside which a container (jayashrees11container) is present with 3 folders - folder1, folder2, folder3

2. A flask app (app.py) is created for printing the contents of the folder. The flask app renders to a
   html file (file_list.html) which displays the list of files.

3. A Virtual Machine (jayashrees11vm) is created in Azure inside a Vnet (jayashrees11vnet) and Subnet

4. The inbound traffic is streamlined for tcp at port 5000, and the source ip is Tiger VPN.

5. The flask app is deployed and run inside the VM

6. The app displays the files present inside the folder (which is given as a query parameter in the URL)

Without VPN:
![alt text](<Without_vpn.png>)

With VPN:
![alt text](<With_vpn.png>)

Cost:
![alt text](<Cost.png>)