import sys,os


sys.path.append(os.getcwd())

from time import sleep

from Base.get_data import Get_data
from Base.get_driver import get_d
from Page.page_tongyi import Tongyi
import pytest
from selenium.common.exceptions import TimeoutException

def get_login_data():
    # 结果列表
    login_list = []
    data = Get_data().get_yaml_data("aolai.yml")
    # return data
    for i in data.keys():
        login_list.append((i, data.get(i).get("phone"), data.get(i).get("passwd"),
                           data.get(i).get("tag"), data.get(i).get("tag_message"),
                           data.get(i).get("expect_result")))
    return login_list


class Test_1():
    def setup_class(self):
        self.aa = Tongyi(get_d("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity"))
    def teardown_class(self):
        self.aa.driver.quit()
    @pytest.mark.parametrize("test_num,phone,passwd,tag,tag_message,expect_result", get_login_data())
    def test_01(self,test_num,phone,passwd,tag,tag_message,expect_result):
        self.aa.tong_shouye().click_wode()
        self.aa.tong_zc().click_denglu()
        self.aa.tong_denglu().shulu(phone, passwd)
        if tag:
            try:
                try:
                    assert self.aa.tong_geren().wodeyouhuiq() == expect_result
                except  AssertionError as a:
                    print(a.__str__())
                sleep(3)
                self.aa.tong_geren().click_shezhi()
                sleep(3)
                self.aa.tong_shezhi().tuichu()
            except TimeoutException :
                self.aa.tong_denglu().close_login_page()
                assert False
        else:
            try:
                tangc = self.aa.tong_shezhi().get_toast(tag_message)
                dlu = self.aa.tong_denglu().if_login_btn_exits()
                assert  dlu and tangc == expect_result
            except  TimeoutException as e:
                assert False
            finally:
                self.aa.tong_denglu().close_login_page()
        #
        # adb=self.aa.tong_geren().wodeyouhuiq()
        # assert adb == expect_result
        # self.aa.tong_geren().click_shezhi()
        # self.aa.tong_shezhi().tuichu()