import random


class VerificationCodeIterator:
    """
    一个能无限生成四位验证码的迭代器类
    """

    def __init__(self):
        # 初始化时只准备状态，不生成具体数据
        print(">>> [系统] 迭代器已启动，准备就绪...")

    def __iter__(self):
        # 返回迭代器对象本身，这是标准协议
        return self

    def __next__(self):
        # 每次调用 next() 时，才现场计算一个新的验证码
        # 体现了“按需取值”的特性
        code = random.randint(1000, 9999)
        return code


# --- 主程序逻辑 ---

# 1. 创建迭代器对象（此时还没生成验证码）
ver_generator = VerificationCodeIterator()

# 2. 获取第一个验证码（触发 __next__，真正开始计算）
current_code = next(ver_generator)
print(f"生成的初始验证码是: {current_code}")

# 3. 进入验证循环
while True:
    try:
        user_input = int(input("请输入验证码: "))

        if user_input == current_code:
            print("✅ 验证成功！")
            break
        else:
            print("❌ 验证码错误，请重试。")
            # 【关键点】：如果用户输错了，我们可以选择是否生成新验证码
            # 这里演示迭代器的用法：调用 next() 获取下一个新值
            current_code = next(ver_generator)
            print(f"💡 提示：验证码已更新为 {current_code} (仅作演示用)")

    except ValueError:
        print("⚠️ 请输入有效的数字。")
