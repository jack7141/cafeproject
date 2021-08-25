# StartUp Project
Anaconda를 활용하여 Django를 구축, 패키지 정리



### 2021-08-18

---
* App 생성
 
users - 유저관련 class

conversations - 메세지(대화) 관련 class

list - 

reviews - 댓글

reservations - 예약 관련 class







---
### 주의사항

* Application 이름들은 무조건 복수형으로 사용해야한다.
* C:\Users\ghl92\Project\CafeProject 구조의 시작은,
  내 project가 시작하는 위치를 기준으로 경로를 잡아야함
---

### 개발노트  
> Application 내부의 migrations 폴더를 삭제했을 경우, 
> 그냥 폴더를 수동으로 만들고 __init__.py만 만들어서 다시 처음부터 진행하면 됨

> 번호 모델을 생성하기 위해서 pip install django-phonenumber-field 설치
> 
>

> django-seed를 통해서 더비 데이터 생성
> 1. 내가 만들고자 하는 App폴더 내부에서 management폴더 생성
> 2. management폴더 내부에서 __init__.py 파일 및 commands폴더 생성
> 3. commands폴더 내부에서 __init__.py 파일 생성
> 
> 데이터가 많이 필요하지 않은 부분은 내가 직접 수동으로 사용할 수 있지만, 이메일 혹은 사용자 계정같은 부분은
> 수동으로 하기엔 너무 방대한 양이기 때문에  Django에서 제공하는 django_seed를 사용해서 더미 데이터를 넣어준다.
> 

### QUREYSET & MANAGE
> ORM Qureyset 문서
> 
> https://docs.djangoproject.com/en/3.2/topics/db/queries/
>
> 강의 7참고!!!!!!!!

#### relate_name이란
> 정참조 역참조의 개념
> 
>    역참조를 위해서 기존의 _set을 사용하기엔 너무 귀찮으니까 related_name을 사용한다.
    정참조는 상관없음
    정참조란 현재 Cafe를 바라보고 있는 host는 Cafe모델에서 cafe.host.요소 이런식으로 접근이 가능하다.
    반면 user쪽에서는 어떤 카페데이터를 가지고 있는지 알 수 없다.
    그렇기 때문에 만들어진게 related_name을 사용해서 역으로 user모델에서도 cafe를 알 수 있도록한다.
    즉, 특정 유저가 어떤 카페의 정보를 가지고 있는지 알 수 있게 된다.
     
