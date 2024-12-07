# -*- coding: utf-8 -*-
import re
from datetime import datetime, timedelta
from devicetest.core.test_case import TestCase, Step, CheckPoint
from hypium import *
from hypium.model import UiParam


class My_page(TestCase):

    def __init__(self, configs):
        self.TAG = self.__class__.__name__
        TestCase.__init__(self, self.TAG, configs)
        self.driver = UiDriver(self.device1)
        self.driver_width, self.driver_height = self.driver.get_display_size()
        self.host = host

    def setup(self):
        Step('1.回到桌面')
        if not self.driver.find_component(BY.key('AppIcon_Image_com.huawei.hmos.camera_218103928_0')):
            self.driver.press_key(KeyCode.POWER)
            self.driver.swipe(UiParam.UP, distance=60)
        self.driver.swipe_to_home()

    def process(self):
        password = "680401"
        Step('2.启动设置应用')
        # self.driver.press_key(KeyCode.POWER)
        self.driver.clear_app_data("com.atomicservice.5765880207855735979")
        self.driver.start_app("com.atomicservice.5765880207855735979", "EntryAbility")
        Step('3.我的')
        self.driver.check_component_exist(BY.text("我的"), wait_time=5)
        self.driver.touch(BY.text("我的"))
        # 等待控件
        self.driver.wait_for_component(BY.text('个人中心'))
        # 点击type为{Text}并且text为{账户余额}的控件
        Step('4.账户余额')
        self.driver.touch(BY.type('Text').text('账户余额'))
        self.driver.wait(0.5)
        # 等待控件
        self.driver.wait_for_component(BY.isAfter(BY.type('Blank')).isBefore(BY.type('Scroll')).text('K币余额').type('Text'))
        # 点击type为{Text}并且text为{直接充值}的控件
        Step('5.直接充值kb')
        self.driver.touch(BY.type('Text').text('直接充值'))
        self.driver.wait(0.5)
        self.driver.check_component_exist(BY.text("150K币"), wait_time=5)
        self.driver.touch(BY.text("150K币"))
        self.driver.wait(1)
        self.driver.check_component_exist(BY.text("确认支付"), wait_time=5)
        self.driver.touch(BY.type('Text').text('确认支付'))
        for w in password:
            pw = "{}".format(w)
            self.driver.touch(BY.key('text-{}'.format(pw)))
            self.driver.wait(0.5)
        self.driver.wait(5)
        # 断言text为{支付成功}的控件存在
        self.driver.check_component_exist(BY.text('支付成功'))
        self.driver.wait(0.5)
        self.driver.touch(BY.type('Text').text('返回商户'))
        self.driver.wait(2)
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(1)
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(1)
        # 等待控件
        Step('6.充值会员')
        self.driver.wait_for_component(BY.text('个人中心'))
        # 点击type为{Text}并且text为{充值}的控件
        self.driver.touch(BY.type('Text').text('充值'))
        self.driver.wait(0.5)
        # 通过相对位置双击控件
        self.driver.touch(BY.text('充值'), mode='double')
        self.driver.wait(0.5)
        # 点击type为{Text}并且text为{超级会员}的控件
        self.driver.touch(BY.type('Text').text('超级会员'))
        self.driver.wait(0.5)
        # 点击type为{Text}并且text为{《会员服务协议》}的控件
        self.driver.touch(BY.type('Text').text('《会员服务协议》'))
        self.driver.wait(1)
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(1)
        # 点击type为{Text}并且text为{开通前请阅读}的控件
        self.driver.touch(BY.type('Text').text('开通前请阅读'))
        self.driver.wait(0.5)
        # 通过相对位置点击控件
        self.driver.touch(BY.isAfter(BY.text('日卡会员')).isBefore(BY.text('0.01 1')).text('日卡会员').type('Text'))
        self.driver.wait(0.5)
        self.driver.wait(1)
        self.driver.check_component_exist(BY.text("确认支付"), wait_time=5)
        self.driver.touch(BY.type('Text').text('确认支付'))
        for w in password:
            pw = "{}".format(w)
            self.driver.touch(BY.text(pw))
            self.driver.wait(0.5)
        self.driver.wait(5)
        # 断言text为{支付成功}的控件存在
        self.driver.check_component_exist(BY.text('支付成功'))
        self.driver.wait(0.5)
        self.driver.touch(BY.type('Text').text('返回商户'))
        self.driver.wait(2)
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(1)
        # 等待控件
        self.driver.wait_for_component(BY.text('个人中心'))
        # 等待控件
        vip_string = self.driver.find_component(BY.text("有效期至:", MatchPattern.CONTAINS)).getText()
        vip_match = re.search(r'\d{4}-\d{2}-\d{2}', vip_string)
        date_str = vip_match.group()
        # 将提取的日期字符串转换为日期对象
        expiration_date = datetime.strptime(date_str, '%Y-%m-%d')
        # 获取系统日期并加一天
        today = datetime.now()
        tomorrow = today + timedelta(days=1)
        self.host.check_equal(expiration_date.date(), tomorrow.date(), "vip购买天数是否正确")
        # 等待控件
        self.driver.wait_for_component(BY.text('个人中心'))
        # 通过相对位置点击控件
        self.driver.touch(BY.isAfter(BY.type('Blank')).isBefore(BY.text('用户ID', MatchPattern.CONTAINS)).type('Image'))
        self.driver.wait(0.5)
        # 等待控件
        Step('7.意见反馈')
        self.driver.wait_for_component(BY.text('意见反馈'))
        # 点击type为{Text}并且text为{意见反馈}的控件
        self.driver.touch(BY.type('Text').text('意见反馈'))
        self.driver.wait(0.5)
        # 等待控件
        # 断言text为{意见反馈}的控件存在
        self.driver.check_component_exist(BY.text('意见反馈'))
        self.driver.wait(0.5)
        # 点击type为{Text}并且text为{功能使用}的控件
        self.driver.touch(BY.type('Text').text('功能使用'))
        self.driver.wait(0.5)
        self.driver.input_text(BY.type('TextInput'), '15868385402')
        self.driver.wait(0.5)
        self.driver.input_text(BY.type('TextArea'), '功能回归自动化测试数据无需回复')
        self.driver.wait(0.5)
        # 点击type为{Button}并且text为{提交}的控件
        self.driver.touch(BY.type('Button').text('提交'))
        self.driver.wait(2)
        # 断言text为{设置}的控件存在
        self.driver.check_component_exist(BY.text('设置'))
        self.driver.wait(0.5)
        # 点击type为{Text}并且text为{关于我们}的控件
        self.driver.touch(BY.type('Text').text('关于我们'))
        self.driver.wait(0.5)
        # 等待控件
        self.driver.wait_for_component(BY.text('关于我们'))
        # 点击type为{Text}并且text为{用户协议}的控件
        Step('8.用户协议')
        self.driver.touch(BY.type('Text').text('用户协议'))
        self.driver.wait(2)
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(0.5)
        self.driver.wait_for_component(BY.text('关于我们'))
        # 点击type为{Text}并且text为{隐私政策}的控件
        Step('9.隐私政策')
        self.driver.touch(BY.type('Text').text('隐私政策'))
        self.driver.wait(2)
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(0.5)
        self.driver.wait_for_component(BY.text('关于我们'))
        # 点击type为{Text}并且text为{会员服务协议}的控件
        Step('10.会员服务协议')
        self.driver.touch(BY.type('Text').text('会员服务协议'))
        self.driver.wait(0.5)
        self.driver.wait(2)
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(0.5)
        self.driver.wait_for_component(BY.text('关于我们'))
        # 点击type为{Text}并且text为{个人信息收集清单}的控件
        Step('11.个人信息收集清单')
        self.driver.touch(BY.type('Text').text('个人信息收集清单'))
        self.driver.wait(0.5)
        self.driver.wait(2)
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(0.5)
        self.driver.wait_for_component(BY.text('关于我们'))
        # 点击type为{Text}并且text为{第三方信息共享清单}的控件
        Step('12.第三方信息共享清单')
        self.driver.touch(BY.type('Text').text('第三方信息共享清单'))
        self.driver.wait(0.5)
        self.driver.wait(2)
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(0.5)
        self.driver.wait_for_component(BY.text('关于我们'))
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(0.5)
        # 等待控件
        self.driver.wait_for_component(BY.text('设置'))
        # 断言text为{账号注销}的控件存在
        Step('13.账号注销')
        self.driver.check_component_exist(BY.text('账号注销'))
        self.driver.wait(0.5)
        # 点击type为{Text}并且text为{账号注销}的控件
        self.driver.touch(BY.type('Text').text('账号注销'))
        self.driver.wait(0.5)
        # 等待控件
        self.driver.wait_for_component(BY.text('账号注销'))
        # 点击type为{Text}并且text为{注销账号}的控件
        self.driver.touch(BY.type('Text').text('注销账号'))
        self.driver.wait(0.5)
        # 断言text为{提示}的控件存在
        self.driver.check_component_exist(BY.text('提示'))
        self.driver.wait(0.5)
        # 点击type为{Button}并且text为{注销}的控件
        self.driver.touch(BY.type('Button').text('注销'))
        self.driver.wait(0.5)


    def teardown(self):
        Step('14.关闭设置应用')
        self.driver.stop_app("com.atomicservice.5765880207855735979")