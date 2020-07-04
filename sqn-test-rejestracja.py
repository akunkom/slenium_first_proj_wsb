import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

invalid_email="jankot.wp.pl"

class SQNstoreRegistration(unittest.TestCase):

    def setUp(self):

        """
        Warunki wstępne:
        Otwarta przeglądarka Chrome
        """

        # otwarcie przeglądarki
        self.driver = webdriver.Chrome()
        # maksymalizacja okna
        self.driver.maximize_window()
        # otwarcie strony
        self.driver.get("https://sqnstore.pl/")


        """
        Przypadek testowy:
        Błędny e-mail (Brak znaku '@')
        """

    def testWrongEmail(self):
        driver = self.driver

        # 1. Kliknij przycisk "Zarejestruj"
        zaloguj_btn = WebDriverWait(driver, 20)\
        .until(EC.element_to_be_clickable((By.LINK_TEXT, 'Zarejestruj')))
        zaloguj_btn.click()

        # 2. Kliknij przycisk "Nie masz konta? Załóż je tutaj"
        rejestr_btn = driver.find_element_by_xpath('//a[@data-link-action="display-register-form"]')
        driver.execute_script("arguments[0].click();", rejestr_btn)

        # 3. Wpisz imię
        name_field = WebDriverWait(driver, 20)\
        .until(EC.element_to_be_clickable((By.NAME, 'firstname')))
        name_field.send_keys("Janina")

        # 4. Wpisz nazwisko
        surname_field = WebDriverWait(driver, 20)\
        .until(EC.element_to_be_clickable((By.NAME, 'lastname')))
        surname_field.send_keys("Kotowska")

        # 5. Wpisz niepoprawny mail (brak znaku '@')
        email=driver.find_element_by_name('email')
        email.send_keys(invalid_email)

        # 6. Wpisz hasło
        password_field = WebDriverWait(driver, 20)\
        .until(EC.element_to_be_clickable((By.NAME, 'password')))
        password_field.send_keys("Q@werty123")

        # 7. Zaznacz "Akceptuję ogólne warunki użytkowania"
        owu_i_pp=driver.find_element_by_xpath('//input[@name="psgdpr"]')
        owu_i_pp.click()

        # 8. Kliknij "ZAPISZ"
        zapisz=driver.find_element_by_xpath('//button[@data-link-action="save-customer"]')
        zapisz.click()

        # opóźnienie 3s
        sleep(3)

        # screenshot komunikatu o błędzie
        driver.get_screenshot_as_file("screenshot.png")

    def tearDown(self):
        self.driver.quit()

if __name__ =="__main__":
    unittest.main(verbosity=2)
