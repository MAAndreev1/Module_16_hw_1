from fastapi import FastAPI

app = FastAPI()

# Start - uvicorn home_work_1:app

@app.get("/")
async def welcome() -> dict:
    return {'message': 'Главная страница'}


@app.get("/user/admin")
async def admin() -> dict:
    return {'message': f'Вы вошли как администрато'}

@app.get("/user/{user_id}")
async def get_id(user_id: int) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get("/user")
async def id_paginator(username: str, age: int) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}.'}