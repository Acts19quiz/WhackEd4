#!/usr/bin/env python
#coding=utf8

from whacked4 import config
from whacked4.ui import mainwindow
import argparse
import os.path
import sys
import traceback
import wx


if __name__ == '__main__':
    
    # Parse common commandline arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument('-debug', action='store_true', help='Enable debug mode.')
    args = parser.parse_known_args()[0]
    
    # Enable debugging mode.
    if args.debug:
        config.DEBUG = True
        print 'Debug mode enabled. Only writing exceptions to stdout.'
 
    # Redirect all console output to a single log file.
    if config.DEBUG == False:
        log_file = open(config.LOG_PATH, 'a')
        sys.stderr = log_file
        sys.stdout = log_file
    
    # Start application.
    config.settings.load()
    app = wx.App(redirect=False)
    
    # Set monospaced font.
    font_size = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT).GetPointSize()
    config.FONT_MONOSPACED = wx.Font(
        font_size,
        wx.FONTFAMILY_DEFAULT,
        wx.FONTSTYLE_NORMAL,
        wx.FONTWEIGHT_NORMAL,
        faceName=config.FONT_MONOSPACED_NAME
    )
    
    try:
        main_window = mainwindow.MainWindow(None, args)
        app.MainLoop()
    
    # Catch all exceptions and write them to stdout, and display if needed.
    except Exception as e:
        traceback.print_exc()
        
        if config.DEBUG == False:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb = traceback.extract_tb(exc_traceback)
            logpath = config.LOG_PATH
            
            # Concatenate a debug trace message.
            trace = ''
            for line in tb:
                trace += '{}: {}: line {}: {}\n'.format(os.path.basename(line[0]), line[2], line[1], line[3])
            
            wx.MessageBox(message='A fatal exception occurred.\n\n{}\n{}\nThis error message can also be found in {}'.format(e, trace, logpath),
                caption='Fatal exception',
                style=wx.OK | wx.ICON_ERROR,
                parent=None)