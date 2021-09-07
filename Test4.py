# Test4 : Login successfully and after login it will be search INDIA or other contents that we will want to search
# For Testing purpose i put only one content that is "INDIA" but we can put multiple contents.
#######################################################################################################################

from selenium import webdriver
import time
import unittest


class MyTestwyscout(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
    def test_login(self):
        driver= self.driver
        try:
            driver.get('https://platformrc.wyscout.com/app/')
            driver.maximize_window()
        except Exception as ex:
            print(ex)
        else:
            time.sleep(5)
            cur_url = driver.current_url
            expected_url = 'https://platformrc.wyscout.com/app/'
            try:
                self.assertEqual(cur_url, expected_url, 'Failed!')
            except Exception as ex:
                print(ex)



            Email = driver.find_element_by_id("login_username")
            Password = driver.find_element_by_id('login_password')
            time.sleep(5)

            Email.clear()
            Password.clear()
            Email.send_keys("sakshipawar358@gmail.com")
            Password.send_keys("pw_IndiaTest!")
            time.sleep(5)
            driver.find_element_by_id('login_button').click()
            time.sleep(3)
            driver.find_element_by_xpath("/html/body/div[9]/div/div/div/div[2]/button").click()
            time.sleep(10)
            elem = driver.find_element_by_name("search")
            elem.clear()
            elem.send_keys("INDIA")


            cur_url = driver.current_url
            expected_url = 'https://platformrc.wyscout.com/app/'
            time.sleep(10)



            try:
                self.assertEqual(cur_url, expected_url, "Not able to SignIn")
            except Exception as ex:
                print("Username and Password is incorrect {}".format(ex))
            time.sleep(20)


    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()
