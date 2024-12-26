import sqlite3
from tabulate import tabulate


class Library:
    def __init__(self, db_name):
        self.db_name = db_name  # 初始化数据库名称

    def connect_db(self):
        # 连接到数据库
        return sqlite3.connect(self.db_name)

    def add_book(self, status="可借"):
        """
        添加图书到数据库
        :param book_id: 书号
        :param title: 书名
        :param publisher: 出版社
        :param author: 作者
        :param status: 图书状态，默认值为 "可借"
        """
        conn = self.connect_db()
        cursor = conn.cursor()
        book_id = input("请输入书号: ")
        if not book_id:
            print("书号不能为空！")
            return
        row = self.get_book(book_id, cursor)
        if row:
            print("该图书已存在！！！")
            return  # 如果图书已存在，则不添加
        title = input("请输入书名: ")
        publisher = input("请输入出版社: ")
        author = input("请输入作者: ")
        # 插入新图书记录到 books 表
        cursor.execute('''
            INSERT INTO books (book_id, title, publisher, author, status) 
            VALUES (?, ?, ?, ?, ?)
        ''', (book_id, title, publisher, author, status))

        # 提交事务并关闭连接
        conn.commit()
        conn.close()
        print("图书信息已录入。")

    def get_book(self, book_id, cursor):
        cursor.execute('SELECT * FROM books WHERE book_id = ?', (book_id,))
        row = cursor.fetchone()
        return row

    def find_book(self, book_id):
        """
        查找指定书号的图书
        :param book_id: 书号
        :return: 如果找到，返回图书信息；否则返回 None
        """
        conn = self.connect_db()
        cursor = conn.cursor()

        # 查找图书
        row = self.get_book(book_id, cursor)
        conn.close()

        if row:
            # 格式化输出为表格形式
            headers = ["书号", "书名", "出版社", "作者", "当前状态", "借阅次数"]
            table = [row]
            print(tabulate(table, headers, tablefmt="grid"))  # 使用grid格式输出
        else:
            print("未找到该图书。")

        return row if row else None  # 如果图书存在，返回图书信息，否则返回 None

    def update_book(self):
        """
        修改图书信息
        :param book_id: 书号
        :param title: 新书名（可以为空，不修改）
        :param publisher: 新出版社（可以为空，不修改）
        :param author: 新作者（可以为空，不修改）
        """
        conn = self.connect_db()
        cursor = conn.cursor()
        book_id = input("请输入要修改的书号: ")
        # 查找图书是否存在
        row = self.get_book(book_id, cursor)
        if not row:
            print("图书不存在")
            return

        # 检查图书是否已经借出，已借出的图书不能修改
        if row[4] == "已借":
            print("图书已被借出，无法修改")
            return
        title = input("请输入新的书名（为空则不修改）: ")
        publisher = input("请输入新的出版社（为空则不修改）: ")
        author = input("请输入新的作者（为空则不修改）: ")
        # 如果有需要修改的字段，则执行更新操作
        if title:
            cursor.execute('UPDATE books SET title = ? WHERE book_id = ?', (title, book_id))
        if publisher:
            cursor.execute('UPDATE books SET publisher = ? WHERE book_id = ?', (publisher, book_id))
        if author:
            cursor.execute('UPDATE books SET author = ? WHERE book_id = ?', (author, book_id))

        # 提交事务并关闭连接
        conn.commit()
        conn.close()

    def borrow_book(self):
        """
        借阅图书
        :param book_id: 书号
        :param student_id: 学号
        """
        conn = self.connect_db()
        cursor = conn.cursor()
        book_id = input("请输入书号: ")
        # 查找图书是否存在
        row = self.get_book(book_id, cursor)
        if not row:
            print("图书不存在")
            return

        # 检查图书是否已经借出
        if row[4] == "已借":
            print("图书已被借出")
            return
        student_id = input("请输入学号: ")
        # 更新图书状态为已借，并增加借阅次数
        cursor.execute('UPDATE books SET status = ?, borrow_count = borrow_count + 1 WHERE book_id = ?',
                       ("已借", book_id))

        # 在 borrow_records 表中插入借阅记录
        cursor.execute('INSERT INTO borrow_records (book_id, student_id, action) VALUES (?, ?, ?)',
                       (book_id, student_id, "借阅"))

        # 提交事务并关闭连接
        conn.commit()
        conn.close()
        print(f"图书《{book_id}》已借出")

    def return_book(self):
        """
        归还图书
        :param book_id: 书号
        :param student_id: 学号
        """
        conn = self.connect_db()
        cursor = conn.cursor()
        book_id = input("请输入书号: ")
        # 查找图书是否存在
        row = self.get_book(book_id, cursor)
        if not row:
            print("图书不存在")
            return

        # 检查图书是否已经被借出
        if row[4] == "可借":
            print("图书未被借出")
            return
        student_id = input("请输入学号: ")
        # 更新图书状态为可借
        cursor.execute('UPDATE books SET status = ? WHERE book_id = ?', ("可借", book_id))

        # 在 borrow_records 表中插入归还记录
        cursor.execute('INSERT INTO borrow_records (book_id, student_id, action) VALUES (?, ?, ?)',
                       (book_id, student_id, "归还"))

        # 提交事务并关闭连接
        conn.commit()
        conn.close()
        print(f"图书《{book_id}》已归还")

    def display_books(self):
        """
        显示所有图书信息
        """
        conn = self.connect_db()
        cursor = conn.cursor()

        # 查询所有图书
        cursor.execute('SELECT * FROM books')
        rows = cursor.fetchall()

        # 检查是否有图书信息
        if rows:
            # 输出所有图书信息
            headers = ["书号", "书名", "出版社", "作者", "当前状态", "借阅次数"]
            print(tabulate(rows, headers, tablefmt="grid", stralign="center"))  # 使用grid格式输出，居中对齐
        else:
            print("暂无图书信息。")

        # 关闭数据库连接
        conn.close()

    def rank_books(self):
        """
        显示借阅次数最多的前 5 本图书
        """
        conn = self.connect_db()
        cursor = conn.cursor()

        # 根据借阅次数排序，显示前 5 本借阅次数最多的图书
        cursor.execute('SELECT * FROM books ORDER BY borrow_count DESC LIMIT 5')
        rows = cursor.fetchall()

        # 输出借阅次数最多的图书
        if rows:
            # 输出所有图书信息
            headers = ["书号", "书名", "出版社", "作者", "当前状态", "借阅次数"]
            print(tabulate(rows, headers, tablefmt="grid", stralign="center"))  # 使用grid格式输出，居中对齐
        else:
            print("暂无图书信息。")

        # 关闭数据库连接
        conn.close()

    def delete_book(self, book_id):
        """
        删除指定书号的图书
        :param book_id: 书号
        """
        conn = self.connect_db()
        cursor = conn.cursor()

        # 删除图书
        cursor.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
        conn.commit()

        # 确认删除
        if cursor.rowcount > 0:
            print(f"图书 {book_id} 已成功删除。")
        else:
            print(f"图书 {book_id} 不存在，无法删除。")

        conn.close()

    def view_borrow_records(self):
        """
        查看所有借阅记录
        """
        conn = self.connect_db()
        cursor = conn.cursor()

        # 查询所有借阅记录
        cursor.execute('SELECT * FROM borrow_records order by time desc')
        rows = cursor.fetchall()

        # 检查是否有借阅记录
        if rows:
            # 输出借阅记录
            headers = ["记录ID", "书号", "学号", "操作", "时间"]
            print(tabulate(rows, headers, tablefmt="grid", stralign="center"))  # 使用grid格式输出，居中对齐
        else:
            print("暂无借阅记录。")

        # 关闭数据库连接
        conn.close()
