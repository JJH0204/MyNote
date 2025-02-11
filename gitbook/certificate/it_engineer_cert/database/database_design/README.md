# 데이터베이스 설계

## 데이터베이스 설계란?

* 효율적인 데이터 저장, 검색, 관리를 위해 데이터베이스 구조를 정의하는 과정을 의미한다.
* 설계가 잘못되면 데이터 중복, 성능 저하, 유지보수 문제가 발생할 수 있기 때문에 체계적인 접근이 필요하다.

***

## 데이터베이스 설계과정

* 데이터베이스 설계는 아래 순서에 맞춰 단계별로 진행한다.



| 단계 | 명칭                                                                              | 설명                                  |
| -- | ------------------------------------------------------------------------------- | ----------------------------------- |
| 1  | <p><a href="requirement-analysis.md">요구 사항 분석<br>(Requirement Analysis)</a></p> | 사용자 요구 사항을 수집하고 분석                  |
| 2  | <p><a href="conceptual-design.md">개념적 설계<br>(Conceptual Design)</a></p>         | ERD(Entity-Relationship Diagram) 작성 |
| 3  | <p><a href="logical-design.md">논리적 설계<br>(Logical Design)</a></p>               | 정규화(Normalization), 관계형 모델 변환       |
| 4  | <p>물리적 설계<br>(Physical Design)</p>                                              | 성능 최적화를 고려한 저장 구조 및 인덱스 설계          |
| 5  | <p>구현 및 운영<br>(Implementation &#x26; Maintenance)</p>                           | 실제 데이터베이스 구축, 튜닝 및 유지보수             |
