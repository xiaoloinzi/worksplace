# encoding=utf-8
class Login():

    #登录
    def user_login(self,driver):
        driver.switch_to_frame('x-URS-iframe')
    # 登录
        driver.find_element_by_name('email').clear()
        driver.find_element_by_name('email').send_keys('username')
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys('password')
        driver.find_element_by_id('dologin').click()

    def user_logout(self,driver):
        driver.switch_to_frame('x-URS-iframe')
        driver.find_element_by_link_text('退出').click()
        driver.quit()


