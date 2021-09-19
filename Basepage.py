class Basepage():
    def __init__(self,driver):  #封装驱动
        self.driver = driver
    def open_url(self,url):    #打开浏览器
        self.driver.get(url)
    def find_element(self,*loc):    #8种定位
        return self.driver.find_element(*loc)