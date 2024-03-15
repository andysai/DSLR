from cefpython3 import cefpython as cef

class MyApp(object):
    def __init__(self):
        self.window_info = cef.WindowInfo()
        self.browser_settings = dict()
        self.browser_settings["windowless_rendering_enabled"] = True
        self.browser_settings["plugins_disabled"] = True
        self.browser_settings["javascript_close_windows"] = False
        self.browser_settings["javascript_access_clipboard"] = False
        self.browserSettings["dom_paste_disabled"] = False
        self.browser = cef.CreateBrowserSync(self.window_info, settings=self.browser_settings)
        self.browser.LoadUrl("http://www.baidu.com")

print(MyApp())
