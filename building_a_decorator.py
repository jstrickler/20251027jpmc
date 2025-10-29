from functools import wraps
import logging
logging.basicConfig(filename="timestamp.log", 
    format="%(levelname)s %(name)s %(asctime)s %(message)s",
    datefmt="%x-%X",
    level=logging.DEBUG,
)

def timestamp(func):  # func is original spam
    @wraps(func)
    def _wrapper(*args, **kwargs):
        logging.debug(func.__name__)
        return func(*args, **kwargs)  # call original  spam() or ham(), etc
    return _wrapper

@timestamp
def spam(repeat_count):
    print('SPAM' * repeat_count)

# spam = timestamp(spam)  # replace original spam value with foo
print(spam)
spam(10)
spam(3)

def ham():
    print("HAM HAM HAM")

ham = timestamp(ham)
ham()
print(spam, ham)