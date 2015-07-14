from SOAPpy import WSDL

#https://public.co.travis.tx.us/SIPSpublicSvc/sipsvc.asmx?WSDL
WSDLFILE = '/Users/jasharmon/src/inmate_search/sipsvc.wsdl'

_server = WSDL.Proxy(WSDLFILE)
def search():
    results = _server.GetAllInmates()
    #print results[0][0]['FullName']
    for r in results[0]:
#        print r['FullName']
        print r

if __name__ == '__main__':
    import sys
    print search()
