import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SQNstoreRegistration(unittest.TestCase):

    def setUp(self):

        """
        Warunki wstępne:
        Przeglądarka otwarta na stronie www.sqnstore.pl
        Użytkownik zalogowany
        """

        self.driver = webdriver.Chrome()
        # maksymalizacja okna
        self.driver.maximize_window()
        # otwarcie strony
        self.driver.get("https://sqnstore.pl/")

        # 1. Kliknij przycisk "Zarejestruj"
        zaloguj_btn = WebDriverWait(self.driver, 20)\
        .until(EC.element_to_be_clickable((By.LINK_TEXT, 'Zarejestruj')))
        zaloguj_btn.click()

        # 2. Wpisz e-mail
        mail_field = WebDriverWait(self.driver, 20)\
        .until(EC.element_to_be_clickable((By.NAME, 'email')))
        mail_field.send_keys("testproj20@wp.pl")

        # 3. Wpisz hasło
        mail_field = WebDriverWait(self.driver, 20)\
        .until(EC.element_to_be_clickable((By.NAME, 'password')))
        mail_field.send_keys("haslo2020")

        # 4. Kliknij "ZALOGUJ SIĘ"
        zaloguj=self.driver.find_element_by_xpath('//button[@data-link-action="sign-in"]')
        self.driver.execute_script("arguments[0].click();", zaloguj)

        # opóźnienie 5s
        sleep(5)


        """
        Przypadek testowy 1:
        Dodanie książki dostępnej w magazynie do koszyka
        """

    def testBasket1(self):
        driver = self.driver

        # 1. Powrót na stronę główną sklepu (kliknij logo)
        logo=driver.find_element_by_xpath('//img[@alt="SQN Store"]')
        logo.click()

        # 2. Kliknij "DODAJ DO KOSZYKA"
        produkt=driver.find_element_by_xpath('//a[@data-id-product="706"]')
        driver.execute_script("arguments[0].click();", produkt)

        # opóźnienie 10s
        sleep(10)

        # screenshot strony
        driver.get_screenshot_as_file("screenshot1.png")

        #### TEST ####

        # Szukam komunikatów na stronie
        errors=driver.find_elements_by_xpath('//*[@id="myModalLabel"]')
        # szukam widocznych (wyświetlonych) komunikatów
        visible_errors=[]
        for e in errors:
            if e.is_displayed():
                visible_errors.append(e)
        # Sprawdzam, czy widoczny jest jeden komunikat
        print(len(visible_errors))
        assert len(visible_errors) == 1
        # Porównuję treść komunikatów
        print(visible_errors[0].text)
        assert visible_errors[0].text=="Produkt dodany poprawnie do Twojego koszyka"

        sleep(3)

        """
        Przypadek testowy 2:
        Dodanie książki niedostępnej w magazynie do koszyka
        """

    def testBasket2(self):
        driver = self.driver

        # 1. Powrót na stronę główną sklepu (kliknij logo)
        logo=driver.find_element_by_xpath('//img[@alt="SQN Store"]')
        logo.click()

        # 2. Kliknij "BRAK W MAGAZYNIE"
        produkt=driver.find_element_by_xpath('//*[@id="featured"]/div/div[1]/div/div[4]/div/div[1]/div[2]/div[2]/a/span')
        driver.execute_script("arguments[0].click();", produkt)

        # opóźnienie 10s
        sleep(10)

        # screenshot strony
        driver.get_screenshot_as_file("screenshot2.png")

        #### TEST ####

        # Szukam komunikatów na stronie
        errors=driver.find_elements_by_xpath('//*[@id="myModalLabel"]')
        # Szukam widocznych (wyświetlonych) komunikatów
        visible_errors=[]
        for e in errors:
            if e.is_displayed():
                visible_errors.append(e)
        # Sprawdzam, czy widoczny jest jeden komunikat
        print(len(visible_errors))
        assert len(visible_errors) == 1
        # Porównuję komunikaty
        print(visible_errors[0].text)
        assert visible_errors[0].text!="Produkt dodany poprawnie do Twojego koszyka"


    def tearDown(self):
        self.driver.quit()

if __name__ =="__main__":
    unittest.main(verbosity=2)
