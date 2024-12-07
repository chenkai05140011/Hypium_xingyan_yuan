from setuptools import setup

setup(
       name='hypiumTest',
       version='1.0.0.0',
       author='chen_kai',
       # py_modules指定需要打包的hypium用例py文件
       py_modules=['testcases.Home_page'],
       include_package_data=True
       )