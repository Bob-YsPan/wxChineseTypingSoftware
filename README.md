# wxPython Chinese Typing Software  
類似台灣TQC中打計算標準的中打軟體，讀取文字檔當作題目並計時打字與算分數。  
Chinese typing software that it's standard close to TQC certification to be used in Taiwan, can load custom text files as article, countdown, and calculate the score.  
## Why I want to build this project?  
以前我碰觸過TQC的打字標準或軟體，覺得這種使用文章來測試中打速度的軟體更貼近生活上使用中文打字的情境，前鎮子練習中打時也特別去網路上找有人流出帶有舊題庫的打字軟體。  
練習途中開始萌生了追求更開放且沒有版權問題的打字軟體的想法，後來也因此發現了[typing.tw](typing.tw)，並開始有了自己寫一套打字軟體的想法。  
A long time ago, I found the TQC typing software that uses articles to practice Chinese typing ability.  It seems like the best solution to improve Chinese typing skills in life.  
When I practice Chinese typing a few years ago, I tried to find TQC typing software that was not the latest version on the network, and begin to think about where to find software that open source and had no copyright. and then I found [typing.tw](typing.tw), and want to code one by myself.  
## Which functions I already done?  
* Basic GUI
* Load article, Countdown, and Type
* Result screen layout
* Check article function(To check and calculate score)(Finished, testing.)  
**Check function tried to match rules at "TQC 規範.txt" in the repo(Refer to [TQC certificate Website](https://www.tqc.org.tw/TQCNet/CertificateDetail.aspx?CODE=r1y127Koepg=)):**
## Coding requirements  
* Python 3
* wxPython  
```pip install wxpython```
* wxFormBuilder(To modify GUI)
## How to debug project(And some files discription)
* Run ```python ChineseTyping.py``` to run program and debug
    * Or can use ```Launcher.sh```(For Linux or macOS), ```Launcher.cmd```(For Windows) to run app.
* ```Python_windows_RICH.fbp``` is a layout files build using wxFormBuilder  
Can use this tool to modify program's Layout, and it will generate file override ```WX_Window.py```
* ```文章[Number]_[Encoding].txt```are example article files. Windows Traditional Chinese version use BIG5 encoding, Unix like(macOS、 Linux) use UTF8 encoding
* ```TQC規範.txt``` is a rules to check user typing(Copied from TQC website)
* ```string_compare.py``` used to check user key in answers line by line, uses Python ndiff function.

## Articles Source(文章來源):

### 文章已經移動到[另外一個Repo](https://github.com/Bob-YsPan/ChineseTypingArticles)維護！

* 文章1.txt > 《將進酒》 李白 | [維基文庫](https://zh.wikisource.org/wiki/%E5%B0%87%E9%80%B2%E9%85%92_(%E6%9D%8E%E7%99%BD))
* 文章2.txt > 《泰國、越南到臺灣，跨越與塑造邊界的茶》 寒波 (節錄) | [科技大觀園](https://scitechvista.nat.gov.tw/Article/C000003/detail?ID=be45b67b-ae53-4626-966e-e2e8a97475ef)
* 文章3.txt > 《我的彼得》 徐志摩 | [維基文庫](https://zh.wikisource.org/wiki/%E6%88%91%E7%9A%84%E5%BD%BC%E5%BE%97)  
* 文章4.txt > 《天災使我們更加團結一心》 陸子鈞 | [科技大觀園](https://scitechvista.nat.gov.tw/Article/C000003/detail?ID=8358bbd7-43c8-4462-ad9e-5611981a3cc4)
* 文章5.txt > 《免於恐懼地吃–食物過敏的治療》 徐伊亭 | [科技大觀園](https://scitechvista.nat.gov.tw/Article/C000003/detail?ID=d2fd0afa-5d47-43d3-acfc-2a89036685de)  

**如文章有侵權問題，麻煩跟我聯絡一下，我會盡快徹下文章，感謝～**  
## Articles Make Guide(文章製作指引):
* 段落開頭需要2全形字元(2 full-width spaces at paragraph start.)
* 所有字採用全型字符(All charters use full-width charters.)
* 每行32個全型字符為限(32 full-width charters max for each line.)  
## Portable Version
I tried to make a portable version under Windows using Pyinstaller, which contains Python 3.4 version built on Windows XP and the Newer python version built on Windows 10. Files can be found in the latest release files.  
## Screenshots
Xfce manjaro dark theme:  
* **Attention!** Maybe some bug under the wxPython in the Gtk, the line of the article you are typing may not be highlighted correctly.  
* **注意！** 可能是一些wxPython的Bug，文章正在打的那行可能不會正常被標(上色)出來  
  
![Screenshot1](/SCR1.png)  
  
Windows 10 21H2:
![Screenshot3](/SCR3.png)  
  
macOS Mojave dark theme:  
* **Attention!** macOS may cause some problems like input window not shown  
* **注意！** 在 macOS 跑的時候可能會遇到輸入框不會顯示等問題！
  
![Screenshot4](/SCR4.png)  
  
**Bonus!** Windows XP with older python(3.4):  
![Screenshot5](/SCR5.png)  
  
