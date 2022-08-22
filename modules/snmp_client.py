import pysnmp
from pysnmp.hlapi import *



class SNMPHandler:

    __address = None
    __results = []

    def __init__(self, address):
        self.__address = address

    def test_oid_comms(self, oids):
        for command in oids:
            result = {}
            
            response = self.get_oid_val(command["OID"])
            result["name"] = command["name"]
            result["response"] = response
            # self.__termHandler.test_print(result)
            self.__results.append(result)

    def get_results(self):
        return self.__results


    def get_oid_val(self, oid):
        iterator = getCmd(
            SnmpEngine(),
            CommunityData('public', mpModel=0),
            UdpTransportTarget((self.__address, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid)))


        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

        if errorIndication:
            return(errorIndication)

        elif errorStatus:
            return('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

        else:
            for varBind in varBinds:
                return(' = '.join([x.prettyPrint() for x in varBind]))
                