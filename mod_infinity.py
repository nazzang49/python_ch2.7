import sys

import mod_a
# 중복 모듈에 대해 단 1회만 호출 = 무한 반복 제재
print("import infinity")

for key in sys.modules.keys():
    print(key)