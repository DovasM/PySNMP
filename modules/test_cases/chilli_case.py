class TestCase:

    __connection = None

    def __init__(self, connection):
        self.__connection = connection

    def get_state(self):
        command = "uci get chilli.@chilli[0].enabled"
        response = self.__connection.exec_command(command)
        return response

    def get_IP(self):
        command = "uci get chilli.@chilli[0].uamlisten"
        response = self.__connection.exec_command(command)
        return response

    def get_net(self):
        command = "uci get chilli.@chilli[0].network"
        response = self.__connection.exec_command(command)
        return response

    def get_auth(self):
        command = "uci get chilli.@chilli[0]._mode"
        response = self.__connection.exec_command(command)
        return response

    # def get_session_count(self):
    #     command = ""
    #     response = self.__connection.exec_command(command)
    #     return response

    # def get_hss_index(self):
    #     command = ""
    #     response = self.__connection.exec_command(command)
    #     return response

    def get_hss_MAC(self):
        command = "ubus call chilli list | grep ipAddress"
        response = self.__connection.exec_command(command)
        return response

    def get_hss_IP(self):
        command = "ubus call chilli list | grep idleTimeout"
        response = self.__connection.exec_command(command)
        return response

    def get_hss_ID(self):
        command = "ubus call chilli list | grep sessionId"
        response = self.__connection.exec_command(command)
        return response

    def get_hss_username(self):
        command = "ubus call chilli list | grep userName"
        response = self.__connection.exec_command(command)
        return response

    # def get_hss_state(self):
    #     command = ""
    #     response = self.__connection.exec_command(command)
    #     return response

    def get_hss_idle_timemout(self):
        command = "ubus call chilli list | grep idleTimeout"
        response = self.__connection.exec_command(command)
        return response