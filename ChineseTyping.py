# Chinese typing program
# Powered by wxWidgets, Python
# Form init code: http://tw511.com/3/48/1618.html
# Form made by wxBuilder
# Program writen by Bob Pan 2020.07 - 2020.08
# Coding on Arch Linux, Gnome Desktop Environment & Windows 10 v2004
# 2021.07 - 2021.09 continue finish
# On Manjaro Linux, Xfce Desktop Environment & Windows 10 21H1

import WX_Window
import wx
import wx.richtext


class Mainframe(WX_Window.MainForm):

    # Varibles
    remain_time = 600
    start = False

    # Init form
    def __init__(self, parent):
        WX_Window.MainForm.__init__(self, parent)

    # After pick file
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

    # Control buttom(開始測驗) function
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

    # Timer Tick(Period: 1s)
    def counter_TimerOnTimer( self, event ):
        if self.remain_time == 0:
            print('Times Up')
            self.counter_Timer.Stop()
            wx.MessageBox('時間到!', '', wx.OK | wx.ICON_INFORMATION)
            self.check_typing(True)
        else:
            self.remain_time = self.remain_time - 1
            # Update time shown
            self.min_Text.LabelText = str(int(self.remain_time / 60)).zfill(2)
            self.sec_Text.LabelText = str(self.remain_time % 60).zfill(2)

    # Get cursor line number
    def line_no(self, pos):
        pos = pos + 2
        for line_no in range(0, self.userRich.GetNumberOfLines()):
            pos = pos - (self.userRich.GetLineLength(line_no) + 1)
            if pos <= 0:
                return line_no

    # When finish last line and triggered keyup, ask user to send answer earlier.
    def userRichOnKeyUp( self, event ):
        line_no = self.line_no(self.userRich.GetCaretPosition())
        if line_no + 1 > self.artList.GetCount():
            self.counter_Timer.Stop()
            if wx.MessageBox('確定完成？', '', wx.YES_NO | wx.ICON_INFORMATION) == wx.YES:
                print('finished.')
                self.check_typing(False)
            else:
                self.counter_Timer.Start(1000)
        else:
            self.artList.SetSelection(line_no)

    # Choose times
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

    # Check typing function (Need Help)
    def check_typing(self, times_up):
        # 產稱題目跟答案的二維空列表
        user_input = []
        answer_art = []

        # 實例化結果視窗(以便改寫RichText內容)以及結果變數
        result_form = ResultForm(None)
        result_form.ResultRich.Clear()
        # 顯示進入檢查狀態(可能會跑比較久)
        self.End_Info.LabelText = '批閱中，請稍後...'
        # 時間到的話，看使用者輸入了幾行，否則檢查全部。
        if times_up:
            max_line = self.userRich.GetNumberOfLines()
        else:
            max_line = self.artList.GetCount()
        # 將文字儲存成陣列
        for line_no in range(0, max_line):
            # 取出文字
            print('正在取出第' + str(line_no), end='行\n')
            # 取出答案的一行字
            current_line = self.artList.GetString(line_no)
            # print(current_line)
            # 命一個該行的空陣列(陣列每一項都是一個字)
            append_line_list = []
            # 將每一行的字取出存入陣列
            for text in current_line:
                print(text, end='')
                append_line_list.append(text)
            answer_art.append(append_line_list)
            print(answer_art[line_no], end=' length = ')
            print(len(answer_art[line_no]))

            # 取出作答的一行字
            current_line = self.userRich.GetLineText(line_no)
            # print(current_line)
            # 清空該行的空陣列(陣列每一項都是一個字)
            append_line_list = []
            # 將每一行的字取出存入陣列
            for text in current_line:
                print(text, end='')
                append_line_list.append(text)
            user_input.append(append_line_list)
            print(user_input[line_no])

        # ---Need help here---

        # 結果視窗的顯示方式
        # result_form.ResultRich.AppendText(text)
        # 將結果RichTextCtrl設定成不可編輯狀態
        result_form.ResultRich.SetEditable(False)
        # 顯示結果視窗，用ShowModal以使下層視窗無法被互動
        result_form.ShowModal()
        result_form.Destroy()
        # 輸入區回到初始狀態
        self.End_Info.LabelText = '按下按鈕開始計時。繳卷請於最後一行完成時按下Enter'
        self.counter_Timer.Stop()
        self.timechoiceOnChoice(self)
        self.userRich.Clear()
        self.artPicker.Enabled = True
        self.timechoice.Enabled = True
        self.controlbtn.LabelText = '開始測驗'
        self.controlbtn.ToolTip = '按下開始測驗'
        self.userRich.Enabled = False
        self.start = False


# Result form init(結果視窗)
class ResultForm (WX_Window.Result_Win):

    def __init__(self, parent):
        WX_Window.Result_Win.__init__(self, parent)


app = wx.App()
frame = Mainframe(None)
frame.Show(True)
# start the applications
app.MainLoop()
