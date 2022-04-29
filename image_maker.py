import time
import os
import numpy as np
from PIL import Image

print("Image making Process Start.")

start_time = time.time()

# 이미지 파일 개수를 정의
NUM_SAMPLES = 1000

# 결과 저장 폴더 생성
out_dir ="random_image"
if out_dir not in os.listdir():
    os.mkdir(out_dir)


for i in range(NUM_SAMPLES):
    name = str(time.time())[-7:] + ".png"

    # 랜덤 이미지를 생성하기 위해 사이즈를 정의합니다. 사이즈마저도 랜덤입니다.
    Xdim, Ydim = np.random.randint(100, 400, size=2)

    # 랜덤 이미지를 생성합니다.
    image = np.random.randint(256, size=(Xdim, Ydim, 3)).astype('uint8')

    # 결과물을 PIL Image 형태로 만듭니다.
    result = Image.fromarray(image)

    # 결과물 파일을 저장합니다.
    result.save(out_dir + "/" +name)

    # 이미지를 닫아줍니다.
    result.close()

print("Image Making Process Done.")

end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")