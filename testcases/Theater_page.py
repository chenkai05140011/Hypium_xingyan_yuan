# -*- coding: utf-8 -*-
from devicetest.core.test_case import TestCase, Step, CheckPoint
from hypium import *
import time
from hypium.model import UiParam
from hypium import host

class Theater_page(TestCase):

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
        Step('3.剧场')
        self.driver.check_component_exist(BY.text("剧场"), wait_time=5)
        self.driver.touch(BY.text("剧场"))
        self.driver.wait(2)
        Step('4.剧名进行搜索')
        self.driver.check_component_exist(BY.text("必看榜"), wait_time=5)
        self.driver.wait(0.5)
        self.driver.touch(BY.text("请输入剧名进行搜索"))
        self.driver.wait(0.5)
        self.driver.input_text(BY.type("TextInput"), "最狂")
        self.driver.wait(0.5)
        self.driver.touch(BY.isAfter(BY.type('TextInput')).isBefore(BY.type('Scroll')).type('Text').text('搜索'))
        self.driver.wait(0.5)
        self.driver.check_component_exist(BY.text("已完结", MatchPattern.CONTAINS), wait_time=5)
        self.driver.touch(BY.text("已完结", MatchPattern.CONTAINS))
        self.driver.check_component_exist(BY.text("选集"), expect_exist=True)
        for w in range(3):
            self.driver.swipe(UiParam.UP, distance=60)
            time.sleep(3)
        self.driver.press_key(KeyCode.BACK)
        time.sleep(2)
        self.driver.touch(BY.isAfter(BY.text('最狂')).isBefore(BY.type('Scroll')).type('Image'))
        self.driver.wait(0.5)
        # assert_equal("1", "1", "搜索成功")
        self.driver.check_component_exist(BY.text("1"), expect_exist=True)
        self.driver.touch(BY.text("1"))
        self.driver.check_component_exist(BY.text("选集"), expect_exist=True)
        for w in range(3):
            self.driver.swipe(UiParam.UP, distance=60)
            self.driver.wait(3)
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(0.5)
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(0.5)
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(0.5)
        Step('5.搜索热榜')
        self.driver.check_component_exist(BY.text("必看榜"), wait_time=5)
        # 通过相对位置点击控件
        self.driver.touch(BY.isAfter(BY.text('搜索')).isBefore(BY.type('SwiperIndicator')).type('Image'))
        self.driver.wait(0.5)
        for w in range(3):
            self.driver.swipe(UiParam.UP, distance=60)
            self.driver.wait(3)
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(0.5)
        Step('6.必看榜')
        self.driver.check_component_exist(BY.text("必看榜"), wait_time=5)
        # 点击type为{Text}并且text为{必看榜}的控件
        self.driver.touch(BY.type('Text').text('必看榜'))
        self.driver.wait(0.5)
        # 通过相对位置点击控件
        self.driver.touch(BY.text("已完结", MatchPattern.CONTAINS))
        self.driver.wait(0.5)
        for w in range(3):
            self.driver.swipe(UiParam.UP, distance=60)
            self.driver.wait(3)
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(0.5)
        Step('7.热播榜')
        self.driver.check_component_exist(BY.text("热播榜"), wait_time=5)
        self.driver.touch(BY.type('Text').text('热播榜'))
        self.driver.wait(0.5)
        # 通过相对位置点击控件
        self.driver.touch(BY.text("已完结", MatchPattern.CONTAINS))
        self.driver.wait(0.5)
        for w in range(3):
            self.driver.swipe(UiParam.UP, distance=60)
            self.driver.wait(3)
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(0.5)
        Step('8.榜单查看更多')
        # 点击type为{Text}并且text为{查看更多}的控件
        self.driver.check_component_exist(BY.text("查看更多"), wait_time=5)
        self.driver.touch(BY.type('Text').text('查看更多'))
        self.driver.wait(0.5)
        self.driver.check_component_exist(BY.text("必看榜"), wait_time=5)
        self.driver.touch(BY.type('Text').text('必看榜'))
        self.driver.wait(0.5)
        self.driver.touch(BY.text("已完结", MatchPattern.CONTAINS))
        self.driver.wait(0.5)
        for w in range(3):
            self.driver.swipe(UiParam.UP, distance=60)
            self.driver.wait(3)
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(0.5)
        self.driver.check_component_exist(BY.text("热播榜"), wait_time=5)
        self.driver.touch(BY.type('Text').text('热播榜'))
        self.driver.wait(0.5)
        self.driver.touch(BY.text("已完结", MatchPattern.CONTAINS))
        if self.driver.find_component(BY.text("追剧")):
            self.driver.check_component_exist(BY.text("选集"), expect_exist=True)
            self.driver.touch(BY.text("追剧"))
            # self.host.check_equal(1, 1, "a != b")
            time.sleep(2)
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(0.5)
        self.driver.press_key(KeyCode.BACK)
        self.driver.wait(0.5)
        # 断言text为{古装}的控件存在
        Step('9.类型古装')
        self.driver.check_component_exist(BY.text('古装'))
        self.driver.wait(0.5)
        self.driver.touch(BY.type('Text').text('古装'))
        self.driver.wait(1)
        # assert_equal("1", "1", "剧场切换类型古装成功")
        self.driver.wait(1)
        Step('10.立即观看')
        if self.driver.find_component(BY.text("立即观看")):
            # 点击type为{Text}并且text为{立即观看}的控件
            self.driver.touch(BY.type('Text').text('立即观看'))
            self.driver.wait(0.5)
            self.driver.check_component_exist(BY.text("选集"), expect_exist=True)
            self.driver.press_key(KeyCode.BACK)
            self.driver.wait(0.5)
        for w in range(3):
            self.driver.swipe(UiParam.UP, distance=60)
            time.sleep(1)



    def teardown(self):
        Step('11.关闭设置应用')
        self.driver.stop_app("com.atomicservice.5765880207855735979")