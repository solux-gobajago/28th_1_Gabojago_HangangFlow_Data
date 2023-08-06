import pandas as pd
import numpy as np
import json

df = pd.read_csv('data\static\csv\keyword.csv', encoding='utf-8') # 'utf-8' 인코딩 방식으로 데이터프레임 읽기
selected_buttons = ["산책", "야구장", "휴식"]

#키워드 입력받기 (while 루프 이용)
# def get_input_list():
#     values_list = []
#     while True:
#         value = input() # 값들을 입력
#         if value.lower() == 'exit': # 키워드 입력 끝났음('확인'버튼)
#             break                   # '확인'버튼은 저장 안됨
#         values_list.append(value)   # 입력된 키워드들을 list에 저장
#     return values_list

# selected_attributes = get_input_list() #입력된 키워드들이 저장되는 리스트
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
CORS(app)

# @app.route('/result', methods=['POST'])
# def get_keyword():
#     if request.method == 'POST':
#         result = request.form
#         return render_template("result.html", result=result)
    
    # values_list = []
    # while True:
    #     value = input() # 값들을 입력
    #     if value.lower() == 'exit': # 키워드 입력 끝났음('확인'버튼)
    #         break                   # '확인'버튼은 저장 안됨
    #     values_list.append(value)   # 입력된 키워드들을 list에 저장
    # selected_attributes = values_list
    # return selected_attributes

@app.route('/react_to_flask', methods=['POST'])
def react_to_flask():
    data = request.json

@app.route('/data', methods=['GET'])
def get_json():
    # DataFrame을 JSON 형식으로 변환
    # data = request.json
    # selected_buttons = data['button_values']
    
    df['합계'] = df[selected_buttons].sum(axis=1) # 선택한 속성들의 수치 합을 계산
    sorted_df = df.sort_values(by='합계', ascending=False) # 수치 합을 기준으로 데이터프레임을 내림차순으로 정렬
    top_3_parks = np.array(sorted_df.iloc[:3, 0]).tolist()

    park_list = []
    for i in top_3_parks:
        park_list.append(i+"한강공원")
    return park_list # 한강공원 list return -> db에서 비교 후 uuid select

@app.route('/park_uuid', methods=['GET'])
def get_uuid():
    park_list = get_json()
    uuid_list = {}
    try:
        for park_name in park_list:
            query = text("SELECT park_uuid FROM park WHERE park_name=:park_name")
            with app.app_context():
                park_data = db.session.execute(query, {'park_name': park_name}).fetchone()
                if park_data:
                    # Park의 UUID에 대해 UTF-8 또는 EUC-KR 중 적절한 인코딩을 시도하며 디코딩합니다.
                    try:
                        park_uuid = park_data[0].decode("utf-8")
                    except UnicodeDecodeError:
                        park_uuid = park_data[0].decode("EUC-KR")
                    
                    uuid_list[park_name] = park_uuid
        return {'park_uuid': uuid_list}
    except Exception as e:
        error_message = str(e)  # 예외를 문자열로 변환
        return {'error_message': json.dumps(error_message)}

# @app.route('/')
# def index():
#     return render_template('/static/App.js') # main page

if __name__ == '__main__':
    app.run(debug=True, port=8000)