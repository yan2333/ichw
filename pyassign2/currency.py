
def test_getnumber():# test if function getnumber work well
    assert ("3562893.42658" == getnumber("gd,/??iavnpihi36941.561033bvoaf#$%^&*geuo3562893.42658"))
    
def test_getthestr():# test if function getthestr work well
    assert ("""{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }"""\
            == getthestr("USD","EUR",2.5))
    
def testall():#test all cases
    test_getthestr()
    test_getnumber()
    print("everthing is ok")
    return "lalala"

def getthestr(currency_from,currency_to,amount):#get the JSON from  http://cs1110.cs.cornell.edu/2016fa/a1server.php? 
    from urllib.request import urlopen

    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=%s&to=%s&amt=%f'\
                  %(currency_from,currency_to,amount))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr

def getnumber(str):# get the number of money from the JSON
    number="1234567890."
    l=len(str)
    thenumber=" "
    for i in str:
        if i in number:
            thenumber=thenumber+i
        else:
            thenumber=thenumber+" "
    return thenumber.split()[1]

def main(a):#
    if a=="lalala":
        currency_from=input("请输入您拥有的货币种类").upper()
        currency_to=input("请输入欲转换的货币种类").upper()
        amount=float(input("请输入欲转换金额"))
        print("You can get "+getnumber(getthestr(currency_from,currency_to,amount))+" "+currency_to)
        
main(testall())
