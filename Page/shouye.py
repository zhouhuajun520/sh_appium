from Base.base import Base
import Page, allure


class Shouye(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
    @allure.attach("点击我的")
    def click_wode(self):
        self.click_1(Page.my_btn_id)