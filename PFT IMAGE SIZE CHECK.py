#%%
import cv2
import os
import pandas as pd

#%%
def print_files_in_dir(root_dir, prefix):
    files = os.listdir(root_dir)
    for file in files:
        path = os.path.join(root_dir, file)
#         print(prefix + path)
        if os.path.isdir(path):
            print_files_in_dir(path, prefix + "    ")
#         print(path)
        filedir.append(path) # 하위폴더의 세부 파일경로를 리스트에 저장

#%%
for year in range(2007,2021):
    year = year
    filedir = []

    if __name__ == "__main__":
        root_dir = "K:/PFT_IMAGE_DATA/{}".format(year)
        # root_dir = "W:\PWV_deID_IMAGE\CASE_TEST\TEST6-1"
        print_files_in_dir(root_dir, "")

    filelist = [filedir for filedir in filedir if '.JPG' in filedir.upper()]
    
    imginfo = pd.DataFrame()

    for file in filelist:

        # 원본 이미지가 손상된 경우는 pass
        try:
            img = cv2.imread(file,cv2.IMREAD_COLOR) # default값이 color지만, 확실히 지정하는게 필요함.
            y, x, l = img.shape
        except AttributeError:
            pass

        ptno = file[len(root_dir)+6:len(root_dir)+6+8]
#         ptno = file[len(root_dir)+2:len(root_dir)+6+8]

        CDW_NO = trns_ptno(ptno)

        remain = file[len(root_dir)+6+8:]

        # img = root_dir_save+CDW_NO+remain
        img = CDW_NO+remain

        input_value = {'A_YEAR': str(year)
                      ,'B_IMG': img
                      ,'C_IMG_Y': str(y)
                      ,'D_IMG_X': str(x)
                      ,'E_IMG_L': str(l)
                      }

        imginfo = imginfo.append(input_value, ignore_index=True)
    
    imginfo.to_excel("savd dir/imginfo_{}.xlsx".format(year), index=False)
    year += 1

#%%

