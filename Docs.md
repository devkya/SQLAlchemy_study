# SQLAlchemy 2.0 문서
## 구성
 - SQLAlchemy Core
   - 데이터베이스 툴킷으로서 SQLAlchemy의 기본 아키텍처. DB 연결 관리 및 DB 쿼리 및 결과와 상호 작용하고, SQL 문의 프로그래밍적 구성을 위한 도구 제공 
 - SQLAlchemy ORM
   - `Core` 기반으로 하여 객체 관계 매핑 기능을 제공함. `ORM`은 사용자 정의 python class를 DB 테이블 및 기타 구성 요소에 매핑 할 수 있는 추가 구성 계층과 `Session`이라고 알려진 객체 지속성 메커니즘을 제공함

### 개념 정리
 - Transaction
   - DB 시스템에서 일련의 작업을 하나의 단위로 묶어서 처리하는 개념. 모든 작업이 성공적으로 완료되거나(commit) 전부 취소되어야(rollback) 한다는 원자성을 보장함
   - 