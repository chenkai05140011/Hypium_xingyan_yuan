# -*- coding: utf-8 -*-
from devicetest.core.test_case import TestCase, Step, CheckPoint
from hypium import *
from hypium.model import UiParam


class cssc(TestCase):

    def __init__(self, configs):
        self.TAG = self.__class__.__name__
        TestCase.__init__(self, self.TAG, configs)
        self.driver = UiDriver(self.device1)
        self.driver_width, self.driver_height = self.driver.get_display_size()

    def setup(self):
        Step("预置条件1xxxx")
        # todo
        Step("预置条件2xxxx")
        # todo

    def process(self):
        # 通过相对位置点击控件
        if not self.driver.find_component(BY.key('AppIcon_Image_com.huawei.hmos.camera_218103928_0')):
            self.driver.press_key(KeyCode.POWER)
            self.driver.swipe(UiParam.UP, distance=60)
        else:
            # 通过相对位置点击控件
            self.driver.touch(BY.key('AppIcon_Image_com.ohos.contacts_100664105_0'))
            self.driver.wait(0.5)


    def teardown(self):
        Step("收尾工作xxxx")
        # todo