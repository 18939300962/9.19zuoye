from xue_001.lianxi004.Basepage import Basepage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Es
from time import sleep
class Fengzpage(Basepage):
    bd_loc01 = (By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/a[1]")
    bd_loc02 = (By.LINK_TEXT,"QQ")
    bd_loc03 = (By.ID, "ptlogin_iframe")
    bd_loc04 = (By.ID,"switcher_plogin")
    bd_loc05 = (By.NAME,"u")
    bd_loc06 = (By.NAME,"p")
    bd_loc07 = (By.CSS_SELECTOR,"html body div#login.login div#web_qr_login.web_qr_login div#web_qr_login_show.web_qr_login_show div#web_login.web_login div.login_form form#loginform div.submit a.login_button input#login_button.btn")
#==============搜索商品===================================================
    ss_loc01 = (By.ID,"searchKeywords")
    ss_loc02 = (By.ID,"searchSubmit")
    ss_loc03 = (By.CSS_SELECTOR,"#ssdsn_search_pro_baoguang-1-0-1_1_01\:0070123434_10059288390 > img:nth-child(1)")
    ss_loc04 = (By.XPATH,'//*[@id="addCart"]')
# ============QQ登录业务================================================================================
    def qdl(self):    #点击登录
        self.find_element(*self.bd_loc01).click()
    def qqdl(self):   #点击qq登录
        self.find_element(*self.bd_loc02).click()
    def kuangjia(self):   #进入frame框架
        kj = self.find_element(*self.bd_loc03)
        self.driver.switch_to.frame(kj)
    def zhdl(self):     #账号密码登录
        self.find_element(*self.bd_loc04).click()
    def srzh(self):   #输入账号
        self.find_element(*self.bd_loc05).send_keys("1914035339")
    def srmm(self):    #输入密码
        self.find_element(*self.bd_loc06).send_keys("yang.1998")
    def djdl(self):    #点击登录
        self.find_element(*self.bd_loc07).click()
    def syqqdl(self):
        self.open_url("https://www.suning.com/")
        sleep(2)
        self.qdl()
        sleep(2)
        self.qqdl()
        sleep(5)
        self.kuangjia()
        sleep(2)
        self.zhdl()
        sleep(2)
        self.srzh()
        sleep(2)
        self.srmm()
        sleep(2)
        self.djdl()
        sleep(2)
#=========商品搜索====================================================================
    def ssnr(self):   #输入商品内容
        self.find_element(*self.ss_loc01).send_keys("迪迦")
    def djss(self):   #点击搜素
        self.find_element(*self.ss_loc02).click()
    def ymxh(self):   #下滑页面到指定位置
        self.driver.execute_script("window.scrollTo(0,1000)")
    def djsp(self):  #点击搜索的商品
        self.find_element(*self.ss_loc03).click()
    def ymqh(self):   #切换页面
        self.driver.switch_to.window(self.driver.window_handles[-1])
    def jrgwc(self):   #点击加入购物车
        self.find_element(*self.ss_loc04).click()
    def hddb(self):   #页面滑动到顶部
        self.driver.execute_script("window.scrollTo(0,0)")
    def hddi(self):   #页面滑动到底部
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    def snjrgwc(self):
        self.open_url("https://www.suning.com/")
        sleep(2)
        self.driver.maximize_window()     #浏览器最大化
        sleep(1)
        self.ssnr()
        sleep(1)
        self.djss()
        sleep(1)
        self.ymxh()
        sleep(2) #强制等待
        self.djsp()
        self.driver.implicitly_wait(5)  #隐式等待
        self.ymqh()
        sleep(1)
        self.ymxh()
        sleep(1)
        # 显示等待
        WebDriverWait(self.driver,10,0.5).until(Es.presence_of_element_located((self.ss_loc04))).click()
        sleep(3)


