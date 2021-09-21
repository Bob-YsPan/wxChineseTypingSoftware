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
from string_compare import string_compare_line

class Mainframe(WX_Window.MainForm):

    # Varibles
    remain_time = 600
    start_time = 600
    start = False

    # Init form
    def __init__(self, parent):
        WX_Window.MainForm.__init__(self, parent)
        # 給輸入框設定文字顏色
        default_type = wx.richtext.RichTextAttr()
        default_type.SetBackgroundColour(wx.Colour( 18, 18, 18 ))
        default_type.SetTextColour(wx.Colour( 238, 238, 238 ))
        default_type.SetFontSize(18)
        self.userRich.AppendText('init...')
        self.userRich.SetDefaultStyle(default_type)
        self.userRich.Clear()

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
                          '大部分Linux環境下請使用UTF-8編碼\nWindows下請使用Big-5或記事本ANSI編碼', '解碼失敗', wx.OK | wx.ICON_ERROR)
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
        self.start_time = self.remain_time
        self.min_Text.LabelText = str(int(self.remain_time / 60)).zfill(2)
        self.sec_Text.LabelText = str(self.remain_time % 60).zfill(2)

    # Check typing function (Need Help)
    def check_typing(self, times_up):
        # 產稱題目跟答案的二維空列表
        user_input = []
        answer_art = []
        total_incorrect = 0
        total_need_type = 0
        total_cleartype = 0

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
            answer_art.append(current_line)

            # 取出作答的一行字
            current_line = self.userRich.GetLineText(line_no)
            # 不能是空行，除非是手動交卷
            if not((current_line == '') and times_up):
                user_input.append(current_line)
        print(answer_art)
        print(user_input)

        # 逐行批閱
        # return：
        # 0 answer_show = 顯示在richbox的答案行
        # 1 userin_show = 顯示在richbox的輸入行
        # 2 mark_index = 需要標顏色的index
        # 3 err_point = 總扣擊數
        # 4 correct_type = 正確字數
        # 5 line_need_text = 須輸入字數

        # 定義一下type，丟一點測試文字再刪掉
        default_type = wx.richtext.RichTextAttr()
        default_type.SetBackgroundColour(wx.Colour( 18, 18, 18 ))
        default_type.SetTextColour(wx.Colour( 238, 238, 238 ))
        default_type.SetFontSize(18)
        result_form.ResultRich.AppendText('init...')
        result_form.ResultRich.SetDefaultStyle(default_type)
        # 幫結果框套下顏色
        result_form.ResultRich.Clear()


        for line_no in range(max_line):
            res = []
            # 使用者來不及打完就不要檢查到最後。
            if (line_no == max_line - 1) and (times_up):
                print('times up, dont check to end.')
                res = string_compare_line(answer_art[line_no], user_input[line_no], True)
            else:
                res = string_compare_line(answer_art[line_no], user_input[line_no], False)
            append_text = res[0] + '\n'
            append_text = append_text + res[1]
            result_form.ResultRich.AppendText(append_text)
            # 設定文字大小
            default_type.SetFontSize(18)
            # 將格式套正確(以免加後面套新格式被蓋掉)
            result_form.ResultRich.MoveToLineEnd()
            cursor_pos = result_form.ResultRich.GetCaretPosition()
            result_form.ResultRich.SetStyle(cursor_pos - len(append_text) + 1, cursor_pos + 1, default_type)
            # 移動游標到行首準備上色
            result_form.ResultRich.MoveToLineStart()
            cursor_pos = result_form.ResultRich.GetCaretPosition()
            print('cursor pos = ' + str(cursor_pos))
            # Copy預設值，設定字體格式
            current_type = wx.richtext.RichTextAttr()
            current_type.Copy(default_type)
            current_type.SetBackgroundColour(wx.RED)
            current_type.SetTextColour(wx.WHITE)
            for pos in range(len(res[2])):
                if res[2][pos]:
                    result_form.ResultRich.SetStyle(cursor_pos + pos + 1, cursor_pos + pos + 2, current_type)
            # 批閱結果顯示
            append_text = '\n ^^ 第 ' + str(line_no + 1) + ' 行批閱結果 ^^ \n'
            append_text = append_text + '淨字數: 正確字數(' + str(res[4]) + ')'
            remain_correct = res[4] - (res[3] * 0.5)
            # 淨字數不小於0
            if remain_correct < 0:
                remain_correct = 0
            total_cleartype = total_cleartype + remain_correct  # 淨字數統計
            append_text = append_text + ' - (錯誤次數(' + str(res[3]) + ') * 0.5) => ' + str(remain_correct)
            append_text = append_text + ' | 應輸入字數: ' + str(res[5])
            total_incorrect = total_incorrect + res[3]  # 總錯誤數
            total_need_type = total_need_type + res[5]  # 應輸入字數
            result_form.ResultRich.AppendText(append_text)
            # 套用小字一點的格式
            current_type = wx.richtext.RichTextAttr()
            current_type.Copy(default_type)
            current_type.SetFontSize(12)
            current_type.SetBackgroundColour(wx.Colour( 18, 18, 18 ))
            result_form.ResultRich.MoveToLineEnd()
            cursor_pos = result_form.ResultRich.GetCaretPosition()
            result_form.ResultRich.SetStyle(cursor_pos - len(append_text) + 1, cursor_pos + 1, current_type)
            result_form.ResultRich.AppendText('\n\n')
        # 結果行顯示
        append_text = '測驗結果: \n'
        use_time = self.start_time - self.remain_time
        append_text = append_text + '用時: ' + str(use_time) + ' 秒\n'
        append_text = append_text + '平均字數: ' + str(round(total_cleartype / (use_time / 60), 2)) + ' 字/分鐘\n'
        err_rate = round((total_incorrect / total_need_type) * 100 ,2)
        append_text = append_text + '錯誤率: ' + str(err_rate) + ' %'
        if err_rate > 10.0:
            append_text = append_text + '(無效)'
        result_form.ResultRich.AppendText(append_text)
        # 套用結果字體
        result_form.ResultRich.MoveToLineEnd()
        cursor_pos = result_form.ResultRich.GetCaretPosition()
        current_type = wx.richtext.RichTextAttr()
        current_type.Copy(default_type)
        current_type.SetFontSize(14)
        current_type.SetFontWeight(wx.FONTWEIGHT_BOLD)
        result_form.ResultRich.SetStyle(cursor_pos - len(append_text) + 1, cursor_pos + 1, current_type)

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
