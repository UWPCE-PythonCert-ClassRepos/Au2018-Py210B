def yushus_Exception_NameError():
	# use a variable that has not been defined yet
    x = y

def yushus_Exception_TypeError():
    # operations between two different type, like str and int
    x = 'yushu'
    x // 3

def yushus_Exception_AttributeError():
    # int type doesn't have an attribute of strip
    x = 5
    y = x.strip()

#yushus_Exception_NameError()
#yushus_Exception_TypeError()
yushus_Exception_AttributeError()