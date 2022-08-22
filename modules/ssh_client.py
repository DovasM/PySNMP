from imp import load_module
import paramiko
import time


class ConnectionHandler:

    __ssh_client = None
    __ssh_channel = None
    __testHandler = None
    __flags = None
    


    def __init__(self, flags):
        print(flags)

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
        stdin, stdout, stderr = self.__ssh_client.exec_command(command)
        # print(''.join(stderr.readlines()))
        if stderr.readlines():
            success = False
        return stdout.readlines()

    def __del__(self):
        self.__close_connection()

    def shell_exec_command(self, command):
        try:
            self.__ssh_channel = self.__ssh_client.invoke_shell()
            self.__ssh_channel.send(command + "\n")

            output = self.__ssh_channel.recv(9999).decode("ascii").splitlines()
            return output
        except Exception as error:
            print(error)



    def wait_until(self, output, timeout, period=0.25):
        mustend = time.time() + timeout
        while time.time() < mustend:
            if output[-2] == 'OK' or output[-2] == 'FAIL':
                return True, output[-2]
            output = self.__ssh_channel.recv(9999).decode("ascii").splitlines()
            # print(0)
            if output[-2] == []:
                continue
            output = self.__ssh_channel.recv(9999).decode("ascii").splitlines()
            time.sleep(period)
        return False, 'Error'
