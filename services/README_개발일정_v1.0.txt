Step 1. CRUD 기능 개발
  1.1 (완료) 리스트, Search, Column Filter, Export to CSV 기능 구현/TEST (12/04)
  1.2 (완료) markdown/highlight 기능 구현/TEST (12/09)
  1.3 (완료) parent-child component 간 통신 구현/TEST (12/09)
  1.4 (완료) 기본 폼 생성 (12/20)
  1.5 (완료) 날짜 처리 플러그인 설치 (12/20)
      . vuetify date-time picker
      . moment
  1.6 (완료) Dockerization (12/20)
  1.7 (완료) Model 창 날짜 표기 변환(format) (12/23)
  1.8 (중단) Model 창 markdown 표기 변환(format) (12/23, 연동 후 재 시도)
      . markdown & highlight (no error, but not work)
  1.9 (완료) fastapi 연동 (참고:  https://www.digitalocean.com/community/tutorials/implementing-authentication-in-nuxtjs-app )
    1) fastapi CRUD using httpie
      . Update :  ex) http PUT "http://localhost:8000/incident/3730" region="KR" month=10 year=2023 az=1 tenant="1" event="test3" 
      . Create :  ex) http POST "http://localhost:8000/incident/" region="KR" month=10 year=2023 az=1 tenant="1" event="test3" 
      . Read   :  ex) http GET "http://localhost:8000/incident/3730"   
      . Delete :  ex) http DELETE "http://localhost:8000/incident/3755"
    2) Production 이행 준비 (ERROR 422,405 건 해결)
        . Backend server (localhost-> IP) 환경 정보 설정 및 Incident Handling 에 적용
          JWT_KEY="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
          # BASE_URL=http://localhost:8000
          BASE_URL=http://192.168.30.254:8000
        . Method 별 Backend API 스키마 조정
          > GET_ALL/POST : SchemaID
          > PUT/GET_ID : Schema (without ID)
  1.10 (완료) 횡전개
    1) Topic별 횡전개
      A] frontend
        . (완료) Navbar 설정 외 기본틀 구성
        . topic별 대시보드 (list 내 링크 조정)
        . Detial 내 field 첨삭
      B] backend
        . Model
        . CRUD
        . Router
        . Schema

    **  http PUT "http://localhost:8000/capacity/188" region="KR" month=10 year=2023 az=1 tenant="1" title="test3"
        http PUT "http://localhost:8000/backup/1273" region="KR" month=10 year=2023 az=1 tenant="1" title="test3"
  1.11 Landing page (???)

Step 2. Tools
  2.1. 대시보드
  2.2. 그래프
  2.3. 분석기  
Step 3) Auth Token
      Register/Login/Logout
      
Step 4. 실시간 모니터링 (인시던트 핸들링 한정)
Step 5. 홈페이지
Step 6. 타 시스템 연동
  . 자산관리?
..,

