# Rutos PySNMP Tester

**Description**

Iot testing program writen in python 3.9.5.

The goal of the project is to have the means to connect the IoT device using SSH connection
and using setuped SNMP protocol and OID value to test the device in real time while saving the results. 

## Usage
0. Download this package with `go get` or `git clone`
```
   go get -u github.com/DovasM/Rutos_PySNMP_tester
	 
	 git clone https://github.com/DovasM/Rutos_PySNMP_tester
```
1. In config.json are setuped settings, commands to test the device.

```
"devices":
     "test_cases" : {
          "device" : [
               {
               "name":"serial",
               "OID":"1.3.6.1.4.1.48690.1.1.0",
               "method" : "get_serial_num"
               },
               {
               "name":"routerName.O",
               "OID":"1.3.6.1.4.1.48690.1.2.0",
               "method" : "get_name"
               },
               {
               "name":"productCode",
               "OID":"1.3.6.1.4.1.48690.1.3.0",
               "method" : "get_product_code"
               },   
	   .....
	   "mobile" : [
               {
               "name":"modemNum",
               "OID":"1.3.6.1.4.1.48690.2.1.0",
               "method" : "get_modem_num"
               },
               {
               "name":"mIndex",
               "OID":"1.3.6.1.4.1.48690.2.2.1.1.1",
               "method" : "get_index"
               },
```
2. In config.json set your directory to save tests

```
"results":{
    "save_as":"csv",
    "path":""
 }
```

3. Start test with command

`sudo python3 main.py <settings>`

Settings you can use:

```
usage: main.py [-u USERNAME] [-p PASSWORD] [-i IP]
optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        User name
  -p PASSWORD, --password PASSWORD
                        Password
  -i IP, --ip IP        IP address
```

## Examples

Testing with SSH connection:

`sudo python3 main.py -i 192.168.1.1 -u root -p Admin123`
