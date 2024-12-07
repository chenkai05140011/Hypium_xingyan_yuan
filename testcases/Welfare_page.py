# -*- coding: utf-8 -*-
from devicetest.core.test_case import TestCase, Step, CheckPoint
from hypium import *
from hypium import host
from hypium.model import UiParam


class Welfare_page(TestCase):

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
        Step('2.启动设置应用')
        # self.driver.press_key(KeyCode.POWER)
        self.driver.clear_app_data("com.atomicservice.5765880207855735979")
        self.driver.start_app("com.atomicservice.5765880207855735979", "EntryAbility")
        Step('3.我的')
        self.driver.check_component_exist(BY.text("我的"), wait_time=5)
        self.driver.touch(BY.text("我的"))
        # 等待控件
        self.driver.wait_for_component(BY.text('个人中心'))
        # 等待控件
        Step('4.免费赚')
        self.driver.wait_for_component(BY.text('免费赚'))
        # 点击type为{Text}并且text为{免费赚}的控件
        self.driver.touch(BY.type('Text').text('免费赚'))
        self.driver.wait(0.5)
        # 等待控件
        self.driver.wait_for_component(BY.text('福利'))
        # 点击type为{Text}并且text为{直接充值}的控件
        Step('5.直接充值')
        self.driver.touch(BY.type('Text').text('直接充值'))
        self.driver.wait(2)
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(0.5)
        # 通过相对位置点击控件
        self.driver.touch(BY.isAfter(BY.text('第7天')).isBefore(BY.text('日常任务')).type('Image'))
        self.driver.wait(0.5)
        Step('6.签到')
        # 点击type为{Text}并且text为{福利再升级}的控件
        if self.driver.find_component(BY.text('福利再升级')):
            # 点击type为{Text}并且text为{双倍领取}的控件
            self.driver.touch(BY.type('Text').text('双倍领取'))
            self.driver.wait(20)
            # 点击type为{Text}并且text为{关闭广告}的控件
            self.driver.touch(BY.type('Text').text('关闭广告'))
            self.driver.wait(0.5)
        Step('7.领取福利')
        count = 0
        while self.driver.find_component(BY.text('领 取')):
             # 通过相对位置点击控件
            self.driver.touch(BY.text('领 取'))
            self.driver.wait(0.5)
            if self.driver.find_component(BY.text('福利再升级')):
                # 点击type为{Text}并且text为{双倍领取}的控件
                self.driver.touch(BY.type('Text').text('双倍领取'))
                self.driver.wait(20)
                # 点击type为{Text}并且text为{关闭广告}的控件
                self.driver.touch(BY.type('Text').text('关闭广告'))
                self.driver.wait(0.5)
                count += 1
        self.host.check_equal(1, 1, "福利领取{}次，一般情况是4次如果不是请检查福利页".format(count))

    def teardown(self):
        Step('8.关闭设置应用')
        self.driver.stop_app("com.atomicservice.5765880207855735979")