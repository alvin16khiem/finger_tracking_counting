import cv2
import time
import os
import hand as htm

pTime = 0
cap = cv2.VideoCapture(0)

FolderPath = "Fingers"
lst=os.listdir(FolderPath) #listdir là hàm liệt kê file ra
lst_2 =[]
for i in lst: # vòng lặp từ i đến lst kiểu i<lst
    image=cv2.imread(f"{FolderPath}/{i}") #Fingers/1.png .....6.png
    print(f"{FolderPath}/{i}")
    lst_2.append(image)
#print(len(lst_2))
#print(lst_2[0].shape)

detecter = htm.handDetector(detectionCon=1)

fingerid = [4,8,12,16,20]
while True:
    ret, frame = cap.read()
    frame=detecter.findHands(frame)
    lmlist = detecter.findPosition(frame,draw=False) # phat hien vi tri
    print(lmlist)

    if len(lmlist) != 0:
        fingers = []

    # viet cho ngon cai ( điểm nằm bên trái hay là bên phải của điểm 3 )
        if lmlist[fingerid[0]][1] < lmlist[fingerid[0] - 1][1]:
            fingers.append(1)  # ngon dang mo
        else:
            fingers.append(0)  # ngon dang dong




    #viet cho ngon dai
    #số càng cao giá trị càng thấp
        for id in range(1,5):
            if lmlist[fingerid[id]][2] < lmlist[fingerid[id]-2][2]:
                fingers.append(1) # ngon dang mo
            else:
                fingers.append(0) # ngon dang dong

        print(fingers)
        tay = fingers.count(1)






    h,w,c = lst_2[0].shape
    frame[0:h,0:w] = lst_2[0]


    #vẽ chữ
    cv2.putText(frame, str(tay), (30, 390), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 5)

    # viet ra fps
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    print(fps)
    cv2.putText(frame,f"FPS:{int(fps)}",(150,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    cv2.imshow("show",frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release() # giải phóng camera
cv2.destroyAllWindows() # thoát tất cả cửa sổ

