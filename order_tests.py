# ГАДЖИАГАЕВ ХАБИБ, 14-КОГОРТА, финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data
import pytest
import configuration
import requests

def positive_assert(track):
     params= data.get_track_params.copy()
     params['t'] = track
     request = sender_stand_request.get_order_by_track(params)
     print(request)
     assert request.status_code == 200

#Тест 1
#При поиске по номеру статус код = 200
def test_status_code_get_order():
    positive_assert(sender_stand_request.post_new_order(data.post_order_body, data.headers).json()["track"])