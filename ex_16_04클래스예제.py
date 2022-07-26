# 컴퓨터 스펙 관리 클래스 예제

class Computer :

    def set_spec(self, cpu, ram, vga, ssd) :
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self) :
        print(f'CPU = {self.cpu}')
        print(f'RAM = {self.ram}')
        print(f'VGA = {self.vga}')
        print(f'SSD = {self.ssd}')

desktop = Computer()
desktop.set_spec('i7', '16GB', 'GTX1060', '512GB')
desktop.hardware_info()

notebook = Computer()
notebook.set_spec('i5', '8GB', 'MX300', '256GB')
notebook.hardware_info()

print()


#  계산기 클래스 예제



class Calculator :

    def input_expr(self) :
        expr = input('수식을 입력하세요 >> ')   # 지역변수에 저장
        self.expr = expr    # 인스턴스 변수에 저장

    def calculator(self) :
        return eval(self.expr)

calc = Calculator()     # 객체 생성
calc.input_expr()
print(f'수식 결과는 {calc.calculator()} 입니다.')