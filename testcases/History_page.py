# -*- coding: utf-8 -*-
import re

from devicetest.core.test_case import TestCase, Step, CheckPoint
from hypium import *
from hypium.model import UiParam
from hypium import host
import re

class History_page(TestCase):

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
        Step('3.看过')
        # 等待控件
        self.driver.wait_for_component(BY.text('看过'))
        # 点击type为{Text}并且text为{看过}的控件
        self.driver.touch(BY.type('Text').text('看过'))
        self.driver.wait(0.5)
        self.driver.wait_for_component(BY.text('我的追剧'))
        # 点击type为{Text}并且text为{我的追剧}的控件
        self.driver.touch(BY.type('Text').text('我的追剧'))
        self.driver.wait(0.5)
        Step('4.追剧查看成功')
        # 点击type为{Text}并且text为{已完结}的控件
        self.driver.touch(BY.text("已完结", MatchPattern.CONTAINS))
        self.driver.wait(0.5)
        self.driver.check_component_exist(BY.text("选集"), expect_exist=True)
        for w in range(2):
            self.driver.swipe(UiParam.UP, distance=60)
            self.driver.wait(2)
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(2)
        Step('5.观看记录')
        # 等待控件
        self.driver.wait_for_component(BY.text('观看记录'))
        # 点击type为{Text}并且text为{观看记录}的控件
        self.driver.touch(BY.type('Text').text('观看记录'))
        self.driver.wait(0.5)
        if self.driver.find_component(BY.text("追剧")):
            self.driver.touch(BY.text("追剧"))
            self.driver.wait(1)
        if self.driver.find_component(BY.text("已追剧", MatchPattern.CONTAINS)):
            self.driver.touch(BY.text("已追剧", MatchPattern.CONTAINS))
            # 等待控件
            self.driver.wait_for_component(BY.text('取消后您将无法快速找到该剧'))
            # 点击type为{Button}并且text为{确认}的控件
            self.driver.touch(BY.type('Button').text('确认'))
            self.driver.wait(0.5)
        self.driver.wait(1)
        self.driver.touch(BY.text("已完结", MatchPattern.CONTAINS))
        self.driver.wait(0.5)
        self.driver.check_component_exist(BY.text("选集"), expect_exist=True)
        for w in range(2):
            self.driver.swipe(UiParam.UP, distance=60)
            self.driver.wait(2)
        self.driver.press_key(KeyCode.BACK)
    def teardown(self):
        Step('6.关闭设置应用')
        self.driver.stop_app("com.atomicservice.5765880207855735979")