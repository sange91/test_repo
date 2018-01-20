def test(arg):
    print "You have entered : %s" % arg
    # unwanted but committed
    # another unwanted commit

def test2(arg):
    print "You have entered : %s" % arg

def moon():
    test("m_arg")
    test2("m_arg2")

def star():
    print"running star func"
    test("my_arg")
    test2("my_arg")


if __name__ == "__main__":
    star()
    moon()

