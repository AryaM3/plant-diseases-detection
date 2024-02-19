import cv2
path=r'C:\Users\mahes\Desktop\gui\leaf.jpg'
image=cv2.imread(r'C:\Users\mahes\Desktop\gui\leaf.jpg')
window_name='image'
cv2.imshow(window_name,image)
cv2.waitKey(0)
cv2.destroyAllWindows()
