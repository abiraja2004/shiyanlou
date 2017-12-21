import functools


def log(func):
    #函数签名改成被装饰的函数
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("haha")
        result = func(*args, **kw)
        print("heihei")
        return result
    return wrapper


@log
def now(s):
    print('now,%s' % s)
    return "end"


print(now("eeee"))


def test(text=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("begin call %s" % text)
            result = func(*args, **kw)
            print("end call %s" % text)
            return result
        return wrapper
    return decorator


@test("kk")  #可以传参数也可以不传
def f():
    pass

d = f()
























