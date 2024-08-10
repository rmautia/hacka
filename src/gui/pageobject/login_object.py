from seleniumpagefactory import PageFactory


class Login(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.timeout = 15
        self.highlight = True

    # define locators dictionary where key name will become WebElement using PageFactory
    locators = {
        "edtUserName": ('XPATH', '//input[@id="emailOrPhone"]'),
        "edtPassword": ('ID', 'password'),
        "btnLogIn": ('XPATH', '(//button[@type="submit"])[2]'),
        "assertHomepage": ('XPATH', '//*[@id="__next"]/header/div/a/img'),
        "continuelogin": ('XPATH', '//button[@type="submit"]'),
        "continuelogin2": ('XPATH', '//button[@data-action-button-primary="true"]')
    }

    def user_name(self, value):
        # set_text(), click_button() methods are extended methods in PageFactory
        self.edtUserName.set_text(value)  # edtUserName become class variable using PageFactory

    def password(self, value):
        self.edtPassword.set_text(value)

    def log_in(self):
        self.btnLogIn.click_button()

    def cont(self):
        self.continuelogin.click_button()

    def cont2(self):
        self.btnLogin.click_button()

    def assertlogin(self):
        return self.assertHomepage.is_displayed()

    def asserthomepage(self):
        return self.assertHomepage.is_displayed()
