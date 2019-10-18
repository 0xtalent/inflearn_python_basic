# Chapter06-1
# 파이썬 클래스
# OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

# 클래스(붕어빵 틀) and 인스턴스(코드에서 사용하는 객체) 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재

# 예제1
class Dog: # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog("mikky", 2)
b = Dog("baby", 3)

# 비교
print(a == b, id(a), id(b))

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)

# 예제2
# self의 이해
class SelfTest:
    def func1():
        print('Func1 called')
    def func2(self):
        print(id(self))
        print('Func2 called')

f = SelfTest()

# print(dir(f))
print(id(f))
# f.func1() # 예외
f.func2()
SelfTest.func1()
# SelfTest.func2() # 예외
SelfTest.func2(f)

# self가 들어 있으면 인스턴스 메소드, 아무것도 없으면 클래스 메소드
# 잘 모르겠다ㅠㅠ 나중에 이해가 되겠지...

# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0 # 재고

    def __init__(self, name):
        # 인스턴스 변수(self 가 있네요)
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
# Warehouse.stock_num = 50
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)
print('>>>', user1.stock_num)
print()

del user1
print('after', Warehouse.__dict__)

# 1. 잘 모르겠어서 class에 대해 공부하기
# 2. 점프 투 파이썬으로 공부한다.
# 3. C 언어에는 클래스가 없다. 굳이 클래스가 없어도 프로그램을 충분히 만들 수 있다.
# 4. 파이썬으로 잘 만든 프로그램을 살펴보아도 클래스를 사용하지 않고 작성한 것들이 상당히 많다.
# 5. 하지만 프로그램을 작성할 때 클래스를 적재적소에 사용하면 프로그래머가 얻을 수 있는 이익은 상당하다.
# 6. 예를 들어) 계산기 / 계산기는 이전에 계산한 결과값을 기억하고 있어야 한다.
# 7.
# result = 0
#
# def add(num):
#     global result
#     result += num
#     return result
#
# print(add(3))
# print(add(4))

# 8. add 함수는 매개변수 num에 받은 값을 이전에 계산한 결과값에 더한 후 돌려주는 함수이다.
# 9. 이전에 계산한 결과값을 유지하기 위해서 result 전역 변수 global을 사용했다.
# 10. 계산기가 2개라면? 5개라면? 10개라면? 그때마다 전역 변수와 함수를 추가할 것인가?
# 11. 위와 같은 경우에 클래스를 사용하면 간단하게 해결할 수 있다.
# 12. 오 이해가 가기 시작합니다...이제 눈으로 공부...

# 예제4
class Dog: # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)

# 인스턴스 생성
c = Dog('july', 4)
d = Dog('Marry', 10)
# 메소드 호출
print(c.info())
print(d.info())
# 메소드 호출
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))
