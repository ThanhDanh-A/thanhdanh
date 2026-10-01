"""
Bài tập 03: In hoa văn bằng vòng lặp lồng 🎨
===============================================
Mục tiêu: Thành thạo nested loops
"""

# TODO 1: In tam giác vuông cao n dòng
# n = 5:
# *
# **
# ***
# ****
# *****
n = 5
print("--- Tam giác vuông ---")
for i in range(1, n + 1):
    print("*" * i)

# TODO 2: In tam giác cân cao n dòng (căn giữa)
# n = 5:
#     *
#    ***
#   *****
#  *******
# *********
print("\n--- Tam giác cân ---")
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# TODO 3: In hình kim cương cao n dòng (n lẻ)
# n = 5:
#   *
#  ***
# *****
#  ***
#   *
print("\n--- Kim cương ---")
mid = (n + 1) // 2  # Dòng đỉnh tới hàng giữa
# Nửa trên
for i in range(1, mid + 1):
    print(" " * (mid - i) + "*" * (2 * i - 1))
# Nửa dưới
for i in range(mid - 1, 0, -1):
    print(" " * (mid - i) + "*" * (2 * i - 1))

# TODO 4 (Thử thách): In bàn cờ n x n
# n = 4:
# ■ □ ■ □
# □ ■ □ ■
# ■ □ ■ □
# □ ■ □ ■
print("\n--- Bàn cờ 4x4 ---")
board_size = 4
for r in range(board_size):
    for c in range(board_size):
        if (r + c) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()