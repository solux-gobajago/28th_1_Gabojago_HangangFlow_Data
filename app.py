# import pandas as pd
# import numpy as np
# import json

# df = pd.read_csv('keyword.csv', encoding='utf-8') # 'utf-8' 인코딩 방식으로 데이터프레임 읽기
# # selected_buttons = ["산책", "야구장", "휴식"]

# #=======================================================================================================
# import uuid
# from flask import Flask, jsonify, render_template, request, redirect
# from flask_cors import CORS
# from db_connect import db
# from sqlalchemy import create_engine, text


# app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False

# selected_keywords = []

# # DB
# def create_app():
#     app = Flask(__name__)
#     app.config.from_pyfile("config.py")
#     db.init_app(app)
#     database = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], max_overflow=0)
#     app.database = database
#     return app
# app = create_app()

# # CORS 설정: 모든 도메인으로부터 요청을 허용합니다. (실제 운영에서는 더 정확한 제한이 필요합니다)
# # 또는 특정 도메인만 허용하려면 아래와 같이 origins 매개변수를 사용합니다.
# # CORS(app, origins="http://allowed-domain.com")
# # CORS(app, resources={r'*': {'origins':  'http://localhost:3000'}})
# # # CORS(app)

# # @app.route('/data/keywords', methods=['POST'])
# # def post_keywords():
# #     global selected_keywords

# #     try : 
# #         data = request.get_json()
# #         selected_buttons = data['keywords']
# #         print(selected_buttons)
# #         return jsonify({'status': 'success'}), 200
# #     except Exception as e :
# #         print("Error", e)

# # def get_keywords():
# #     return selected_keywords

# # @app.route('/data/parks', methods=['GET'])
# # def get_park():
# #     # DataFrame을 JSON 형식으로 변환
# #     selected_buttons = get_keywords()
    
# #     df['합계'] = df[selected_buttons].sum(axis=1) # 선택한 속성들의 수치 합을 계산
# #     sorted_df = df.sort_values(by='합계', ascending=False) # 수치 합을 기준으로 데이터프레임을 내림차순으로 정렬
# #     top_3_parks = np.array(sorted_df.iloc[:3, 0]).tolist()

# #     park_list = []
# #     for i in top_3_parks:
# #         park_list.append(i+"한강공원")
# #     return park_list # 한강공원 list return -> db에서 비교 후 uuid select

# # def bytes_to_uuid_string(uuid_bytes):
# #     return str(uuid.UUID(bytes=uuid_bytes))

# # @app.route('/data/park_uuid', methods=['GET'])
# # def get_uuid():
# #     park_list = get_park()
# #     uuid_list = []
# #     try:
# #         for park_name in park_list:
# #             query = text("SELECT park_uuid FROM park WHERE park_name=:park_name")
# #             with app.app_context():
# #                 park_data = db.session.execute(query, {'park_name': park_name}).fetchone()
# #                 if park_data:
# #                     park_uuid = park_data[0]

# #                     # # UUID가 문자열이 아닌 경우, 문자열로 변환
# #                     # if not isinstance(park_uuid, str):
# #                     #     park_uuid = str(park_uuid)
# #                     uuid_string = bytes_to_uuid_string(park_uuid)
# #                     uuid_list.append(uuid_string)
# #         print(uuid_list)
# #         return {'park_uuid': uuid_list}
# #     except Exception as e:
# #         error_message = str(e)  # 예외를 문자열로 변환
# #         return {'error_message': json.dumps(error_message)}

# # if __name__ == '__main__':
# #     app.run(debug=True, port=8000)

# CORS(app, resources={r'*': {'origins': 'http://localhost:3000'}})

# @app.route('/data', methods=['GET'])
# def get_park_uuids():
#     try:
#         keywords = request.args.getlist('keyword')  # 쿼리 스트링에서 'keyword' 파라미터를 리스트로 받아옴
#         park_list = get_park(keywords)
#         uuid_list = []

#         for park_name in park_list:
#             query = text("SELECT park_uuid FROM park WHERE park_name=:park_name")
#             with app.app_context():
#                 park_data = db.session.execute(query, {'park_name': park_name}).fetchone()
#                 if park_data:
#                     park_uuid = park_data[0]
#                     uuid_string = bytes_to_uuid_string(park_uuid)
#                     uuid_list.append(uuid_string)

#         return {'park_uuid': uuid_list}
#     except Exception as e:
#         error_message = str(e)
#         return {'error_message': error_message}

# def get_park(selected_buttons):
#     df['합계'] = df[selected_buttons].sum(axis=1) # 선택한 속성들의 수치 합을 계산
#     sorted_df = df.sort_values(by='합계', ascending=False) # 수치 합을 기준으로 데이터프레임을 내림차순으로 정렬
#     top_3_parks = np.array(sorted_df.iloc[:3, 0]).tolist()

#     park_list = []
#     for i in top_3_parks:
#         park_list.append(i+"한강공원")
#     return park_list

# def bytes_to_uuid_string(uuid_bytes):
#     return str(uuid.UUID(bytes=uuid_bytes))

# if __name__ == '__main__':
#     app.run(debug=True, port=8000)
##################

# import pandas as pd
# import numpy as np
# import json

# df = pd.read_csv('keyword.csv', encoding='utf-8') # 'utf-8' 인코딩 방식으로 데이터프레임 읽기

# #=======================================================================================================
# import uuid
# from flask import Flask, jsonify, render_template, request, redirect
# from flask_cors import CORS
# from db_connect import db
# from sqlalchemy import create_engine, text

# app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False

# selected_keywords = []

# # DB
# def create_app():
#     app = Flask(__name__)
#     app.config.from_pyfile("config.py")
#     db.init_app(app)
#     database = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], max_overflow=0)
#     app.database = database
#     return app
# app = create_app()

# # CORS 설정: 모든 도메인으로부터 요청을 허용합니다. (실제 운영에서는 더 정확한 제한이 필요합니다)
# # 또는 특정 도메인만 허용하려면 아래와 같이 origins 매개변수를 사용합니다.
# # CORS(app, origins="http://allowed-domain.com")
# CORS(app, resources={r'*': {'origins':  'http://localhost:4000'}})
# @app.route('/data', methods=['GET'])
# def post_keywords():
#     global selected_keywords
#     try : 
#         # keyword -> list
#         keyword = request.args.getlist("keyword")
#         keywords = ', '.join(keyword) # 추가한 부분
#         print("flask --- keywords", keywords)
#         selected_keywords = keywords
#         print("flask --- selected_keywords", selected_keywords)
#         # keywordlist -> park list
#         df['합계'] = df[selected_keywords].sum(axis=1)
#         sorted_df = df.sort_values(by='합계', ascending=False)
#         parks = np.array(sorted_df.iloc[:, 0]).tolist()
#         park_list = []
#         for i in parks:
#             park_list.append(i+"한강공원")
#         print("flask ---- park_list", park_list)
#         # park list -> uuid list
#         uuid_list = []
#         try:
#             for park_name in park_list:
#                 query = text("SELECT park_uuid FROM park WHERE park_name=:park_name")
#                 with app.app_context():
#                     park_data = db.session.execute(query, {'park_name': park_name}).fetchone()
#                     if park_data:
#                         park_uuid = park_data[0]
#                         uuid_string = str(uuid.UUID(bytes=park_uuid))
#                         uuid_list.append(uuid_string)
#             result = jsonify({'park_uuid': uuid_list})
#             print("flask---- result", result)
#             return result, 200  # 유효한 응답 반환
#         except Exception as e:
#             print("flask---- error")
#             error_message = str(e)
#             return {'error_message': json.dumps(error_message)}, 500  # 유효한 응답 반환
#     except Exception as e:
#         error_message = str(e)
#         return {'error_message': json.dumps(error_message)}, 500  # 유효한 응답 반환


# if __name__ == '__main__':
#     app.run(debug=True, port=8000)
import pandas as pd
import numpy as np
import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS
from db_connect import db
from sqlalchemy import create_engine, text

# 데이터프레임 초기화
df = pd.read_csv('./keyword.csv', encoding='utf-8')

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app, resources={r'*': {'origins':  'http://localhost:4000'}})

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    database = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], max_overflow=0)
    app.database = database
    return app

app = create_app()

@app.route('/data', methods=['GET'])
def get_park_uuids():
    try:
        selected_keywords = request.args.get("keyword").split(",")
        if not selected_keywords:
            return {'error_message': 'No keywords provided'}, 400

        # 키워드가 데이터프레임의 컬럼에 있는지 확인
        invalid_keywords = [kw for kw in selected_keywords if kw not in df.columns]
        if invalid_keywords:
            return {'error_message': f'Invalid keywords: {", ".join(invalid_keywords)}'}, 400

        
        if isinstance(selected_keywords, str):
            selected_keywords = [selected_keywords]

        park_list = get_park(selected_keywords)
        print("print--- park list", park_list)
        uuid_list = []
     

        for park_name in park_list:
            query = text("SELECT park_uuid FROM park WHERE park_name=:park_name")
            with app.app_context():
                park_data = db.session.execute(query, {'park_name': park_name}).fetchone()
                # park_data = db.session.query.filter_by(filter).first()
                if park_data:
                    park_uuid = park_data[0]
                    uuid_string = str(uuid.UUID(bytes=park_uuid))
                    uuid_list.append(uuid_string)
        result = {'park_uuid': uuid_list}
        print("check result", result)
        return result
    except Exception as e:
        error_message = str(e)
        return {'error_message': error_message}, 500

def get_park(selected_keywords):
    df['합계'] = df[selected_keywords].sum(axis=1)
    sorted_df = df.sort_values(by='합계', ascending=False)
    # top_3_parks = np.array(sorted_df.iloc[:3, 0]).tolist()
    parks = np.array(sorted_df.iloc[:, 0]).tolist()
    park_list = [i + "한강공원" for i in parks]
    return park_list

if __name__ == '__main__':
    app.run(debug=True, port=8000)
