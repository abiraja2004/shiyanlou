""" rmon.views.urls

定义了所有 API 对应的 URL
"""
from flask import Blueprint

from rmon.views.user import UserList, UserDetail
from rmon.views.auth import AuthView, RefreshTokenView

api = Blueprint('api', __name__)

# 登录
api.add_url_rule('/login', view_func=AuthView.as_view('login'))
api.add_url_rule('/token/refresh',
                 view_func=RefreshTokenView.as_view('refresh_token'))

# 用户管理
api.add_url_rule('/users/', view_func=UserList.as_view('user_list'))
api.add_url_rule('/users/<int:object_id>',
                 view_func=UserDetail.as_view('user_detail'))
