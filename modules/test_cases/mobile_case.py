class TestCase:

    __connection = None

    def __init__(self, connection):
        self.__connection = connection

    def get_modem_num(self):
        command = "uci get simcard.@sim[0].position"
        response = self.__connection.exec_command(command)
        return response

    def get_index(self):
        command = "uci get simcard.@sim[0].primary"
        response = self.__connection.exec_command(command)
        return response

    def get_desc(self):
        command = "uci get simcard.@sim[0].modem"
        response = self.__connection.exec_command(command)
        return response

    def get_imei(self):
        command = "ubus call vuci.network.mobile modems_info | grep imei"
        response = self.__connection.exec_command(command)
        return response

    def get_model(self):
        command = "ubus call vuci.network.mobile modems_info | grep modem"
        response = self.__connection.exec_command(command)
        return response

    def get_manufacturer(self):
        command = "gsmctl -w"
        response = self.__connection.exec_command(command)
        return response

    def get_revision(self):
        command = "ubus call vuci.network.mobile modems_info | grep fw_version"
        response = self.__connection.exec_command(command)
        return response
    
    def get_serial(self):
        command = "gsmctl -a"
        response = self.__connection.exec_command(command)
        return response

    def get_IMSI(self):
        command = "gsmctl -x"
        response = self.__connection.exec_command(command)
        return response

    def get_sim_state(self):
        command = "gsmctl -z"
        response = self.__connection.exec_command(command)
        return response

    def get_pin_state(self):
        command = "gsmctl -u"
        response = self.__connection.exec_command(command)
        return response

    def get_net_state(self):
        command = "gsmctl -g"
        response = self.__connection.exec_command(command)
        return response

    def get_signal(self):
        command = "gsmctl -q"
        response = self.__connection.exec_command(command)
        return response

    def get_operator(self):
        command = "gsmctl -o"
        response = self.__connection.exec_command(command)
        return response

    def get_operator_num(self):
        command = "gsmctl -f"
        response = self.__connection.exec_command(command)
        return response

    def get_conn_state(self):
        command = "ubus call vuci.network.mobile mobile_status | grep connection"
        response = self.__connection.exec_command(command)
        return response

    def get_conn_type(self):
        command = "gsmctl -t"
        response = self.__connection.exec_command(command)
        return response

    def get_temperature(self):
        command = "gsmctl -c"
        response = self.__connection.exec_command(command)
        return response

    def get_SINR(self):
        command = "gsmctl -Z"
        response = self.__connection.exec_command(command)
        return response

    def get_RSRP(self):
        command = "gsmctl -W"
        response = self.__connection.exec_command(command)
        return response

    def get_RSRQ(self):
        command = "gsmctl -M"
        response = self.__connection.exec_command(command)
        return response

    def get_IP(self):
        command = "gsmctl --ip mob1s1a1"
        response = self.__connection.exec_command(command)
        return response