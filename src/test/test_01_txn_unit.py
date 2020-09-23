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
                rv = c.post('/rates/file/',
                                 data=data)
                return rv.data.decode('utf-8')

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
        assert '"status": "fail"' in rv

    def test_01_good_json(self, _good_json_file_1: str, _web_app: Flask) -> None:
        rv = self._post_file(_good_json_file_1, _web_app)
        assert '"status": "success"' in rv
