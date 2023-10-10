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

# Rationale for Database Schema

The database schema I created consists of three tables called patients, labs, and patient_lab. 

1. Patients Table

* patient_id: acts as a unique identifier for each patient, primary key, datatype: integer
* first_name: contains information about the patient's first name, datatype: string
* last_name: contains information about the patient's last name, datatype: string
* date_of_birth: contains information about the patient's birthday, datatype: date
* admitted_date: contains information about when the patient was admitted, datatype: date

2. Labs Table

* lab_id: acts as a unique identifier for each lab test, primary key, datatype: integer
* lab_name: contains information about the name of the lab test ordered, datatype: string
  
3. Patient_lab Table

* patient_lab_id: acts as a unique identifier for the lab for the patient, datatype: integer
* patient_id: contains the unique identifier number assigned for the patient, foreign key
* lab_id: contains the unique identifier number assigned for the lab test, foreign key

# Errors / Troubleshooting

I was unable to deploy my Flask application because I kept getting an error message that I attempted to resolve, but was unable to. 

Below is the error message I got:
![image](https://github.com/jesschannn/Flask_4_databases_mysql_vm./assets/123782059/5ba82d47-a25d-44a6-b2e1-d77e4a4bd772)

```sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1045, "Access denied for user 'None'@'34.139.138.85' (using password: YES)")```

Reading the error, I interpreted the error as stating that a user named "None" with an IP address that did not match the IP address I put in my .env file did not have access to deploy the Flask app I had created. 

Troubleshooting: 

1. In the Google shell console, I navigated to the mysql console and typed in ```show databases;``` and ```select user from mysql.user``` to see if I had any other users or any other databases that should not have been there.
2. In Azure, I double checked to see that the IP address of the VM I created was the same IP address I used in my .env file and in MySQL Workbench.
3. In MySQL Workbench, I double checked to make sure all of the information I put was correct. I also tested the connection to make sure it was running correctly, which it was.
4. I tried to run this code replacing "user", "password, "ip", "port", and "database" with my own information from the .env file, but I was still receiving the same error message.

   ```app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'user':'password'@'ip':'port'/'database''```
   
5. As per Professor William's suggestion, I removed the quotations in my .env file, but I was still getting the same error message.

If my Flask application had run successfully, there would be a database with "fake" information populated in the three tables I had created.
