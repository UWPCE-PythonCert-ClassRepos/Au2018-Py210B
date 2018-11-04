def do_twice(f):
  f()
  f()

def do_four(f):
  do_twice(f)
  do_twice(f)

def beam():
  print('+----+----+')

def post():
  print('|    |    |')

def posts():
  do_four(post)

def row():
  beam()
  posts()

def grid():
  do_twice(row)
  beam()

grid()

