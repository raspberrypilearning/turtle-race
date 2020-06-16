## 賽道

你將會建立一個烏龜賽跑的遊戲。首先，牠們將需要一條賽道。

+ 開啟空白的 Python 模板： <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>。

+ 添加以下程式碼，以便使用烏龜( turtle )來繪製線條： 
    
    ![螢幕截圖](images/race-forward.png)

+ 現在，讓我們使用烏龜來為比賽繪製一些賽道標記。
    
    烏龜的 `write` 函式可將文字寫到螢幕上。
    
    試試看！
    
    ![螢幕截圖](images/race-markings1.png)

+ 現在，你需要在各線段之間填上數字，以便建立標記：
    
    ![螢幕截圖](images/race-markings2.png)

+ 你是否已經注意得到，程式碼的重複性太高？唯一不同的是輸入的數字。
    
    在 Python 裏有更好的做法。你可以使用`for`迴圈。
    
    將你的程式碼修改成使用`for`迴圈：
    
    ![螢幕截圖](images/race-for.png)

+ 嗯，4 是最後被印出的數字。Python 中，` range(5)` 會傳回 5 個數字，從 0 到 4。要讓它傳回 5，則需要使用` range(6) ` ：
    
    ![螢幕截圖](images/race-range.png)

+ 現在我們可以繪製一些賽道標記。烏龜的起點位於螢幕中間的 (0,0) 坐標。
    
    將烏龜移動到左上方：
    
    ![螢幕截圖](images/race-goto.png)

+ 啊，你得先把畫筆舉起來！
    
    ![螢幕截圖](images/race-penup.png)

+ 現在繪製一些垂直線來作為賽道：
    
    ![螢幕截圖](images/race-lines.png)
    
    `right(90)`可使烏龜向右轉90度（直角）。放下筆之前，`forward(10)`可使烏龜向前移動10步，讓數字和線的開頭之間留下一個小空隙。 畫完線後，舉起筆並使用 `backward(160)` 讓烏龜向後退160步，也就是，線的長度加上空隙。

+ 如果讓數字置中，看起來會更整齊：
    
    ![螢幕截圖](images/race-center.png)

+ 你可以加快烏龜的速度，使其繪製得更快：
    
    ![螢幕截圖](images/race-speed.png)