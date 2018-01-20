def test(arg):
    print "You have entered : %s" % arg
    # unwanted but committed
    # another unwanted commit

def test2(arg):
    print "You have entered : %s" % arg

def moon():
    test("m_arg")
    test2("m_arg2")

if __name__ == "__main__":
    moon()
    

