#Test5 : For new user OR who don't have account on wyscout we can directly use "chooseplan" option
###########################################################################################################

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

            Choose_plan= driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div[3]/a").click()
            time.sleep(5)


            cur_url = driver.current_url
            expected_url = 'https://wyscout.com/pricing/'
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
