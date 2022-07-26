# 클래스의 구성


# 1. 클래스의 기본 구성
# 객체를 만들어내는 클래스는 객체가 가져야 할 값과 기능을 가지고 있어야 함
# 값은 변수, 기능은 함수
# 정리하면 클래스는 변수와 함수로 구성된다고 볼 수 있음
# - 관리를 하기 위해 변수와 함수를 모아서 관리 한다는 뜻

# 클래스를 구성하는 변수는 1) 클래스를 기본으로 생성된 모든 인스턴스들이 공유하는 변수인 클래스 변수와
# 2) 모든 인스턴스들이 개별적으로 가지는 변수인 인스턴스 변수로 분리됨

# 클래스를 구겅하는 함수는 메소드 method라고 하고
# 1) 클래스 메소드 2) 정적 메소드 3) 인스턴스 메소드로 분리


# 2. 인스턴스 변수와 인스턴스 메소드
# 인스턴스 변수란 클래스를 기반으로 만들어지는 모든 인스턴스들이 각각 따로 저장하는 변수
# 모든 인스턴스 변수는 self라는 키워드를 앞에 붙여줌
# 인스턴스 메소드란 인스턴스 변수를 사용하는 메소드
# 인스턴스 메소드는 반드시 첫 번째 매개변수로 self를 추가해야 함


class Person :      # Person 클래스를 정의 
    # 첫 번째 매개변수는 self이므로 인스턴스 메소드
    # 모든 인스턴스는 who_am_i() 메소드를 호출 할 수 있음
    # 매개변수 self에는 메서드를 호출하는 인스턴스가 전달
    def who_am_i(self, name, age, tel, address) :
        # 인스턴스 변수 = 매개변수 . 모든 인스턴스 변수는 최초에 값이 대입되는 시점에 알아서 생성
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

boy = Person() # 인스턴스 boy가 생성 . 클래스의 생성자가 호출
# print(boy.name) # 'Person' Object has no attribute 'name' - 데이터 입력전이라서 생성이 안됨 : 저장공간이 없다는 뜻?
boy.who_am_i('john', 15, '123-1234', 'toronto')
print(boy.name) # john
print(boy.age)  # 15
print(boy.tel)  # 123-1234
print(boy.address)  # toronto




