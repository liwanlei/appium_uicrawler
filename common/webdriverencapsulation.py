'''关于appium的一个简单的封装'''
import os.path
from datetime import timedelta, datetime

from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from common.disapp import make_dis
from common.log import LOG
from selenium.webdriver.support.wait import WebDriverWait

from appium.webdriver.common.touch_action import TouchAction

from common.pictools import opear


class deriver_encapsulation(object):
    def __init__(self, port, Testplatform, platform_version, dev, apkname, activity):
        self.driver = self.init()
        self.port = port
        self.Testplatform = Testplatform
        self.platform_version = platform_version
        self.dev = dev
        self.apkname = apkname
        self.activity = activity

    def init(self):
        dis_app = make_dis(self.Testplatform, self.platform_version, self.dev, self.apkname, self.activity)
        LOG.info(dis_app)
        deriver = webdriver.Remote('http://localhost:{}/wd/hub'.format(str(self.port)), dis_app)
        return deriver

    def find_ele(self, method, path, timeout=1):
        try:
            if method == 'id':
                se = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element_by_id(path))

            elif method == 'xpath':
                se = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element_by_xpath(path))
            elif method == 'css':
                se = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element_by_css_selector(path))

            elif method == 'and':
                se = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element_by_android_uiautomator
                ('new Uiselector().%s' % path))

            elif method == 'class':
                se = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element_by_class_name
                (path))
            elif method == 'name':
                se = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element_by_name
                (path))
            elif method == 'acces':
                se = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element_by_accessibility_id
                (path))
            elif method == 'text':
                se = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element_by_link_text
                (path))
            elif method == 'partial':
                se = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element_by_partial_link_text
                (path))
            elif method == 'tag':
                se = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element_by_tag_name
                (path))
            else:
                raise NameError('no element,please send tag,xpath,text,id,css,id,tag')
            return se
        except:
            return None

    def find_elemens(self, method, path, timeout=1):
        try:
            if method == 'id':
                se = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_id(path))

            elif method == 'xpath':
                se = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_xpath(path))
            elif method == 'css':
                se = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_css_selector(path))

            elif method == 'and':
                se = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_android_uiautomator
                ('new Uiselector().%s' % path))

            elif method == 'class':
                se = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_eelements_by_class_name
                (path))
            elif method == 'name':
                se = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_name
                (path))
            elif method == 'acces':
                se = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_accessibility_id
                (path))
            elif method == 'text':
                se = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_link_text
                (path))
            elif method == 'partial':
                se = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_partial_link_text
                (path))
            elif method == 'tag':
                se = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_tag_name
                (path))
            else:
                raise NameError('no element,please send tag,xpath,text,id,css,id,tag')
            return se
        except:
            return None

    def install(self, path):  # 安装app
        self.driver.install_app(path)

    def uninstall(self,apkname):  # 卸载app
        self.driver.remove_app(apkname)

    def instal_ios(self, bundleId):  # ios
        self.driver.remove_app(bundleId)

    def close(self):  # 关闭app
        self.driver.close_app()

    def reset(self):  # 重置app
        self.driver.reset()

    def hide_keybord(self):  # 隐藏键盘
        self.driver.hide_keyboard()

    def send_keyevent(self, event):  # 只有安卓有
        self.driver.keyevent(keycode=event)

    def sned_press_keycode(self, keycode):  # 安卓有
        self.driver.press_keycode(keycode=keycode)

    def long_press_keycode(self, keycode):  # 长按发送
        self.driver.long_press_keycode(keycode)

    def current_activity(self):
        '''
        获取当前的activity
        '''
        activity = self.driver.current_activity
        return activity

    def wait_activity(self, activity, times, interval=1):
        self.driver.wait_activity(activity, timeout=times, interval=interval)


    def run_back(self, second):
        self.driver.background_app(seconds=second)

    def is_app_installed(self, baoming):  # ios需要buildid
        self.driver.is_app_installed(baoming)

    def launch_app(self):  # 启动app
        self.driver.launch_app()

    def start_acti(self, app_package, app_activity):
        self.driver.start_activity(app_package, app_activity)

    def ios_lock(self, locktime):
        self.driver.lock(locktime)

    def yaoshouji(self):
        self.driver.shake()

    def open_tongzhi(self):  # 安卓api 18以上
        self.driver.open_notifications()

    def renturn_network(self):  # 返回网络
        network_type = self.driver.network_connection
        return network_type

    def set_network_type(self, type):
        from appium.webdriver.connectiontype import ConnectionType
        if type == 'wifi' or type == 'WIFI' or type == 'w' or type == 'WIFI_ONLY':
            self.driver.set_network_connection(ConnectionType.WIFI_ONLY)
        elif type == 'data' or type == 'DATA' or type == 'd' or type == 'DATA_ONLY':
            self.driver.set_network_connection(ConnectionType.DATA_ONLY)
        elif type == 'ALL' or type == 'all' or type == 'a' or type == 'ALL_NETWORK_ON':
            self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
        elif type == 'NO' or type == 'no' or type == 'n' or type == 'NO_CONNECTION':
            self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        elif type == 'AIRPLANE_MODE' or type == 'air' or type == 'ar' or type == 'fly':
            self.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
        else:
            raise NameError('plase wifi ,data,all,no,fly')

    def open_location(self):
        self.driver.toggle_location_services()

    def set_location(self, weidu, jingdu, haiba):
        self.driver.set_location(weidu, jingdu, haiba)

    def get_size(self):
        size = self.driver.get_window_size()
        return size

    def sendkeys(self, element, text):
        element.click()
        element.clear()
        element.send_keys(text)

    def screen(self, filename):
        self.driver.get_screenshot_as_file(filename)

    def closedriver(self):
        self.driver.close()

    def killdriver(self):
        self.driver.quit()

    def get_wiow_size(self):  # 获取窗口大小
        return self.driver.get_window_size()

    def swap(self, s_x, s_y, e_x, e_y):  # 从一点到另一点
        self.driver.flick(s_x, s_y, e_x, e_y)

    def swip_end(self, s_x, s_y, e_x, e_y, duration=100):
        self.driver.swipe(s_x, s_y, e_x, e_y, duration=duration)

    def toche(self, x, y, duration=500):
        self.driver.tap([(x, y)], duration=duration)

    def scroll(self, x, y):  # 滚动元素
        self.driver.scroll(x, y)

    def drag_and_drop(self, e1, e2):  # 移动元素
        self.driver.drag_and_drop(e1, e2)

    def contexts_is(self):  # 可用
        self.driver.contexts()

    def push(self, data, path):
        self.driver.push_file(data, path)

    def pull(self, path):
        self.driver.pull_file(path)

    def take_screen(self, basepath, bound=None):
        yesterday = (datetime.now() + timedelta()).strftime("%Y_%m_%d_%H_%S_%M")
        paths = os.path.join(basepath, yesterday + ".png")
        self.driver.get_screenshot_as_file(paths)
        if bound != None:
            opear(paths, bound)

    def swpape(self, startx, starty, endx, endy):
        LOG.info("scroll from : startX " + str(startx) + ", startY " + str(starty) + ", to  endX " + str(
            endx) + ",endY " + str(endy))
        self.driver.swipe(startx, starty, endx, endy, 1000)

    def socrae(self):
        '''
        滑动
        '''
        wid_hight = self.get_wiow_size()
        whidt = wid_hight['width']
        height = wid_hight['height']
        startx = whidt * 0.5
        starty = height * 0.5
        endx = startx / 2
        endy = 50
        self.swpape(startx, starty, endx, endy)

    def page_soucre(self):
        '''
        获取当前页面的布局

        '''
        return self.driver.page_source

    def click(self, x, y):
        '''
        固定坐标的点击
        '''
        t = TouchAction(self.driver)
        try:
            t.tap(x=x, y=y).wait(10).perform()
        except Exception as e:
            LOG.error("点击固定坐标异常，原因：{}".format(str(e)))

    def longcick(self, x, y):
        '''
        在某个地方长按
        '''
        t = TouchAction(self.driver)
        t.long_press(x=x, y=y).wait(10)

    def doubletap(self, x, y):
        t = TouchAction(self.driver)
        t.tap(x=x, y=y).wait(10).tap(x=x, y=y).perform()

    def draginde(self, x, y, enx, eny, andriod):
        if y < 200:
            y = 200
        t = TouchAction(self.driver)
        if andriod is False:
            enx -= x
            eny -= y
        if andriod:
            t.long_press(x=x, y=y).move_to(x=x, y=y).release().perform()
        else:
            t.long_press(x=x, y=y).wait(10).move_to(x=x, y=y).release().perform()

    def pinch(self, x, y, enx, eny, isup, height, andriod):
        '''
        设置app的放大还是缩小
        '''
        lineCenterX = (x + enx) / 2
        lineCenterY = (y + eny) / 2
        if x > enx:
            x, enx = enx, x
            y, eny = eny, y
        if y < 200:
            y = 200
        if eny < 200:
            eny = 200
        if y > height - 200:
            y = height - 200
        if eny > height - 200:
            eny = height - 200
        toochx = TouchAction(self.driver)
        touchy = TouchAction(self.driver)
        if andriod:
            if isup:
                toochx.press(x=lineCenterX, y=lineCenterY).move_to(x=x, y=y).release()
                touchy.press(x=lineCenterX, y=lineCenterY).move_to(x=enx, y=eny).release()
            else:
                toochx.press(x=x, y=y).move_to(x=lineCenterX, y=lineCenterY).release()
                touchy.press(x=enx, y=eny).move_to(x=lineCenterX, y=lineCenterY).release()
        else:
            if isup:
                toochx.press(x=lineCenterX, y=lineCenterY).wait(10).move_to(100, 0).release()
                touchy.press(x=lineCenterX, y=lineCenterY).wait(10).move_to(-100, 0).release()
            else:
                toochx.press(x=x, y=y).wait(10).move_to(x=lineCenterX - x, y=0).release()
                touchy.press(x=enx, y=eny).wait(10).move_to(x=lineCenterX - enx, y=0).release()
