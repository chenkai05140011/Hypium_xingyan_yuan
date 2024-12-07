# -*- coding: utf-8 -*-
from devicetest.core.test_case import TestCase, Step, CheckPoint
from hypium import *
import time
from hypium.model import UiParam
from hypium import host

class Home_page(TestCase):

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
        Step('3.首页')
        self.driver.check_component_exist(BY.text("首页"), wait_time=5)
        self.driver.touch(BY.text("首页"))
        time.sleep(2)
        self.driver.check_component_exist(BY.text("看全集"), wait_time=5)
        Step('4.追剧')
        if self.driver.find_component(BY.text("追剧")):
            self.driver.touch(BY.text("追剧"))
            # self.host.check_equal(1, 1, "a != b")
            time.sleep(3)
        if self.driver.find_component(BY.text("已追剧")):
            self.driver.touch(BY.text("已追剧"))
            time.sleep(1)
            if self.driver.find_component(BY.text("取消后您将无法快速找到该剧")):
                self.driver.touch(BY.text("确认"))
                time.sleep(1)
                # assert_equal("1", "1", "首页取消追剧成功")
        Step('5.点赞')
        if self.driver.find_component(BY.text("0")):
            self.driver.touch(BY.text("0"))
            # assert_equal("1", "1", "首页点赞成功")
            time.sleep(2)
        if self.driver.find_component(BY.text("1")):
            self.driver.touch(BY.text("1"))
            # assert_equal("1", "1", "首页取消点赞成功")
            time.sleep(1)
        Step('6.首页暂停')
        self.driver.touch((0.5, 0.5))
        self.driver.wait(3)
        self.driver.touch((0.5, 0.5))
        Step('7.看全集跳转')
        self.driver.touch(BY.text("看全集"))
        self.driver.find_component(BY.text("选集"))
        self.driver.press_key(KeyCode.BACK)
        time.sleep(1)
        Step('8.首页视频滑动播放')
        for w in range(5):
            self.driver.swipe(UiParam.UP, distance=60)
            time.sleep(5)


    def teardown(self):
        Step('9.关闭设置应用')
        self.driver.stop_app("com.atomicservice.5765880207855735979")