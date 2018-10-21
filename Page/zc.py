from Base.base import Base
import Page, allure


class Zhuce(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
    @allure.attach("点击登录按钮")
    def click_denglu(self):
        self.click_1(Page.exits_account_id)