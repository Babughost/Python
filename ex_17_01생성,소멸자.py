# 생성자와 소멸자
# 1. 생성자

class Candy :
    def set_info(self, shape, color) :
        self.shape = shape
        self.color = color

satang = Candy()
satang.set_info('circle', 'brown')

# satang = Candy() 코드가 실행되면서 satang 인스턴스(객체)가 생성되는데 이때는 인스턴스에 저장된
# 모양과 색상 정보가 없음
# 인스텐스 생성후에 set_info() 메소드를 호출해서 모양과 색상 정보를 가짐
# 정리하면
# 1) 값이 없는 인스턴스 생성
# 2) 값을 저장할 수 있는 메소드를 호출

# 값을 가진 인스턴스를 생성하기 위해 생성자를 이용
# 생성자는 인스턴스를 생성할때 자동으로 호출되는 특별한 메소드
# 모든 클래스는 __init__() 이라는 이름을 가진 생성자를 가지고 있음
# __init__() 메소드(생성자)는 인스턴스가 생성 될 떄 자동으로 호출되기 때문에 인스턴스 변수의 초가화 용도로 사용


class Candy :
    def __init__(self, shape, color) :
        self.shape  = shape
        self.color = color

satang = Candy('circle','brown')


# 2. 소멸자
# 인스턴스가 생성될 때 자동으로 생성되는 생성자와 마찬가지로
# 인스턴스가 소멸될 때 자동으로 호출되는 메서드
# 소멸자는 __del__()

class Sample :
    def __del__(self) :
        print('인스턴스가 소멸됩니다.')


sample = Sample()
del sample  # 인스턴스가 소멸됩니다.