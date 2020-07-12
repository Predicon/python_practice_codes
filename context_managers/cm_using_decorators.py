from contextlib import contextmanager
#using decorator
@contextmanager
def file(filename,mode):
    print('enter')
    file=open(filename,mode)
    yield file
    file.close()
    print('exit')


with file('test.txt','w') as f:
    f.write('goog day')
    