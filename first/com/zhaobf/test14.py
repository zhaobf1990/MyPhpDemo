class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def users(self, user):
        return Chain('%s/%s/%s' % (self._path, "users", user))

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().users('michael').repos)

# print(Chain().status.user)
