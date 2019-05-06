import os
from async_promises import Promise
def cp(v):
  def p(res,rej):
    print('running',v)
    os.system(f'sleep {v}')
    print('finished',v)
    res(v)
  return p

# list(map(Promise,map(cp,[2,1,5,4])))
def grep(pattern):
  print("Looking for %s" % pattern)
  while True:
    line = (yield)
    if pattern in line:
      print(line)

def t(targets):
  for tg in targets:
    tg.run()


running = True
def pip(func,nexts):
  while(running):
    _input = (yield)
    output = func(_input)
    for next in nexts:
      next(output)

def f1(v):
  print('f1',v)
  return v*2

def f2(v):
  print('f2',v)
  return v*3

def f3(v):
  print('f3',v)
  return v*4

p3 = pip(f3,print)
p3.send(None)

p2 = pip(f2,p3.send)
p2.send(None)

p1 = pip(f1,p2.send)
p1.send(None)
