#!/usr/bin/env python
#coding=utf8

from whacked4.ui import windows

import whacked4.config as config

import wx


class StringDialog(windows.StringDialogBase):
    """
    This dialog displays a string to be edited by the user.
    """

    def __init__(self, parent):
        windows.StringDialogBase.__init__(self, parent)

        self.SetEscapeId(windows.STRING_CANCEL)

        self.Original.SetFont(config.FONT_MONOSPACED)
        self.New.SetFont(config.FONT_MONOSPACED)

        self.engine_string = None
        self.old_string = None
        self.new_string = None
        self.extended = False
        self.max_length = 0

    def set_state(self, engine_string, old_string, extended, name, cheat=False):
        """
        Sets a new state for this string dialog.
        """

        self.engine_string = engine_string
        self.old_string = old_string
        self.extended = extended

        # Set displayed text.
        self.Original.ChangeValue(engine_string)
        self.New.ChangeValue(old_string)

        if cheat:
            self.SetLabel('Cheat - {}'.format(name))
            self.New.SetWindowStyleFlag(wx.TE_DONTWRAP)
        else:
            self.SetLabel('String - {}'.format(name))
            self.New.SetWindowStyleFlag(wx.TE_MULTILINE | wx.TE_DONTWRAP | wx.TE_PROCESS_ENTER | wx.TE_PROCESS_TAB)

        if extended:
            self.CharsLeft.Hide()
        else:
            self.CharsLeft.Show()

        self.update_length()

        self.New.SelectAll()
        self.New.SetFocus()

    def text_enter(self, event):
        """
        Called when text is entered.
        """

        self.update_length()
        event.Skip()

    def update_length(self):
        """
        Updates the amount of characters left.
        """

        if self.extended:
            return

        text = self.New.GetValue()

        self.CharsLeft.SetLabel('Text {} {}'.format(len(self.engine_string), len(text)))# Acts 19 quiz

    def text_keydown(self, event):
        """
        Process key down events.

        Handles the fact that a text control's MaxLength setting does not count newlines.
        """

        event.Skip()

    def activate(self, event):
        self.New.SetFocus()

    def ok(self, event):
        self.new_string = self.New.GetValue()
        self.EndModal(0)

    def cancel(self, event):
        self.new_string = None
        self.EndModal(0)
