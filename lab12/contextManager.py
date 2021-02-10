from contextlib import contextmanager


@contextmanager
def file_open(path, typ):
    global f_obj
    try:
        print('Start work custom manager')
        f_obj = open(path, typ)
        yield f_obj
    except OSError:
        print("We had an error!")
    finally:
        print('Closing file')
        f_obj.close()
