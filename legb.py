# 1. Local
# 2. Enclosing Function(내포 함수)
# 3. Global
# 4. Built-in

a = 1 # G
def f():
    b = 200 # E
    def g():
        b = 100 # L
        print(b) # L이 주석처리 되어도, E가 존재하므로 에러 발생 X
        print(__name__) # B
    g()
f()

# B를 사용하는 경우 = 다른 파일에서 import 할 때 f()의 실행 제재
if __name__ == '__main__':
    f()










