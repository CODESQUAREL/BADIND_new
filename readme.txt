
python interpreter 설정
( anaconda 말고 라이브러리 하나도 설치 안 된 깨끗한 상태의 python interpreter 추천)


라이브러리 설치
pip install Django Django-bootstrap4 pillow
pip install django-environ

테스트용 db생성
(makemigrations는 안 해도됨 commit되어있음)
python manage.py migrate

서버구동
python manage.py runserver

서버주소
http://127.0.0.1:8000

빠이팅!!