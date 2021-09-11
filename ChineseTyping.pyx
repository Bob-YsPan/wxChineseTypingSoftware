# Chinese typing program
# Powered by wxWidgets, Python
# Form init code: http://tw511.com/3/48/1618.html
# Form made by wxBuilder
# Program writen by Bob Pan 2020.07 - 2020.08
# Coding on Arch Linux, Gnome Desktop Environment

import WX_Window
import wx
import wx.richtext


class Mainframe(WX_Window.MainForm):

    # Varibles
    remain_time = 600
    start = False

    def __init__(self, parent):
        WX_Window.MainForm.__init__(self, parent)

    def artPickerOnFileChanged( self, event ):
        err = False
        try:
            art_file = open(self.artPicker.GetPath(), mode='r')
            self.artList.Clear()
            for art_line in art_file:
                self.artList.Append(art_line.replace('\n', ''))
        except UnicodeDecodeError:
            wx.MessageBox('請使用另一種編碼格式儲存文字檔\n'
                          '大部分Linux環境下請使用UTF-8編碼\nWindows下請使用Big-5或ANSI編碼', '解碼失敗', wx.OK | wx.ICON_ERROR)
            err = True
        if not err:
            print('selected')
            self.controlbtn.Enabled = True

    def controlbtnOnButtonClick(self, event):
        if self.start:
            self.counter_Timer.Stop()
            self.timechoiceOnChoice(event)
            self.userRich.Clear()
            self.artPicker.Enabled = True
            self.timechoice.Enabled = True
            self.controlbtn.LabelText = '開始測驗'
            self.controlbtn.ToolTip = '按下開始測驗'
            self.userRich.Enabled = False
            self.start = False
        else:
            self.counter_Timer.Start(1000)
            self.artPicker.Enabled = False
            self.timechoice.Enabled = False
            self.controlbtn.LabelText = '停止測驗'
            self.controlbtn.ToolTip = '按下停止測驗並清除輸入'
            self.userRich.Enabled = True
            self.userRich.SetFocus()
            self.start = True

    def counter_TimerOnTimer( self, event ):
        if self.remain_time == 0:
            print('Times Up')
            self.counter_Timer.Stop()
            wx.MessageBox('時間到!', '', wx.OK | wx.ICON_INFORMATION)
        else:
            self.remain_time = self.remain_time - 1
            # Update time shown
            self.min_Text.LabelText = str(int(self.remain_time / 60)).zfill(2)
            self.sec_Text.LabelText = str(self.remain_time % 60).zfill(2)

    def line_no(self, pos):
        pos = pos + 2
        for line_no in range(0, self.userRich.GetNumberOfLines()):
            pos = pos - (self.userRich.GetLineLength(line_no) + 1)
            if pos <= 0:
                return line_no

    def userRichOnKeyUp( self, event ):
        line_no = self.line_no(self.userRich.GetCaretPosition())
        if line_no + 1 > self.artList.GetCount():
            self.counter_Timer.Stop()
            if wx.MessageBox('確定完成？', '', wx.YES_NO | wx.ICON_INFORMATION) == wx.YES:
                print('finished.')
            else:
                self.counter_Timer.Start(1000)
        else:
            self.artList.SetSelection(line_no)

    def timechoiceOnChoice( self, event ):
        if self.timechoice.Selection == 0:
            self.remain_time = 1 * 60
        elif self.timechoice.Selection == 1:
            self.remain_time = 3 * 60
        elif self.timechoice.Selection == 2:
            self.remain_time = 5 * 60
        elif self.timechoice.Selection == 3:
            self.remain_time = 10 * 60
        elif self.timechoice.Selection == 4:
            self.remain_time = 20 * 60
        elif self.timechoice.Selection == 5:
            self.remain_time = 30 * 60
        self.min_Text.LabelText = str(int(self.remain_time / 60)).zfill(2)
        self.sec_Text.LabelText = str(self.remain_time % 60).zfill(2)


app = wx.App()
frame = Mainframe(None)
frame.Show(True)
# start the applications
app.MainLoop()
