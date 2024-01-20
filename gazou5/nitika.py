import cv2

# 画像を読み込む
input_image_path = 'gandam.jpg'
original_image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

# 二値化する（例：単純な閾値処理）
_, binary_image = cv2.threshold(original_image, 128, 255, cv2.THRESH_BINARY)

# 保存する
output_image_path = '2.jpg'
cv2.imwrite(output_image_path, binary_image)
