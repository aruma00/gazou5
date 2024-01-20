import cv2

# 画像を読み込む
contour_image_path = '1.jpg'
binary_image_path = '2.jpg'

binary_image = cv2.imread(binary_image_path)
Canny_Edges = cv2.imread(contour_image_path)

# 画像を合成する
alpha = 0.5  # 重みづけの係数 (0.0から1.0の範囲で調整)
combined_image = cv2.addWeighted(binary_image, alpha, Canny_Edges, 1 - alpha, 0)

# 保存する
output_image_path = '3.jpg'
cv2.imwrite(output_image_path, combined_image)
