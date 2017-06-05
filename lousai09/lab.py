# -*- coding:utf-8 -*-
import copy

class Lab(object):
    """ 实验
    """

    def __init__(self, name, tags=[]):
        self.name = name
        # FIXME
        self._tags = copy.deepcopy(tags)

    def insert_tag(self, tag):
        """ 插入标签，需要检查标签是否存在
        """
        # FIXME
        if not (tag in self._tags):
           self._tags.append(tag)

    @property
    def tags(self):
        return self._tags[:]

    def can_be_started(self, user):
        """判断用户能否启动实验，只有登录的会员用户才能启动实验
        """
        # FIXME
        if not user.is_authenticated:
            can = False
        elif user.is_member:
            can = True
        else:
            can = False
        return can
