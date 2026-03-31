import os
import sys
import pytest

# 1つ上の階層にあるapp.pyを読み込めるようにする
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app

# テスト用クライアントとCSVを準備
@pytest.fixture
def test_resources(tmp_path):
    test_csv = tmp_path / "test_study_log.csv"

    app.config["TESTING"] = True
    app.config["CSV_PATH"] = str(test_csv)

    with app.test_client() as test_client:
        yield test_client, test_csv

# トップページが正常に開けるか確認
def test_home_page(test_resources):
    test_client, test_csv = test_resources
    response = test_client.get("/")
    assert response.status_code == 200

# トップページにタイトルが表示されるか確認
def test_home_page_title(test_resources):
    test_client, test_csv = test_resources
    response = test_client.get("/")
    assert "勉強記録アプリ" in response.data.decode("utf-8")

# 日付が空欄のときにエラーメッセージが出て保存されないか確認
def test_blank_date_error(test_resources):
    test_client, test_csv = test_resources
    response = test_client.post("/", data={
        "study_date": "",
        "subject": "数学",
        "study_time": "60"
    })
    assert "すべての項目を入力してください。" in response.data.decode("utf-8")
    assert not test_csv.exists()

# 学習時間に文字を入れたときにエラーが出るか確認
def test_string_time_error(test_resources):
    test_client, test_csv = test_resources
    response = test_client.post("/", data={
        "study_date": "2026-03-01",
        "subject": "数学",
        "study_time": "abc"
    })
    assert "学習時間は整数で入力してください。" in response.data.decode("utf-8")

# 学習時間に0を入れたときにエラーが出るか確認
def test_zero_time_error(test_resources):
    test_client, test_csv = test_resources
    response = test_client.post("/", data={
        "study_date": "2026-03-01",
        "subject": "数学",
        "study_time": "0"
    })
    assert "学習時間は1~1440の範囲で入力してください。" in response.data.decode("utf-8")

# 正常入力でCSVに保存されることを確認
def test_valid_input_saves_data(test_resources):
    test_client, test_csv = test_resources

    response = test_client.post("/", data={
        "study_date": "2026-03-01",
        "subject": "数学",
        "study_time": "60"
    })

    response_text = response.data.decode("utf-8")

    assert response.status_code == 200
    assert "保存しました。" in response_text
    assert test_csv.exists()

    content = test_csv.read_text(encoding="utf-8")
    assert "2026-03-01,数学,60" in content

# 学習時間に1441を入れたときにエラーが出て保存されないか確認
def test_over_max_time_error(test_resources):
    test_client, test_csv = test_resources
    response = test_client.post("/", data={
        "study_date": "2026-03-01",
        "subject": "数学",
        "study_time": "1441"
    })
    assert "学習時間は1~1440の範囲で入力してください。" in response.data.decode("utf-8")
    assert not test_csv.exists()

# 学習時間に1440を入れたときに正常に保存されるか確認
def test_max_time_valid_save(test_resources):
    test_client, test_csv = test_resources

    response = test_client.post("/", data={
        "study_date": "2026-03-01",
        "subject": "数学",
        "study_time": "1440"
    })

    response_text = response.data.decode("utf-8")

    assert response.status_code == 200
    assert "保存しました。" in response_text
    assert test_csv.exists()

    content = test_csv.read_text(encoding="utf-8")
    assert "2026-03-01,数学,1440" in content