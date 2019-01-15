## Đường đua

Bạn sẽ tạo ra một trò chơi với rùa đua. Đầu tiên, họ sẽ cần một đường đua.

+ Mở mẫu Python Trinket trống: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Thêm đoạn mã sau để vẽ một đường bằng cách sử dụng 'rùa':
    
    ![ảnh chụp màn hình](images/race-forward.png)

+ Bây giờ chúng ta hãy sử dụng con rùa để vẽ một số dấu vết cho cuộc đua.
    
    Hàm rùa `viết` ghi văn bản vào màn hình.
    
    Thử nó:
    
    ![ảnh chụp màn hình](images/race-markings1.png)

+ Bây giờ bạn cần phải điền vào các số ở giữa để tạo các dấu:
    
    ![ảnh chụp màn hình](images/race-markings2.png)

+ Bạn có nhận thấy rằng mã của bạn rất lặp lại không? Điều duy nhất thay đổi là số để viết.
    
    Có một cách tốt hơn để làm điều này trong Python. Bạn có thể sử dụng vòng lặp `cho`.
    
    Cập nhật mã của bạn để sử dụng vòng lặp `cho`:
    
    ![ảnh chụp màn hình](images/race-for.png)

+ Hmm, mà chỉ in số lên đến 4. Trong phạm vi Python `(5)` trả về năm số, từ 0 lên đến 4. Để có được nó cũng trả về 5 bạn sẽ cần phải sử dụng `phạm vi (6)`:
    
    ![ảnh chụp màn hình](images/race-range.png)

+ Bây giờ chúng ta có thể vẽ một số dấu rãnh ghi. Con rùa bắt đầu tại tọa độ (0,0) ở giữa màn hình.
    
    Di chuyển con rùa lên trên cùng bên trái để thay thế:
    
    ![ảnh chụp màn hình](images/race-goto.png)

+ Ah, bạn sẽ muốn nhấc bút lên trước!
    
    ![ảnh chụp màn hình](images/race-penup.png)

+ Thay vì vẽ một đường theo chiều ngang, hãy vẽ các đường thẳng đứng để tạo bản nhạc:
    
    ![ảnh chụp màn hình](images/race-lines.png)
    
    `right (90)` làm cho con rùa rẽ phải 90 độ (góc phải.) Di chuyển `về phía trước (10)` trước khi đặt bút xuống để lại một khoảng cách nhỏ giữa số và đầu dòng. Sau khi vẽ đường bạn nhấc bút lên và đi `lùi (160)` chiều dài của đường kẻ cộng với khoảng trống.

+ Nó trông neater nếu bạn trung tâm các con số:
    
    ![ảnh chụp màn hình](images/race-center.png)

+ Và bạn có thể tăng tốc độ cho rùa để nó nhanh hơn:
    
    ![ảnh chụp màn hình](images/race-speed.png)