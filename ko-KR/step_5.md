## 거북이 경주

이제 재미있게 놀아봅시다. 경주용 거북이를 추가해 봅시다! 거북이가 매번 똑같은 거리만큼 움직인다면 정말 지루할 것입니다. 그래서 거북이를 매 턴마다 랜덤한 거리만큼 움직이게 할 것입니다. 우승자는 100바퀴 안에 가장 멀리 이동한 거북입니다.

+ `forward(20)` 같은 명령을 사용할 때 당신은 하나의 거북이를 사용합니다. 하지만 여러분은 더 많은 거북이를 만들 수 있습니다. 스크립트 끝에 다음 코드를 추가하세요. (반드시 들여쓰기가 되어있지 않았는지 확인하세요).
    
    ![스크린샷](images/race-red.png)
    
    첫번째 거북이는 'ada'라고 부르도록 하겠습니다. 다음 줄은 거북이의 모양과 색깔을 결정합니다. 정말 거북이같이 보이네요!

+ 거북이를 시작점으로 보내봅시다!
    
    ![스크린샷](images/race-start.png)

+ 그리고 랜덤하게 거북이를 움직이는 레이스를 만들어 봅시다. 이를 구현하기 위해서는 파이썬 `random` 라이브러리의 `randint`가 필요합니다. 스크립트 상단에 `import`을 추가해주세요.
    
    ![스크린샷](images/race-randint.png)

+ `randint` 함수는 지정된 값 내에서 랜덤한 정수를 반환합니다. 거북이는 1, 2, 3, 4 혹은 5스텝을 랜덤하게 이동하게 됩니다.
    
    ![스크린샷](images/race-random.png)

+ 한 거북이만 가지고는 경기를 하기 어렵겠죠? 다른 거북이도 추가해 봅시다!
    
    ![스크린샷](images/race-blue.png)
    
    파란 거북이를 움직이는 코드는, 붉은 거북이를 움직였을 때와 **같게** for</0>문을 사용하면 됩니다.</p></li>
</ul>