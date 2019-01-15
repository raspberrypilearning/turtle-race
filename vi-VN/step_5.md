## Đua rùa

Bây giờ cho bit vui vẻ. Hãy thêm một số loài rùa đua. Nó sẽ thực sự nhàm chán nếu những con rùa đã làm điều tương tự mỗi lần để họ sẽ di chuyển một số ngẫu nhiên các bước mỗi lượt. Người chiến thắng là con rùa nhận được xa nhất trong 100 lượt.

+ Khi bạn sử dụng các lệnh như `tiến (20)` bạn đang sử dụng một con rùa duy nhất. Nhưng bạn có thể tạo thêm rùa. Thêm đoạn mã sau vào cuối tập lệnh của bạn (nhưng chắc chắn rằng nó không được thụt lề):
    
    ![ảnh chụp màn hình](images/race-red.png)
    
    Dòng đầu tiên tạo ra một con rùa gọi là 'ada'. Các dòng tiếp theo thiết lập màu sắc và hình dạng của con rùa. Bây giờ nó thực sự trông giống như một con rùa!

+ Hãy gửi con rùa đến vạch xuất phát:
    
    ![ảnh chụp màn hình](images/race-start.png)

+ Bây giờ bạn cần phải làm cho cuộc đua rùa bằng cách di chuyển một số ngẫu nhiên các bước tại một thời điểm. Bạn sẽ cần hàm `randint` từ thư viện Python `ngẫu nhiên`. Thêm dòng `nhập` này vào đầu tập lệnh của bạn:
    
    ![ảnh chụp màn hình](images/race-randint.png)

+ Hàm `randint` trả về một số nguyên ngẫu nhiên (toàn bộ số) giữa các giá trị được chọn. Con rùa sẽ di chuyển về phía trước 1, 2, 3, 4 hoặc 5 bước ở mỗi lượt.
    
    ![ảnh chụp màn hình](images/race-random.png)

+ Một con rùa không phải là một cuộc đua! Hãy thêm một số khác:
    
    ![ảnh chụp màn hình](images/race-blue.png)
    
    Lưu ý rằng mã để di chuyển con rùa màu xanh cần phải ở **cùng** `cho vòng lặp` làm mã để di chuyển con rùa màu đỏ để chúng từng di chuyển mỗi lượt.