import mymod1

mymod1.myfunc1()

from mymod1 import myfunc2

myfunc2()

import mypkg1 as pkg
pkg.mypkg1func1()

import mypkg1.mypkgmod1
mypkg1.mypkgmod1.mypkgmod1func1()

import mypkg2
#mypkg2.mypkg2mod1.mypkg2mod1func1() # This fails

import mypkg2.mypkg2mod1
mypkg2.mypkg2mod1.mypkg2mod1func1()

import mypkg3
mypkg3.mypkg3mod1func1()
