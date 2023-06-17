import os, shutil, sys
import numpy as np
from tqdm.auto import tqdm

##########################################
##########################################
### 나눌 데이터가 있는 폴더의 경로 입력 ###
path = '180.동의보감 약초 이미지 AI데이터/01.데이터/1.Training/원천데이터/Temp(cls_list)/잎/' # Temp값은 for문 안에서 변경됨

cls_list = ['가는장구채', '맑은대쑥', '분홍장구채', '왕자귀나무', '자귀나무', '장구채', '제비쑥', '진득찰', '털진득찰'] # 접두사(TS_ | VS_) 제외하고 자신의 class 폴더 이름 입력 ex) ['곰취', '참취', '개오동', '꽃개오동']
### 저장될 폴더의 경로 입력 ###
save_path = 'qwer/'
# gogo = ['train/', 'test/']
##########################################
##########################################

move_rate = 0.2 # test 나눌 비율
for class_name in cls_list:
    current_path = path.split("/")
    current_path[4] = "TS_" + class_name
    current_path = "/".join(current_path)
    print(current_path)
    print(save_path)
    
    data_path = current_path if current_path[-1] == '/' else current_path + '/'
    splited_path = save_path if save_path[-1] == '/' else save_path + '/'
    train_save_path = splited_path + 'train/' + class_name
    test_save_path = splited_path + 'test/' + class_name
    if os.path.isdir(train_save_path) == False:
        os.makedirs(train_save_path)
        
    if os.path.isdir(test_save_path) == False:
        os.makedirs(test_save_path)


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

    print(f"전체 데이터 개수: {data_count}\n")
    print(f"최종 train 데이터 개수: {len(os.listdir(train_save_path))}")
    print(f"최종 test 데이터 개수: {len(os.listdir(test_save_path))}")