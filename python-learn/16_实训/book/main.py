from library import Library
def menu():
    """
    显示系统操作菜单
    """
    print("""
    1. 录入图书信息
    2. 查找图书信息
    3. 删除图书信息
    4. 修改图书信息
    5. 图书借阅
    6. 图书归还
    7. 图书借阅热度排行
    8. 查看所有图书
    9. 查看所有借阅记录
    0. 退出系统
    """)


def main():
    """
    主函数，运行用户交互系统
    """
    library = Library("library.db")

    while True:
        menu()  # 显示菜单
        choice = input("请选择操作: ")

        if choice == "1":
            # 录入图书信息
            library.add_book()

        elif choice == "2":
            # 查找图书信息
            book_id = input("请输入要查找的书号: ")
            book = library.find_book(book_id)
            if book:
                # print(book)
                print()
            else:
                print("未找到该图书。")

        elif choice == "3":
            # 删除图书信息
            book_id = input("请输入要删除的书号: ")
            library.delete_book(book_id)

        elif choice == "4":
            # 修改图书信息
            library.update_book()

        elif choice == "5":
            # 图书借阅
            library.borrow_book()

        elif choice == "6":
            # 图书归还
            library.return_book()

        elif choice == "7":
            # 图书借阅热度排行
            library.rank_books()
        elif choice == "8":
            # 所有图书
            library.display_books()
        elif choice == "9":
            # 借阅记录
            library.view_borrow_records()

        elif choice == "0":
            # 退出系统
            print("退出系统。")
            break

        else:
            print("无效选择，请重新输入。")


if __name__ == "__main__":
    main()
