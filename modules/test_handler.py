

from distutils.cmd import Command
from imp import find_module
from operator import mod


class TestHandler:


    __snmp_connection = None
    __ssh_connection = None
    __config = None
    __termHandler = None
    __device = None
    __results = []

    def __init__(self, snmp_connection, ssh_connection ,config):


        self.__snmp_connection = snmp_connection
        self.__ssh_connection = ssh_connection
        self.__config = config

        
        self.__termHandler = __import__('modules.terminal_handler', fromlist=['modules'])
        self.__termHandler= self.__termHandler.TerminalHandler()


    def __load_case(self, path):
        module = None
        try:
            # __import__('modules.test_cases.{type}_case'.format(type), fromlist=['modules'])
            module = __import__('modules.test_cases.{0}_case'.format(path), fromlist=['modules.test_cases'])
            return module.TestCase(self.__ssh_connection)
        except:
            return False

    def chilli_check(self):
        active = False
        if (self.__ssh_connection.exec_command('uci get hwinfo.hwinfo.wifi') == 1 or
        self.__ssh_connection.exec_command('uci get hwinfo.hwinfo.ethernet') == 1):
            active = True
        return active       

    def device_check(self):
        return True


    def mobile_check(self):
        active = False
        if self.__ssh_connection.exec_command('uci get hwinfo.hwinfo.mobile') == 1:
            active = True
        return active             

    def gps_check(self):
        active = False
        if self.__ssh_connection.exec_command('uci get hwinfo.hwinfo.gps') == 1:
            active = True
        return active         


    def hwinfo(self, cases):
        hw = []
        hw.append('device')
        for case in cases:
            test_case = getattr(self, "{}_check".format(case))
            if test_case:
                hw.append(case)
        return hw        

    def count_comm(self, cases):
        count = 0
        for case in cases:
            commands = self.__config.get_comm(case)
            count = count + len(commands)
        return count

    def test_commands(self):
        
        # self.__connection.exec_command("/etc/init.d/gsmd stop\r")
        result = {}

        test_cases = self.hwinfo(self.__config.get_test_cases())
        result["count"] = self.count_comm(test_cases)
        for test_case in test_cases:
            commands = self.__config.get_comm(test_case)
            case = self.__load_case(test_case)
            

            for command in commands:
                

                ssh_response = getattr(case, command['method'])()
                snmp_response = self.snmp_test_command(command["OID"])

                if ssh_response == snmp_response:
                    result["status"] = True
                else:
                    result['status'] = False 

                result["name"] = command["name"]
                
                self.__termHandler.test_print(result)
                self.__results.append(result)
            
        # self.__connection.exec_command("/etc/init.d/gsmd start\r")



    def snmp_test_command(self, OID):
        response = self.__snmp_connection.get_oid_val(OID)
        response = response.split()[-1]
        return response

    
    def get_results(self):
        return self.__results