from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://automationpractice.pl/index.php?controller=authentication&back=my-account"

    def open(self):
        self.driver.get(self.url)

    def fill_login_email(self, email):
        self.driver.find_element(By.ID, "email").send_keys(email)
        
    def fill_sign_up_email(self, email):
        self.driver.find_element(By.ID, "email_create").send_keys(email)    

    def fill_password(self, password):
        self.driver.find_element(By.ID, "passwd").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, "SubmitLogin").click()
        
    def click_create(self):
        self.driver.find_element(By.ID, "SubmitCreate").click()

    def get_error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger").text

    def is_logged_in(self):
        return "my-account" in self.driver.current_url
