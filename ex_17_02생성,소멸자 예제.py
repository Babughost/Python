# 생성자 예제

# class USB :
#     def __init__(self, capacity) :
#         self.capacity = capacity

#     def info(self) :
#         print(f'{self.capacity} GB USB')

# usb = USB(64)
# usb.info()



# 소멸자 예제

class Service :
    def __init__(self, service) :
        self.service = service
        print(f'{self.service} 가 시작 되었습니다.')

    def __del__(self):
        print(f'{self.service} 가 종료 되었습니다.')

s = Service('길 안내')
# del s     # 출력 후 메모리 소멸로 인해 del s 작성을 안 해도 종료 메시지 나옴





