# Flask_4_databases_mysql_vm.

# VM Set Up (for Azure)

1. Navigate to your Azure account
2. In the hamburger bar to the left, navigate to "Virtual Machines"
3. Click "create"
4. Make sure you are under the correct subscription. Go to the resource group and designate which one you want the virtual machine to live in
5. Give your virtual machine a name
6. Based on the current assignment, set the security type to standard, the imagine to Ubuntu Server 20.04 LTS - x64 Gen2, size to Standard_B1ms
7. Under the "Administrator Account" section, select password. Create a username and password for the virtual machine
8. Under the "Inbound Port Rules", select allow selected ports. Click on the drop down menu and select SSH(22), HTTP(80), and HTTPS(443)
9. Go to auto-shutdown and click on for "enable auto-shut down". Adjust the showdown time and time zone based on your preferences
10. You do not need to make any changes in the advanced and tags tab. 
11. Go to the "Review and Create" tab and make sure that everything is correct
12. Deploy your virtual machine
13. Once the virtual machine has been successfully deployed, click on the virtual machine that was just created
14. Go to the left side and under settings, click networking
15. Click on "add inbound port rules". Type in "3306" into "destination port ranges" and add the port.

# MySQL Process Set Up
1. In the console, type in ```ssh <yourusername>@<publicIPaddress>```
2. Type in "yes" when the line "are you sure you want to continue connecting?"
3. Type in ```sudo apt-get update``` to the console to get the latest updates
4. Type in ```sudo apt install mysql-server mysql-client``` to the console
5. Log into MySql by typing in ```sudo mysql```
6. Create a new user: type into console ```create user '<name>'@'%' identified by '<password>```
7. Confirm the user recently created: type into console ```select user from mysql.user;```
