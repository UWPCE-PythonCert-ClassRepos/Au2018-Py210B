# This function causes a NameError

def i_make_name_errors():
    return flubber

# This function causes a TypeError

def i_make_type_errors():
    return 17 + "bees"

# This function causes a SyntaxError

def i_make_syntax_errors():
    if("B")

# This function causes an AttributeError

def i_make_attribute_errors():
    bar = 17
    return bar.attribute