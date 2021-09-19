# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class MainForm
###########################################################################

class MainForm ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"中文打字練習程式", pos = wx.DefaultPosition, size = wx.Size( 1024,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 1024,600 ), wx.DefaultSize )
		self.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.SetBackgroundColour( wx.Colour( 239, 239, 239 ) )

		mainSizer = wx.BoxSizer( wx.VERTICAL )

		titleSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.artPicker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"選擇文章...", u"*.txt", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.artPicker.SetToolTip( u"按我瀏覽檔案" )

		titleSizer.Add( self.artPicker, 1, wx.ALL, 5 )

		self.controlbtn = wx.Button( self, wx.ID_ANY, u"開始測驗", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.controlbtn.Enable( False )
		self.controlbtn.SetToolTip( u"按下開始測驗" )

		titleSizer.Add( self.controlbtn, 0, wx.ALL, 5 )


		titleSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.min_Text = wx.StaticText( self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.min_Text.Wrap( -1 )

		titleSizer.Add( self.min_Text, 0, wx.ALL, 5 )

		self.timeDot_Text = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.timeDot_Text.Wrap( -1 )

		titleSizer.Add( self.timeDot_Text, 0, wx.ALL, 5 )

		self.sec_Text = wx.StaticText( self, wx.ID_ANY, u"00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sec_Text.Wrap( -1 )

		titleSizer.Add( self.sec_Text, 0, wx.ALL, 5 )


		titleSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.time_staticText = wx.StaticText( self, wx.ID_ANY, u"計時", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.time_staticText.Wrap( -1 )

		titleSizer.Add( self.time_staticText, 0, wx.ALL, 5 )

		timechoiceChoices = [ u"1分鐘", u"3分鐘", u"5分鐘", u"10分鐘", u"20分鐘", u"30分鐘" ]
		self.timechoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, timechoiceChoices, 0 )
		self.timechoice.SetSelection( 3 )
		self.timechoice.SetToolTip( u"計時器設定" )

		titleSizer.Add( self.timechoice, 0, wx.ALL, 5 )


		mainSizer.Add( titleSizer, 0, wx.EXPAND, 5 )

		artListChoices = []
		self.artList = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, artListChoices, 0 )
		self.artList.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Noto Sans CJK TC Regular" ) )
		self.artList.SetToolTip( u"題目" )

		mainSizer.Add( self.artList, 1, wx.ALL|wx.EXPAND, 5 )

		self.userRich = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.userRich.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Noto Sans CJK TC Regular" ) )
		self.userRich.Enable( False )
		self.userRich.SetToolTip( u"輸入區" )

		mainSizer.Add( self.userRich, 1, wx.EXPAND |wx.ALL, 5 )

		self.End_Info = wx.StaticText( self, wx.ID_ANY, u"按下按鈕開始計時。段落開頭使用全形空格。繳卷請於最後一行完成時按下Enter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.End_Info.Wrap( -1 )

		mainSizer.Add( self.End_Info, 0, wx.ALL, 5 )


		self.SetSizer( mainSizer )
		self.Layout()
		self.counter_Timer = wx.Timer()
		self.counter_Timer.SetOwner( self, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.artPicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.artPickerOnFileChanged )
		self.controlbtn.Bind( wx.EVT_BUTTON, self.controlbtnOnButtonClick )
		self.timechoice.Bind( wx.EVT_CHOICE, self.timechoiceOnChoice )
		self.userRich.Bind( wx.EVT_KEY_UP, self.userRichOnKeyUp )
		self.userRich.Bind( wx.EVT_LEFT_UP, self.userRichOnKeyUp )
		self.Bind( wx.EVT_TIMER, self.counter_TimerOnTimer, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def artPickerOnFileChanged( self, event ):
		event.Skip()

	def controlbtnOnButtonClick( self, event ):
		event.Skip()

	def timechoiceOnChoice( self, event ):
		event.Skip()

	def userRichOnKeyUp( self, event ):
		event.Skip()


	def counter_TimerOnTimer( self, event ):
		event.Skip()


###########################################################################
## Class Result_Win
###########################################################################

class Result_Win ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"測試結果", pos = wx.DefaultPosition, size = wx.Size( 1024,600 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.Size( 1024,600 ), wx.DefaultSize )

		Sizer = wx.BoxSizer( wx.VERTICAL )

		self.ResultRich = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.ResultRich.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Noto Sans CJK TC Regular" ) )

		Sizer.Add( self.ResultRich, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( Sizer )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


