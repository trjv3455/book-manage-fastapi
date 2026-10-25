from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="图书管理后端接口")

# 内存模拟数据库
book_db = [
    {"id":1, "name":"物联网原理", "author":"张三", "is_borrow":False},
    {"id":2, "name":"Python编程", "author":"李四", "is_borrow":False}
]

# 数据校验模型
class Book(BaseModel):
    name: str
    author: str
    is_borrow: Optional[bool] = False

# 获取全部图书
@app.get("/books", response_model=List[Book])
def get_all_books():
    return book_db

# 根据id查询单本图书
@app.get("/books/{book_id}")
def get_book(book_id:int):
    for b in book_db:
        if b["id"] == book_id:
            return b
    return {"msg":"图书不存在"}

# 新增图书
@app.post("/books")
def add_book(book: Book):
    new_id = max(item["id"] for item in book_db) + 1
    new_book = {
        "id": new_id,
        "name": book.name,
        "author": book.author,
        "is_borrow": book.is_borrow
    }
    book_db.append(new_book)
    return {"msg":"新增成功", "data": new_book}

# 修改图书信息
@app.put("/books/{book_id}")
def update_book(book_id:int, book:Book):
    for b in book_db:
        if b["id"] == book_id:
            b["name"] = book.name
            b["author"] = book.author
            b["is_borrow"] = book.is_borrow
            return {"msg":"修改成功", "data":b}
    return {"msg":"图书不存在"}

# 删除图书
@app.delete("/books/{book_id}")
def del_book(book_id:int):
    global book_db
    for b in book_db:
        if b["id"] == book_id:
            book_db.remove(b)
            return {"msg":"删除成功"}
    return {"msg":"图书不存在"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
