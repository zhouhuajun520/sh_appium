from Base.base import Base
import Page, allure


class Denglu(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
    @allure.step("输入信息")
    def shulu(self, name, passwd):
        allure.attach("输入用户名", name)
        self.send_1(Page.login_account_id, name)
        allure.attach("输入密码", passwd)
        self.send_1(Page.login_passwd_id, passwd)
        self.click_1(Page.login_btn_id)
    def if_login_btn_exits(self):
        # 判断登录按钮是否存在 存在返回True 不存在返回False
        try:
            self.element(Page.login_btn_id)
            allure.attach("登录按钮是否存在", "存在")
            return True
        except Exception as e:
            allure.attach("登录按钮是否存在", "不存在")
            return False
    @allure.step("关闭登录页")
    def close_login_page(self):
        # 关闭登录页
        self.click_1(Page.login_close_btn_id)
