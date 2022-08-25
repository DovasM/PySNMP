
class TestCase:

    __connection = None

    def __init__(self, connection):
        self.__connection = connection

    def get_serial_num(self):
        command = "ubus call mnfinfo get_value '{\"key\":\"serial\"}'"
        response = self.__connection.exec_command(command)
        return response

    def get_name(self):
        command = "uci get system.system.routername"
        response = self.__connection.exec_command(command)
        return response

    def get_product_code(self):
        command = "ubus call mnfinfo get_value '{\"key\":\"name\"}'"
        response = self.__connection.exec_command(command)
        return response

    def get_batch_num(self):
        command = "ubus call mnfinfo get_value '{\"key\":\"batch\"}'"
        response = self.__connection.exec_command(command)
        return response

    def get_hardw_rev(self):
        command = "ubus call mnfinfo get_value '{\"key\":\"hwver\"}'"
        response = self.__connection.exec_command(command)
        return response

    def get_fw_ver(self):
        command = "uci get system.system.device_fw_version"
        response = self.__connection.exec_command(command)
        return response

