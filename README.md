book-manage-fastapi
基于FastAPI开发简易图书管理后端，实现RESTful风格CRUD接口，自带自动交互式API文档，适合后端接口开发练习。

功能清单
- 查询全部图书、根据ID查询单本图书
- 新增图书信息
- 修改图书信息、借阅状态
- 删除图书
- 自动生成 Swagger 接口文档

技术栈
Python3，FastAPI，Pydantic，uvicorn
```bash
pip install -r requirements.txt

运行方式
python main.py

启动后访问自动文档：
- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

项目结构
├── main.py             # 接口主程序
├── requirements.txt     # 依赖列表
├── README.md
