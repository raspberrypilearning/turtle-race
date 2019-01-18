## 競争するトラック

これから、かめが競争するゲームを作ります。まず最初にトラックをつくっていこう。

+ Trinket（トリンケット）:　<a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.　ここを開いてみよう。

+ 以下のコードを加えて線を引いてみよう。
    
    ![スクリーンショット](images/race-forward.png)

+ 今度はタートルを使って、レースのトラックを作ってみよう。
    
    タートルに`write(ライト)`という機能で画面に文字を描こう。
    
    試してみる：
    
    ![スクリーンショット](images/race-markings1.png)

+ 下のようにゴールまでの数字を入れてみよう。
    
    ![スクリーンショット](images/race-markings2.png)

+ 今書いたコードに繰り返していることはあるかな？数字だけを変えてみよう。
    
    Pythonにはもっといい方法があります。
    
    `for`文というものを使って書き直してみよう：
    
    ![スクリーンショット](images/race-for.png)

+ えーっと、数字が4までいきました。Pythonでは`range(5)`とすると0から4までの5個の数字を返します。5まで使いたいときは`range(6)`とすれば使えるよ：
    
    ![スクリーンショット](images/race-range.png)

+ さて、いくつかのトラックを描いてみよう。かめは(0,0)というスクリーンの真ん中からスタートするよ。
    
    かめを左上に動かしてみよう。
    
    ![スクリーンショット](images/race-goto.png)

+ →矢印の先だけ最初に描いてみよう。
    
    ![スクリーンショット](images/race-penup.png)

+ 水平な線の代わりに、垂直な線をトラックとして描いてみよう。
    
    ![スクリーンショット](images/race-lines.png)
    
    `right(90) `はタートルを時計回りに90度動かしてくれる。線を描く前に`forward(10)`をすることで、数字と線の始まる位置をずらしてくれる。これがもしなかったら、矢印の先と数字が被ってしまって見えなくなってしまう。 線が描けたら、ペンをあげて`backward(160)`をして線を描き始めた少し上まで戻ってみよう。

+ 以下のようにコードを加えると、見た目が綺麗に見えるよ
    
    ![スクリーンショット](images/race-center.png)

+ そして、スピードアップを加えるとタートルが線を早く描いてくれるよ。
    
    ![スクリーンショット](images/race-speed.png)