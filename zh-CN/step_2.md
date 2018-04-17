## 跑道

你将创建一个海龟赛跑的游戏。首先，它们需要一条跑道。



+ 打开空白 Python 模版 Trinket：<a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>。 

+ 添加以下代码来使用“turtle”（海龟）画一条线：

  ![screenshot](images/race-forward.png)
   
+ 现在让我们使用海龟来为比赛画一些跑道标记。 

  海龟 `write`（写入）函数将文本写入画面。 
  
  试试看：

  ![screenshot](images/race-markings1.png)
  
+ 现在你需要在其间填写数字来创建标记：

  ![screenshot](images/race-markings2.png)
  
+ 你是否注意到了你的代码有很多重复？唯一改变的内容就是写入的数字。

  在 Python 中有一个更好的方法来进行此操作。你可以使用 `for` 循环。 
  
  更新你的代码来使用 `for` 循环：
  
  ![screenshot](images/race-for.png)
   
+ 嗯，这样只会打印最大为 4 的数字。在 Python 中，​`range(5)` 将返回 5 个数字，从 0 到 4。为使其返回 5，你将需要使用 `range(6)`：

  ![screenshot](images/race-range.png)
   
+ 现在我们可以画一些跑道标记。海龟从画面中间的坐标 (0,0) 出发。 

  使海龟向左上方移动：
  
  ![screenshot](images/race-goto.png)

+ 啊，你首先需要提笔！

  ![screenshot](images/race-penup.png)
  
+ 让我们画一些垂直线而非水平线来创建跑道：

  ![screenshot](images/race-lines.png)
  
  `right(90)` 使海龟向右旋转 90 度（直角）。落笔之前向 `forward(10)` 移动，在数字和线的开头之间留出一小块间距。画完线后，你提笔并移动 `backward(160)`，即线条加上间距的长度。 
  
+ 如果你将数字居中，看起来会更简洁：

  ![screenshot](images/race-center.png)

+ 你可以将海龟加速，使其画得更快：

  ![screenshot](images/race-speed.png)




