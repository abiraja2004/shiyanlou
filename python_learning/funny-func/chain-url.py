class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, name, **kwargs):
        return Chain('%s/%s' % (self._path, name))

    def __str__(self):
        return self._path

    __repr__ = __str__



#/status/user/timeline/list
#方法也是一个属性
c = Chain().users('jack').repos
print(c)
"""

这里Chain().users('michael')部分，首先代码没有定义users()方法(如果有定义方法，
它的优先级高与__getattr__)，所以这么把它看做未定义属性。
于是触发__getattr__。__getattr__(self,path)返回Chain('/users')，
相当于变成了Chain('/users')('michael').users.repos.Chain('/users')('michael')
触发__call__，得到Chain('/users/michael/')。users.repos。再后面同理。
最后得到Chain('/users/michael/users/repos')。通过__repr__输出。

如果是print(Chain('/users/michael/users/repos') )  则通过__str__输出。
"""