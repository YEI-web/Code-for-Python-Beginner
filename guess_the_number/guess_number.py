import random


def play_round():
    """
    玩一轮猜数字。
    电脑随机生成 0~9 的整数，用户输入猜测。
    猜对返回 1 分，猜错返回 0 分，并揭示答案。
    """
    # 随机生成一个 0 到 9 的整数（包含 0 和 9）
    answer = random.randint(0, 9)

    # 让用户输入猜测，int() 把文字转成整数
    while True:
        guess_str = input("请猜一个 0~9 的数字: ")

        # 验证输入是否为合法整数
        if not guess_str.isdigit():
            print("输入无效，请输入一个数字！")
            continue

        guess = int(guess_str)

        # 验证数字是否在合法范围
        if guess < 0 or guess > 9:
            print("数字必须在 0~9 之间！")
            continue

        break

    # 判断对错
    if guess == answer:
        print(f"🎉 恭喜猜对了！答案就是 {answer}，+1 分！")
        return 1
    else:
        print(f"😢 猜错了，答案是 {answer}。本轮得 0 分。")
        return 0


def main():
    """游戏主入口：管理总分和是否再来一局"""
    print("=" * 40)
    print("       欢迎来到《猜数字小游戏》")
    print("       规则：猜 0~9 中的一个数字")
    print("       猜对 +1 分，猜错结算总分")
    print("=" * 40)

    total_score = 0  # 累计总分
    round_count = 0  # 已玩回合数

    # 外层循环：控制是否再来一局
    while True:
        round_count += 1
        print(f"\n--- 第 {round_count} 关 ---")

        # 玩一轮，拿到得分
        score = play_round()
        total_score += score

        # 如果本轮猜错，游戏结束并显示总分
        if score == 0:
            print(f"\n🏁 游戏结束！共玩了 {round_count} 关，总分：{total_score} 分")

            # 询问是否重新开始
            choice = input("再来一次？(y/n): ").strip().lower()
            if choice == "y":
                total_score = 0
                round_count = 0
                print("\n🔄 好的，重新开始！\n")
            else:
                print("👋 再见！")
                break
        else:
            # 猜对了可以继续猜下一轮
            print(f"当前总分：{total_score} 分，继续挑战下一关！")


# 当这个文件被直接运行时，执行 main()
# （如果被其它文件 import，main() 不会自动执行）
if __name__ == "__main__":
    main()
