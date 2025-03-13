import unittest
import configparser
import sys
import os
import logging
from utils.browser_setup import BrowserSetup
from pages.home_page import HomePage
import HtmlTestRunner

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class HomePageTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Khởi tạo trình duyệt trước khi chạy các test case"""
        config = configparser.ConfigParser()
        config.read('config.ini')
        
        try:
            cls.home_url = config['app']['login_url']
            cls.driver = BrowserSetup.get_driver()
            cls.driver.get(cls.home_url)
            cls.home_page = HomePage(cls.driver)
            logging.info("Trình duyệt đã được khởi động thành công")
        except Exception as e:
            logging.error(f"Lỗi khi khởi tạo trình duyệt: {e}")
            raise

    def test_product_details_display(self):
        """Kiểm tra thông tin chi tiết của sản phẩm"""
        logging.info("Chạy test: Kiểm tra thông tin sản phẩm")
        
        self.assertTrue(self.home_page.is_product_displayed(), "Sản phẩm không hiển thị")
        self.assertTrue(self.home_page.get_product_title(), "Tiêu đề sản phẩm không hiển thị")
        self.assertTrue(self.home_page.get_product_time(), "Thời gian sản phẩm không hiển thị")
        self.assertTrue(self.home_page.get_product_price(), "Giá sản phẩm không hiển thị")

    def test_add_to_basket(self):
        """Kiểm tra thêm sản phẩm vào giỏ hàng"""
        logging.info("Chạy test: Thêm sản phẩm vào giỏ hàng")
        
        initial_count = int(self.home_page.get_basket_count())
        self.home_page.click_add_to_basket()
        new_count = int(self.home_page.get_basket_count())
        
        self.assertGreater(new_count, initial_count, "Số lượng giỏ hàng không tăng")

    def test_add_to_cart(self):
        """Kiểm tra thêm sản phẩm vào cart"""
        logging.info("Chạy test: Thêm sản phẩm vào cart")
        
        initial_count = int(self.home_page.get_cart_count())
        self.home_page.click_add_to_cart()
        new_count = int(self.home_page.get_cart_count())
        
        self.assertGreater(new_count, initial_count, "Số lượng cart không tăng")

    def test_navigation_buttons(self):
        """Kiểm tra điều hướng trang đăng nhập và đăng ký"""
        logging.info("Chạy test: Điều hướng trang login và register")
        
        self.home_page.click_login()
        self.assertIn("signin", self.driver.current_url, "Không mở được trang đăng nhập")

        self.driver.back()

        self.home_page.click_register()
        self.assertIn("register", self.driver.current_url, "Không mở được trang đăng ký")

    @classmethod
    def tearDownClass(cls):
        """Đóng trình duyệt sau khi chạy tất cả test case"""
        if cls.driver:
            cls.driver.quit()
            logging.info("Trình duyệt đã được đóng")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports', report_name='HomePageTestReport'))
