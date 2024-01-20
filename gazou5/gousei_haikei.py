import cv2
import numpy as np

def apply_screen_tone(image):
    # スクリーントーンの背景画像を読み込む（例：pattern.jpg）
    pattern_path = 'haikei4.jpg'
    pattern = cv2.imread(pattern_path)

    # 画像をグレースケールに変換
    pattern_gray = cv2.cvtColor(pattern, cv2.COLOR_BGR2GRAY)

    # 画像のサイズを合わせる
    h, w = image.shape[:2]
    pattern_resized = cv2.resize(pattern_gray, (w, h))

    # 画像を反転させてスクリーントーンにする
    inverted_pattern = cv2.bitwise_not(pattern_resized)

    # 輪郭画像を反転させる
    inverted_image = cv2.bitwise_not(image)

    # スクリーントーンを適用
    result = cv2.bitwise_and(inverted_image, inverted_image, mask=inverted_pattern)

    # 結果を反転させて元の向きに戻す
    result = cv2.bitwise_not(result)

    return result

# 合成画像を読み込む
composite_image_path = '3.jpg'
composite_image = cv2.imread(composite_image_path, cv2.IMREAD_GRAYSCALE)

# 背景をスクリーントーンに変換
result_image = apply_screen_tone(composite_image)

# 結果を保存
output_image_path = '4.jpg'
cv2.imwrite(output_image_path, result_image)
