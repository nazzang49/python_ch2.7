# (방법1 - path 직접 입력) 다른 프로젝트에 있는 .py 파일 활용
# import sys
# sys.path.append('..\python-modules')
# 문법 체크 = 에러 O
# 실제 실행 = 에러 X

# (방법2 - 환경변수 설정) settings - project interpreter - show all - show path - add 특정 프로젝트
import mymath

print(mymath.pi)
print(mymath.add(10, 20))
print(mymath.area_circle(10))

