from PIL import Image, ImageDraw, ImageFont

def text_to_matrix(text, font_size=15):
    # 創建一個16x16的圖像
    image = Image.new('1', (16, 16), color=1)
    draw = ImageDraw.Draw(image)

    # 設置字體和大小
    font = ImageFont.truetype("GenShinGothic-Normal.ttf", font_size)

    # 在圖像上繪製文字
    draw.text((0, 0), text, font=font, fill=0)

    # 將圖像轉換為矩陣
    matrix = list(image.getdata())

    # 將一維矩陣轉換為二維矩陣
    matrix = [matrix[i:i + 16] for i in range(0, len(matrix), 16)]

    return matrix

# 使用範例
chinese_text = "安"
matrix = text_to_matrix(chinese_text)

# 輸出矩陣，每欄陣列結束後換行
for row in matrix:
    print(row)
