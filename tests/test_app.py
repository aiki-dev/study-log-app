import os
import sys
import pytest

# 1つ上の階層にあるapp.pyを読み込めるようにする
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app

# テストで使うクライアントを作成
@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

# トップページが正常に開けるか確認
def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200

# トップページにタイトルが表示されるか確認
def test_home_page_title(client):
    response = client.get("/")
    assert "勉強記録アプリ" in response.data.decode("utf-8")

# 日付が空欄のときにエラーメッセージが出るか確認
def test_blank_date_error(client):
    response = client.post("/", data={
        "study_date": "",
        "subject": "数学",
        "study_time": "60"
    })
    assert "すべての項目を入力してください。" in response.data.decode("utf-8")