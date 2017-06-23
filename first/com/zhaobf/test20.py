import multiprocessing
def f(name):
    print('hello',name)
if __name__=='__main__':
    p=multiprocessing.Process(target=f,args=('bob',))
    p.start()
    p.join()
