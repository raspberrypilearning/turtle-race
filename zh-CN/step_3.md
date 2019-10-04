## 跑道

您将编写一个乌龟赛跑的游戏。首先，此游戏需要建立一个跑道。

+ 单击链接<a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>，打开一个空白的Trinket Python模版。

+ 添加以下代码以使用'turtle'模块绘制一条线：
    
    ![截图](images/race-forward.png)

+ 现在让我们使用turtle模块来为赛跑绘制跑道标记。
    
    Turtle模块中的`write`函数能在屏幕上绘制文本。
    
    尝试一下：
    
    ![截图](images/race-markings1.png)

+ 现在你需要在线条两端之间填写一些数字来创建标记：
    
    ![截图](images/race-markings2.png)

+ 你注意到你的代码是非常重复的吗？它们唯一不同的地方是输入的数字。
    
    在Python中有一种更好的方法来写这样重复的代码。您可以使用`for`循环。
    
    使用`for`循环来更新你的代码：
    
    ![截图](images/race-for.png)

+ 嗯，这只打印了从0到4之间的数字。Python中的`range(5)`函数将返回从0到4的五个数字。要让它返回数字5，您则需要使用`range(6)`：
    
    ![截图](images/race-range.png)

+ 现在我们可以绘制一些跑道的标记了。turtle模块将从屏幕中央的坐标 (0,0) 开始绘制。
    
    现在要将画笔移动到屏幕的左上方：
    
    ![截图](images/race-goto.png)

+ 啊，你要先把画笔抬起来！
    
    ![截图](images/race-penup.png)

+ 让我们绘制一些垂直线来创建跑道, 而不是水平线：
    
    ![截图](images/race-lines.png)
    
    `right(90)`函数使画笔向右转90度。将画笔放下之前，使用`forward(10)`函数前进10步将使线条的起点和数字之间保留一个小的空隙。 线条画好后，将画笔抬起并使用`backward(160)`函数向后移动160步，即线条和空隙的总长。

+ 居中数字，将使界面看起来更整洁：
    
    ![截图](images/race-center.png)

+ 你还可以加快画笔的速度，使它画得更快：
    
    ![截图](images/race-speed.png)