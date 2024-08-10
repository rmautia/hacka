from gui.driver import drivermanager
from gui.pageobject import login_object

driverObj = drivermanager.Driver()


class LoginPage:
    def open_login_page(self, url):
        driver = driverObj.fox_driver()
        driver.get(url)
        driver.maximize_window()
        # login_obj = login_object.Login(driver)
        # login_obj.log_in()
        # welcome = login_obj.assertlogin()
        # assert welcome == True
        # driver.implicitly_wait(40)
        return driver
        # login_obj = login_object.Login(self.driver)

    def give_user_name_and_password(self, driver):
        login_obj = login_object.Login(driver)
        login_obj.user_name("+254704445630")
        login_obj.password("Thejourney1.")
        login_obj.log_in()

    def assert_home_page(self, driver):
        login_obj = login_object.Login(driver)
        homepg = login_obj.asserthomepage()
        assert homepg == True
        driver.implicitly_wait(4000)

