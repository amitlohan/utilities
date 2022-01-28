import glob
import numpy as np
import cv2

#sample=cv2.imread('sample.png')
#print(sample)

bg_col=np.array([255,255,255])
#bg_col=np.array([0,0,0])

white_paths = glob.glob('./input/*')

for white_path in white_paths:
    target=cv2.imread(white_path)
    target[np.all(target==bg_col,2)]=np.array([243,243,243])
    cv2.imwrite(white_path.replace('input','output'),target)
    
print("Done")
