from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.checkout_page import CheckoutPage
from .pages.base_page import BasePage
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TestUserCheckout():
    @pytest.fixture(scope="function", autouse=True)
    def setup_login(self, browser, link_login, email, password_valid):
        page = LoginPage(browser, link_login)
        page.open()
        password1 = password2 = password_valid
        page.new_user_registration(email, password1, password2)
        page.should_be_authorized_user()

    @pytest.mark.need_review_custom_scenarios
    def test_user_can_order_product_from_product_page(self, browser, link_product, product_title, product_price, order_confirmation_message, test_first_name, test_last_name, test_first_lane_address, test_city, postcode, country):
        page = ProductPage(browser, link_product)
        page.open()
        page.add_product_to_basket()
        page.go_to_checkout_page()
        checkout_page = CheckoutPage(browser, browser.current_url)
        checkout_page.fill_all_required_fields_and_click_continue(test_first_name, test_last_name, test_first_lane_address, test_city, postcode, country)
        checkout_page.skip_payment_methods()
        checkout_page.place_order()
        assert order_confirmation_message in checkout_page.order_confirmation(), "Order confirmation message is wrong"
        assert f'{test_first_name} {test_last_name}\n{test_first_lane_address}\n{test_city}\n{postcode}\n{country}' == checkout_page.check_shipping_address(), "Shipping address confirmation is wrong"
        assert product_title == checkout_page.check_order_contents(), "Order content confirmation is wrong"
        assert product_price == checkout_page.check_order_total(), "Product price on preview page is wrong"

