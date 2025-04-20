import pytest
from pages.login_page import LoginPage

# Constantes para teste (nome listado está como John Doe, aniversário setado para 01/01/2000)

VALID_EMAIL = "jefefermcshart@gmail.com"
VALID_PASSWORD = "validAndSecurePassword"
INVALID_EMAIL = "invalidemail.com"
INVALID_PASSWORD = "invalidPassword"

@pytest.mark.usefixtures("browser")
class TestLogin:

    def test_login_com_credenciais_validas(self, browser):
        page = LoginPage(browser)
        page.open()
        page.fill_login_email(VALID_EMAIL)
        page.fill_password(VALID_PASSWORD)
        page.click_login()
        assert page.is_logged_in()

    def test_login_com_email_invalido(self, browser):
        page = LoginPage(browser)
        page.open()
        page.fill_login_email(INVALID_EMAIL)
        page.fill_password(INVALID_PASSWORD)
        page.click_login()
        assert "Invalid email address." in page.get_error_message()

    def test_login_com_senha_incorreta(self, browser):
        page = LoginPage(browser)
        page.open()
        page.fill_login_email(VALID_EMAIL)
        page.fill_password(INVALID_PASSWORD)
        page.click_login()
        assert "Authentication failed." in page.get_error_message()
        
    def test_criacao_de_conta_com_email_existente(self, browser):
        page = LoginPage(browser)
        page.open()
        page.fill_sign_up_email(VALID_EMAIL)
        page.click_create()
        assert "An account using this email address has already been registered. Please enter a valid password or request a new one." in page.get_error_message()
