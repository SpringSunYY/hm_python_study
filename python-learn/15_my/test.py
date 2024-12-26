class Solution:
    def __init__(self):
        # 初始化结果列表和数字到字母的映射
        self.res = []
        self.letter_map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letter_combinations(self, digits: str):
        # 如果输入为空，直接返回空结果
        if not digits:
            return []
        # 调用递归函数，从第 0 个数字开始处理
        self.find_combination(digits, 0, [])
        return self.res

    def find_combination(self, digits: str, index: int, current: list):
        # 递归终止条件：当处理的索引等于数字长度时，组合完成
        if index == len(digits):
            # 将当前组合加入结果列表
            self.res.append(''.join(current))
            return

        # 获取当前数字对应的字母
        letters = self.letter_map[int(digits[index])]
        # 遍历数字对应的每一个字母
        for letter in letters:
            current.append(letter)  # 添加当前字母
            self.find_combination(digits, index + 1, current)  # 递归处理下一个数字
            current.pop()  # 回溯，移除当前字母


# 测试代码
if __name__ == "__main__":
    solution = Solution()
    result = solution.letter_combinations("23")
    for combination in result:
        print(combination)
