from time import sleep

from Base.base import Base
import Page


class  Shezhi(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def tuichu(self, tbg=1):
        self.huadong(1)

        self.click_1(Page.logout_btn_id)
        sleep(2)
        #确定退出
        if  tbg == 1:
            self.click_1(Page.logout_acc_btn_id)
        #取消退出
        else:
            self.click_1(Page.log_out_miss_btn_id)