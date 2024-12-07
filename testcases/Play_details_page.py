# -*- coding: utf-8 -*-
import re

from devicetest.core.test_case import TestCase, Step, CheckPoint
from hypium import *
import time
from hypium.model import UiParam
from hypium import host


class Play_details_page(TestCase):

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
        Step('3.首页')
        self.driver.check_component_exist(BY.text("首页"), wait_time=5)
        self.driver.touch(BY.text("首页"))
        time.sleep(2)
        # if poco(" 将为您创建手机桌面图标 ").exists():
        #     poco("添加应用到桌面").wait_for_appearance()
        #     poco("添加应用到桌面").click()
        #     sleep(1)
        Step('4.看全集跳转')
        self.driver.touch(BY.text("看全集"))
        self.driver.check_component_exist(BY.text("选集"), expect_exist=True)
        time.sleep(1)
        self.driver.touch(BY.text("选集"))
        self.driver.check_component_exist(BY.text("1-20"), wait_time=5)
        self.driver.touch(BY.text("1-20"))
        time.sleep(1)
        self.driver.touch(BY.text("3"))
        # assert_equal("1", "1", "详情页选集成功")
        self.driver.check_component_exist(BY.text("第3集", MatchPattern.CONTAINS), expect_exist=True)
        Step('5.播放页暂停')
        self.driver.touch((0.5, 0.5))
        self.driver.wait(3)
        self.driver.touch((0.5, 0.5))
        Step('6.追剧')
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
        Step('7.点赞')
        if self.driver.find_component(BY.text("0")):
            self.driver.touch(BY.text("0"))
            # assert_equal("1", "1", "首页点赞成功")
            time.sleep(2)
        if self.driver.find_component(BY.text("1")):
            self.driver.touch(BY.text("1"))
            # assert_equal("1", "1", "首页取消点赞成功")
            time.sleep(1)
        Step('8.充值kb')
        while not self.driver.find_component(BY.text("充值规则")):
            self.driver.swipe(UiParam.UP, distance=60)
            time.sleep(1)
        else:
            self.driver.check_component_exist(BY.text("150K币"), wait_time=5)
            self.driver.touch(BY.text("150K币"))
            time.sleep(1)
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
        Step('9.充值看全集')
        while not self.driver.find_component(BY.text("充值规则")):
            self.driver.swipe(UiParam.UP, distance=60)
            time.sleep(2)
        else:
            self.driver.check_component_exist(BY.text("看全集"), wait_time=5)
            self.driver.touch(BY.text("看全集"))
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
            # 等待控件
            self.driver.wait_for_component(BY.text('选集'))
            # 点击type为{Text}并且text为{选集}的控件
            self.driver.touch(BY.type('Text').text('选集'))
            self.driver.wait(0.5)
            input_string = self.driver.find_component(BY.text("已完结", MatchPattern.CONTAINS)).getText()
            match = re.search(r'\d+', input_string)
            number = match.group()
            while not self.driver.find_component(BY.text(number)):
                self.driver.swipe(UiParam.UP, distance=60)
                self.driver.wait(1)
            else:
                # 点击type为{Text}并且text为{15}的控件
                self.driver.touch(BY.type('Text').text(number))
                self.driver.wait(0.5)
                if self.driver.find_component(BY.text("100K币")):
                    qjqs = "全集解锁失败"
                else:
                    qjqs = "全集解锁成功"
            self.host.check_equal(qjqs, "全集解锁成功", "全集解锁是否成功{}".format(number))
            self.driver.wait(180)
        self.driver.press_key(KeyCode.BACK)

    def teardown(self):
        Step('10.关闭设置应用')
        self.driver.stop_app("com.atomicservice.5765880207855735979")