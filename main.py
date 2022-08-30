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
snmp = None


def init_modules():
    global config, tester, resulter, terminal_flags, device, flags, snmp, ssh
    try:
        terminal_flags = TerminalHandler.TerminalHandler()
        flags = terminal_flags.get_args()
        config = ConfigHandler.ConfigHandler("config.json")
        snmp = SNMPHandler.SNMPHandler(config.get_param("address"))
        ssh = ConnectionHandler.ConnectionHandler(flags)
        tester = TestHandler.TestHandler(snmp, ssh ,config)
        resulter = ResultHandler.ResultHandler(config.get_param("results")["save_as"])
        
    except Exception as error:
        raise Exception (error)



def main():
    try:
        while True:
            init_modules()
            tester.test_commands()
            resulter.open_file(config.get_param("results")["path"])
            resulter.save_results(tester.get_results())
            resulter.close_file()
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()