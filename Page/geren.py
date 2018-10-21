from Base.base import Base
import Page, allure


class  Geren(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
    def wodeyouhuiq(self):
        wude = self.element(Page.person_coupons_id).text
        allure.attach("获取文本信息", "{}",format(wude))
        return wude
    @allure.step("点击设置")
    def click_shezhi(self):
        self.click_1(Page.setting_btn_id)