from imp import load_module
import paramiko
import time


class ConnectionHandler:

    __ssh_client = None
    __ssh_channel = None
    __testHandler = None
    __flags = None
    


    def __init__(self, flags):

        if not self.__open_connection(flags.ip, flags.username, flags.password):
            raise Exception("Unable to connect to SSH server")

        # self.__flags = flags

        # self.__testHandler = self.load_module()
        # self.__testHandler.test_commands(config.get_comm(self.__flags.name))
        
    def load_module(self):
        module = None
        try:
            module = __import__('modules.test_handler', fromlist=['modules'])
            return module.TestHandler(self, self.__flags.name)
        except:
            return False 

    def __close_connection(self):
        if self.__ssh_client:
            self.__ssh_client.close()

    def __open_connection(self, addr, username, password):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(addr, 22, username, password)
            self.__ssh_client = client
            return True
        except:
            return None

    def exec_command(self, command):
        success = True
        grep = False
        stdin, stdout, stderr = self.__ssh_client.exec_command(command)
        # print(''.join(stderr.readlines()))
        if stderr.readlines():
            success = False
        comp_t = command.split()[0]
        grep_c = command.split()[-2]
        if grep_c == "grep":
            grep = True
        response = stdout.readlines()

        response = getattr(self,"%s_compare" % comp_t)(response, grep)
        return response

    def __del__(self):
        self.__close_connection()




    def ubus_compare(self, ssh_response, grep):
        if grep:
            ssh_response = ssh_response[0].split()[-1].strip('"')
        else:
            ssh_response = ssh_response[1].split()[-1].strip('"')
        return ssh_response


    def uci_compare(self, ssh_response, grep):
        ssh_response = ssh_response[0].strip('\n')
        return ssh_response
    
    def gsmctl_compare(self, ssh_response, grep):
        ssh_response = ssh_response[0].strip('\n')
        return ssh_response



