# encoding=utf-8
class Login():
#修改user_login（）方法的入参，为其增加username、password的入参，
# 将得到的具体参数作为登录时的数据
    #修改接口需要驱动、用户名、密码等参数
    def user_login(self,driver,username,password):
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











