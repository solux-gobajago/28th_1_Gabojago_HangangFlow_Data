import pandas as pd
import numpy as np
import json

df = pd.read_csv('data\static\csv\keyword.csv', encoding='utf-8') # 'utf-8' 인코딩 방식으로 데이터프레임 읽기
selected_buttons = ["산책", "야구장", "휴식"]

#=======================================================================================================

from flask import Flask, jsonify, render_template, request, redirect
from flask_cors import CORS
from db_connect import db
from sqlalchemy import create_engine, text

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# DB
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    database = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], max_overflow=0)
    app.database = database
    return app
app = create_app()

# CORS 설정: 모든 도메인으로부터 요청을 허용합니다. (실제 운영에서는 더 정확한 제한이 필요합니다)
# 또는 특정 도메인만 허용하려면 아래와 같이 origins 매개변수를 사용합니다.
# CORS(app, origins="http://allowed-domain.com")
CORS(app, resources={r'*': {'origins': 'http:localhost//:8000'}})
# CORS(app)

@app.route('/data/park_keywords', methods=['GET'])
def get_keywords():
    keywords = request.args.getlist('selected[]')
    # keywords = request.args.get()
    selected_buttons = keywords
    return selected_buttons
    # keywords = request.args.get()

@app.route('/data/park_list', methods=['GET'])
def get_json():
    # DataFrame을 JSON 형식으로 변환
    # data = request.json
    # selected_buttons = data['button_values']
    selected_buttons = get_keywords()
    
    df['합계'] = df[selected_buttons].sum(axis=1) # 선택한 속성들의 수치 합을 계산
    sorted_df = df.sort_values(by='합계', ascending=False) # 수치 합을 기준으로 데이터프레임을 내림차순으로 정렬
    top_3_parks = np.array(sorted_df.iloc[:3, 0]).tolist()

    park_list = []
    for i in top_3_parks:
        park_list.append(i+"한강공원")
    return park_list # 한강공원 list return -> db에서 비교 후 uuid select

@app.route('/data/park_uuid', methods=['GET'])
def get_uuid():
    park_list = get_json()
    uuid_list = []
    try:
        for park_name in park_list:
            query = text("SELECT park_uuid FROM park WHERE park_name=:park_name")
            with app.app_context():
                park_data = db.session.execute(query, {'park_name': park_name}).fetchone()
                if park_data:
                    park_uuid = park_data[0]

                    # # UUID가 문자열이 아닌 경우, 문자열로 변환
                    # if not isinstance(park_uuid, str):
                    #     park_uuid = str(park_uuid)

                    uuid_list.append(str(park_uuid))

        return {'park_uuid': uuid_list}
    except Exception as e:
        error_message = str(e)  # 예외를 문자열로 변환
        return {'error_message': json.dumps(error_message)}

if __name__ == '__main__':
    app.run(debug=True, port=8000)