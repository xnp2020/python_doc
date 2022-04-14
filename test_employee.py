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

    def test_give_default_raise(self):
        """测试默认值"""
        self.my_employee.give_raise()
        wan_salary = self.my_employee.get_salary()
        self.assertEqual(wan_salary, "Wan Ting salary is 6000")

    def test_give_custom_raise(self):
        """测试自定义值"""
        self.my_employee.give_raise(1000)
        wan_salary = self.my_employee.get_salary()
        self.assertEqual(wan_salary, "Wan Ting salary is 2000")
        
if __name__ == '__main__':
    unittest.main()