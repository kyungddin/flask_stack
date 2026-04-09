# API 서버
- 데이터 통신을 위해 사용하는 서버
    - 다른 애플리케이션에 데이터를 제공해준다
- 처리 대상: JSON, XML 등 데이터를 포함한 Body 컨텐츠
- 기능: DB 연동, 다른 애플리케이션과의 통신
- 프로토콜: HTTP, HTTPS

- 흐음.. DB에 접근하기 위한 중간 서버 정도로 생각해야 하나.. (어쨌든 API니까)


# Flask Basic Structure : Application Factory
```python
from flask import Flask

def create_app(): # Application Factory(=Create App): Flask 애플리케이션을 생성하는 함수
    app = Flask(__name__)
    @app.route('/') # 라우트 데코레이터: URL과 함수를 연결하는 역할
    def hello(): # route에 의해 url에 연결되는 함수
        return 'Hello, TechWing!'
    return app

# But! 이런식이면 새로운 URL이 생길 때 라우트 함수를 앱 팩토리에 계속 추가해줘야 함!
# 따라서 우리는 블루트린트라는 것을 이용할 것이다..
```