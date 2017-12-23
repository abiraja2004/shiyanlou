""" rmon.views.decorators

该模块实现了视图控制器装饰器
"""

from functools import wraps
from flask import g, request

from rmon.common.errors import RestError, AuthenticationError
from rmon.models import User


class ObjectMustBeExist:
    """该装饰器确保操作的对象必须存在
    """

    def __init__(self, object_class):
        """
        Args:
            object_class (class): 数据库对象
        """

        self.object_class = object_class

    def __call__(self, func):
        """装饰器实现
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            Args:
                object_id (int): SQLAlchemy object id
            """

            object_id = kwargs.get('object_id')
            if object_id is None:
                raise RestError(404, 'object not exist')

            obj = self.object_class.query.get(object_id)
            if obj is None:
                raise RestError(404, 'object not exist')

            g.instance = obj
            return func(*args, **kwargs)

        return wrapper


class TokenAuthenticate:
    """通过 jwt 认证用户

    验证 HTTP Authorization 头所包含的 token
    """

    def __init__(self, admin=True, verify_exp=True):
        """
        Args:
            admin(bool): 是否需要验证管理员权限
        """
        self.admin = admin
        self.verify_exp = verify_exp


    def __call__(self, func):
        """装饰器实现
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 补全代码
            jwt_token = request.headers.get('Authorization')
            if jwt_token is not None:
                jwt_token = jwt_token.split(" ")[-1]
            else:
                jwt_token = request.form.get('token')
                if jwt_token is None:
                    jwt_token = request.args.get('token')
                    if jwt_token is None:
                        raise RestError(403, 'token not exist')
            g.instance = User.verify_token(jwt_token)
            return func(*args, **kwargs)
        return wrapper
