import unittest

from employee import *

class Test_employee(unittest.TestCase):
    """
    测试employee类
    """

    def setUp(self):
        """创建一个employee实例供测试方法使用"""
        first_name = "wan"
        last_name = "ting"
        salary = 1000
        self.my_employee = Employee(first_name,last_name,salary)

    def test_give_default_raise():
        """测试默认值"""
        self.my_employee.get_salary()
        self.assertEqual()

    def test_give_custom_raise():
        pass