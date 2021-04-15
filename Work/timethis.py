# timethis.py

def timethis(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f'Elapsed time: {end_time - start_time} seconds')
    return wrapper
