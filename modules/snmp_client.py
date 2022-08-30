from pysnmp.hlapi import *



class SNMPHandler:

    __address = None

    def __init__(self, address):
        self.__address = address


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
                varBind = ' = '.join([x.prettyPrint() for x in varBind])
                varBind = varBind.split()
                varBind = varBind[2:]
                varBind = str(varBind).strip("'' [] ,").replace("', '", " ")
                return(varBind)
                