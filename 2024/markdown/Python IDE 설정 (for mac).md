맥에는 기본적으로 파이썬이 설치되어 있지만 버전이 낮을 것이다.

## 1. 버전 확인 방법: ~ --version
'''
python3 --version
python --version
'''

결과
(base) admin@adminui-MacBookAir ~ % python --version

Python 3.9.6

(base) admin@adminui-MacBookAir ~ % python3 --version

Python 3.11.7
> 파이썬이 두개 설치된 것 같다.

## 2. 설치 경로 확인: which ~
'''
which python
'''

결과
(base) admin@adminui-MacBookAir ~ % which python

python: aliased to /usr/bin/python3

(base) admin@adminui-MacBookAir ~ % which python3

/opt/anaconda3/bin/python3
> python3 의 경우 아나콘다 설치를 통해 함께 설치된 것 같다.

## 3. 라이브러리 설치: pip, pip3
'''
pip install requests
pip3 install requests
python -m pip install requests 
> (사용하는 파이썬 버전에 해당하는 pip가 뭔지 모르면 **-m** 추가)  
'''
