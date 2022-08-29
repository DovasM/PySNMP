import modules.config_handler as ConfigHandler
import modules.test_handler as TestHandler
import modules.result_handler as ResultHandler
import modules.snmp_client as SNMPHandler
import modules.ssh_client as ConnectionHandler
import modules.terminal_handler as TerminalHandler


config = None
ssh = None
tester = None
resulter = None
device = None
__connHandler = None
snmp = None

def __load_module(type, flags, config):
        module = None
        try:
            module = __import__('modules.{type}'.format(type=type), fromlist=['modules'])
            return module.ConnectionHandler(flags, config)
        except Exception as error:

            raise Exception (error)  


def init_modules():
    global config, tester, resulter, terminal_flags, device, flags, snmp, ssh
    try:
        terminal_flags = TerminalHandler.TerminalHandler()
        flags = terminal_flags.get_args()
        config = ConfigHandler.ConfigHandler("config.json")
        snmp = SNMPHandler.SNMPHandler(config.get_param("address"))
        ssh = ConnectionHandler.ConnectionHandler(flags)
        # __connHandler = __load_module(device.device_conn_select(flags.name), flags, config)
        tester = TestHandler.TestHandler(snmp, ssh ,config)
        resulter = ResultHandler.ResultHandler(config.get_param("results")["save_as"])
        
    except Exception as error:
        raise Exception (error)



def main():
    try:
        init_modules()
        # commands = "chilli"
        # print(config.get_comm(commands))

        # "ubus call vuci.network.mobile get_all_modems | grep version"
        # print(ssh.exec_command("gs"))
        tester.test_commands()
        # print(tester.get_results())
        # resulter.open_file(config.get_param("results")["path"])
        # resulter.save_results(tester.get_results())
        # resulter.close_file()

        # print(tester.get_results())
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()