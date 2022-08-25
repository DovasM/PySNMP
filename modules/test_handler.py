

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
            print(module)
            return module.TestCase(self.__ssh_connection)
        except:
            return False      

    def test_commands(self):
        
        # self.__connection.exec_command("/etc/init.d/gsmd stop\r")

        commands = self.__config.get_comm("chilli")
        case = self.__load_case('chilli')
        print(case)
        for command in commands:
            result = {}
            
            ssh_response = getattr(case, command['method'])()
            snmp_response = self.snmp_test_command(command["OID"])
            
            if ssh_response == snmp_response:
                result["status"] = True
            else:
                result['status'] = False 

            result["name"] = command["name"]
            result["count"] = len(commands)

            # self.__termHandler.test_print(result)
            self.__results.append(result)
            
        # self.__connection.exec_command("/etc/init.d/gsmd start\r")



    def snmp_test_command(self, OID):

        response = self.__snmp_connection.get_oid_val(OID)

        response = response.split()[-1]
        return response

    
    def get_results(self):
        return self.__results