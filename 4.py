# from fastapi import FastAPI

# # 创建服务
# app = FastAPI()


# class TaskResponse(BaseModel):
#     user_id: str
#     summary: str
#     accepted: bool


# class TaskRequest(BaseModel):
#     user_id: str
#     title: str
#     priority: int


# @app.post("/tasks/analyze", response_model=TaskResponse)
# def analyze(task: TaskRequest):
#     if task.priority < 1 or task.priority > 5:
#         raise HTTPException(status_code=400, detail="Invalid priority")
#     return {
#         "user_id": "用户 id",
#         "summary": "任务 标题 的优先级是 priority",
#         "accepted": true,
#     }


#   1. 创建 FastAPI 服务。
#   2. 定义 UserRequest：
#       - user_id: str
#       - name: str
#       - age: int
#   3. 定义 UserResponse：
#       - user_id: str
#       - message: str
#       - valid: bool
#   4. 创建接口：

#   POST /users/check

#   5. 如果 age < 18，返回 400 错误，detail 是 "User is under 18"。
#   6. 否则返回：

#   {
#     "user_id": "请求里的 user_id",
#     "message": "用户 name 已通过校验",
#     "valid": true
#   }


from faseapi import FastAPI,HttpException
from pydantic import BaseModel

app = FastAPI()

class UserRequest (BaseModel):
    user_id: str
    name: str
    age: int

class UserResponse (BaseModel):
    user_id: str
    message: str
    valid: bool

@app.post("/users/check", response_model=UserResponse)
def check(user: UserRequest):
    if user.age < 18:
        raise HttpException(status_code=400, detail="User is under 18")
    return {
        "user_id": user.user_id,
        "message": f"用户 {user.name} 已通过校验",
        "valid": True
    }
