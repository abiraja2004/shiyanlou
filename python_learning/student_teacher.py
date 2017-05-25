#!/usr/bin/env python3

import sys

import collections

from collections import Counter

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)
 
    def get_grade(self):

        score = sys.argv[2]

        result = Counter(score).most_common(4)

        lw = []

        fv = 0

        pv = 0

        for k, v in result:
            
            if k == 'D':

                fv = v
            
            else:

                pv += v
        lw.append('Pass: {}'.format(pv))

        lw.append('Fail: {}'.format(fv))
        
        finalstr = ', '.join(lw)

        return finalstr
        

class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self):

        score = sys.argv[2]

        result = Counter(score).most_common(4)

        lw = []

        for k, v in result:

            lw.append('{}: {}'.format(k, v))

        finalstr = ', '.join(lw)

        return finalstr        

person1 = Person('Sachin')
student1 = Student('Kushal', 'CSE', 2005)
teacher1 = Teacher('Prashad', ['C', 'C++'])

#print(person1.get_details())
#print(student1.get_details())
#print(teacher1.get_details())
if __name__ == '__main__':

    if sys.argv[1] == 'teacher':

        print(teacher1.get_grade())

    elif sys.argv[1] == 'student':

        print(student1.get_grade())
