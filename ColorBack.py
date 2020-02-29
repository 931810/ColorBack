import cv2
#青色(FHD,PNG)に対応
def blue_back(F):
    img=cv2.imread(F,-1)
    C=120#閾値
    for i in range(1080):
        for j in range(1920):
            if (abs(img[i][j][0]-255)+img[i][j][1]+img[i][j][2]<C):
                img[i][j][3]=0
            else:
                img[i][j][3]=255
    return img
#緑色(FHD,PNG)に対応
def green_back(F):
    img=cv2.imread(F,-1)
    C=120#閾値
    for i in range(1080):
        for j in range(1920):
            if (abs(img[i][j][1]-255)+img[i][j][0]+img[i][j][2]<C):
                img[i][j][3]=0
            else:
                img[i][j][3]=255
    return img
#様々な色(FHD,PNG)に対応
def fullcolor_back(F):
    x=1919#1920-1
    y=1079#1080-1
    img=cv2.imread(F,-1)
    C=120#閾値
    Ave=[(int(img[0][0][0])+int(img[0][x][0])+int(img[y][0][0])+int(img[y][x][0]))//4,(int(img[0][0][1])+int(img[0][x][1])+int(img[y][0][1])+int(img[y][x][1]))//4,(int(img[0][0][2])+int(img[0][x][2])+int(img[y][0][2])+int(img[y][x][2]))//4]
    for i in range(1080):
        for j in range(1920):
            if (abs(img[i][j][0]-Ave[0])+abs(img[i][j][1]-Ave[1])+abs(img[i][j][2]-Ave[2])<C):
                img[i][j][3]=0
            else:
                img[i][j][3]=255
    return img
#読み込み
img=fullcolor_back('image_in.png')
#書き出し
cv2.imwrite('image_out.png',img)
