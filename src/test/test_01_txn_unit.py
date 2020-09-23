import pytest
import os, io
from flask import Flask
from flask.wrappers import Response
from ..app import blueprint
from ..app.main import create_app
from werkzeug.datastructures import FileStorage

class Test():

    def _post_file(self, file_path: str, _web_app: Flask) -> Response:
        with open(file_path, 'rb') as f:
            data = {
                'file': (f, file_path)
            }
            with _web_app.test_client() as c:
                rv = c.post('/overdraft/file/',
                                 data=data)
                # return rv.data.decode('utf-8')
                return rv.json

    @pytest.fixture
    def _bad_json_file(self) -> FileStorage:
        filename = './test/fixtures/15731-ba.json'
        return filename

    @pytest.fixture
    def _good_json_file_1(self) -> FileStorage:
        filename = './test/fixtures/15475-ba.json'
        return filename

    @pytest.fixture
    def _web_app(self) -> Flask:
        os.environ['FLASK_ENV'] = 'development'
        app = create_app('test')
        app.register_blueprint(blueprint)
        app.app_context().push()
        return app

    def test_01_bad_json(self, _bad_json_file: str, _web_app: Flask) -> None:
        rv = self._post_file(_bad_json_file, _web_app)
        assert rv['status'] == "fail"

    def test_02_good_json(self, _good_json_file_1: str, _web_app: Flask) -> None:
        rv = self._post_file(_good_json_file_1, _web_app)
        assert rv['status'] == "success"

    def test_02_sum(self, _good_json_file_1: str, _web_app: Flask) -> None:
        rv = self._post_file(_good_json_file_1, _web_app)
        assert rv['data'][0]['data'][0]['value'] == 0.009150716113899024