# from fastapi import APIRouter
# from sqlalchemy.exc import NoResultFound
#
# from database import session_factory
# from users.models import UserORM
#
# router = APIRouter(
#     prefix="/users",
#     tags=["Users"]
# )
#
# @router.get("/user/{user_id}")
# def get_user(user_id):
#     try:
#         with session_factory() as session:
#             query = session.get_one(UserORM, user_id)
#             # result = session.execute(query)
#             # user = result.scalars().all()
#         return {"status": f"Добро пожаловать, {query.username}!"}
#     except NoResultFound:
#         return {"status": 404, "data": f"Юзер с id={user_id} не найден!"}
#
#
# @router.post("/new_user")
# def set_user(name: str):
#     with session_factory() as session:
#         stmt = UserORM(username=name)
#         session.add(stmt)
#         session.commit()
#     return {"status": f"Add {name}: success"}