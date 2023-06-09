import os, shutil, sys
import numpy as np
from tqdm.auto import tqdm

##########################################
##########################################
### 나눌 데이터가 있는 폴더의 경로 입력 ###
data_path = 'real_data/01.데이터/참취/train/잎'

### 저장될 폴더의 경로 입력 ###
save_path = 'real_data/01.데이터/참취/'
##########################################
##########################################

data_path = data_path if data_path[-1] == '/' else data_path + '/'
splited_path = save_path if save_path[-1] == '/' else save_path + '/'
train_save_path = splited_path + 'train_split'
test_save_path = splited_path + 'test_split'
os.makedirs(train_save_path)
os.makedirs(test_save_path)

move_rate = 0.2 # 옮길 비율

## 데이터 불러오기
data_list = os.listdir(data_path)
data_count = len(data_list)
print(f'불러온 데이터 중 10개\
      \n{[data for data in data_list[:10]]}\
      \n데이터 개수: {data_count}\n')

## split 설정
split_rate = move_rate
split_count = round(data_count * split_rate)
print(f'test 데이터의 비율: {split_rate}\n옮길 개수: {split_count}\n')
move_index = list(map(int, np.linspace(0, data_count-1, split_count)))
print(f'이동할 인덱스 {move_index}\n')

## 데이터 번호순으로 정렬
print(f"정렬 전\n {[data for data in data_list[:10]]}\n")
data_list.sort()
print(f"정렬 후\n {[data for data in data_list[:20]]}\n")

## 원본 데이터 유지한채로 train, test 나눠서 이동(복사)
move_data_list = []
for idx in move_index:
    move_data_list.append(data_list[idx])
for count, idx in enumerate(move_index):
    idx -= count
    data_list.pop(idx)


for data in tqdm(data_list):
    shutil.copy(data_path + data, train_save_path)
for data in tqdm(move_data_list):
    shutil.copy(data_path + data, test_save_path)

print(f"최종 train 데이터 개수: {len(os.listdir(train_save_path))}")
print(f"최종 test 데이터 개수: {len(os.listdir(test_save_path))}")