from os import environ
from flask import request, session
import invoice_challenge.helpers.controller_helper as ControllerHelper
import pytest
import time

def test_should_succeed_format_get_collection_response():
    data_resp = [
        {
            "id": 1,
            "name": "test_name"        
        },
        {
            "id": 2,
            "name": "another_name"        
        }
    ]
    params = {
        "pageSize": 50,
        "page": 0,
    }
    result = ControllerHelper.format_get_collection_response(data_resp, params)
    expected = {
        "data": data_resp,
        "total": 2,
        "page_size": 50,
        "page": 0
    }
    assert result == expected

def test_should_succeed_format_get_collection_response_without_data():
    data_resp = []
    params = {}
    result = ControllerHelper.format_get_collection_response(data_resp, params)
    expected = {
        "data": data_resp,
        "total": 0,
        "page_size": 100,
        "page": 0
    }
    assert result == expected

def test_should_succeed_format_get_collection_response_with_only_one_param():
    data_resp = [
        {
            "id": 1,
            "name": "test_name"        
        }
    ]
    params = {
        "page": 2,
    }
    result = ControllerHelper.format_get_collection_response(data_resp, params)
    expected = {
        "data": data_resp,
        "total": 1,
        "page_size": 100,
        "page": 2
    }
    assert result == expected

def test_should_succeed_encode_auth_token_types():
    environ["SECREAT_KEY"] = "a_random_secret_key"
    user_id = 1
    result = ControllerHelper.encode_auth_token(user_id)
    assert type(result) == bytes
    assert type(result.decode()) == str

def test_should_succeed_decode_auth_token():
    environ["SECREAT_KEY"] = "a_random_secret_key"
    user_id = 1
    auth_token = ControllerHelper.encode_auth_token(user_id)
    result = ControllerHelper.decode_auth_token(auth_token)
    assert result == user_id
