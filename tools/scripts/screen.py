#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import platform

def getResolution():
    try:
        # for Python 3
        import tkinter as tk
    except ImportError:
        # for Python 2
        import Tkinter as tk
        
    if platform.system() != "Windows":

        """
        Workaround to get the size of the current screen in a multi-screen setup.

        Returns:
            geometry (str): 
                [width]x[height]+[left]+[top]
        """
        root = tk.Tk()
        root.update_idletasks()
        root.attributes('-fullscreen', True)
        root.state('iconic')
        #geometry = root.winfo_geometry().width()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.destroy()
        return [width,height]
        
    else:
        from ctypes.windll.user32 import GetSystemMetrics
        width, height = GetSystemMetrics(0), GetSystemMetrics(1)
        return [width,height]
