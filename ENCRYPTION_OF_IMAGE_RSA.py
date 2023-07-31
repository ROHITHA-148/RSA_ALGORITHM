#ENCRYPTION OF IMAGE USING PYTHON(RSA ALGORITHM)
#importing required libs
from tkinter import*
from tkinter import messagebox
from PIL import Image 
import PIL 
import numpy as np
import time

global msg
global flag
def login():
    username=entry1.get()
    password=entry2.get()
    if username=="" and password=="":
        msg=messagebox.showinfo("","Blank Not Allowed,username and password must be filled") 
    elif username=="":
        msg=messagebox.showinfo("","Blank Not Allowed,User name must be filled!")
    elif password=="":
        msg=messagebox.showinfo("","Blank Not Allowed,password must be filled")  
    

    elif username=="rohitha" and password=="123":
        msg=messagebox.showinfo("","login success")
        #taking input from the user to select an image
        n=str(input('Choose a number \n1 Taj Mahal\n2 Sastra University\n3 India map \n4\n'))
        if n=="1":
          print('You have chosen 1 Taj Mahal\n')
          #converting the original RGB image to greyscale using the .convert() and 'L' argument
          ori_img = (Image.open('original_image_1.jpeg').convert('L'))
          #showing the image that will be encrypted 
          ori_img.show()
          img = np.array(Image.open('original_image_1.jpeg').convert('L'))
          #converting the uint8 type numpy.ndarray to uint32 type
          img32 = np.array(img, dtype=np.uint32) 

        if n=="2":
          print('You have chosen 2 Sastra University\n')
          #converting the original RGB image to greyscale using the .convert() and 'L' argument
          ori_img = (Image.open('original_image_2.jpeg').convert('L'))
          #showing the image that will be encrypted
          ori_img.show() 
          img = np.array(Image.open('original_image_2.jpeg').convert('L'))
          #converting the uint8 type numpy.ndarray to uint32 type
          img32 = np.array(img, dtype=np.uint32) 

        if n=="3":
          print('You have chosen 3 India map\n')
          #converting the original RGB image to greyscale using the .convert() and 'L' argument
          ori_img = (Image.open('original_image_3.jpeg').convert('L'))
          #showing the image that will be encrypted
          ori_img.show()
          img = np.array(Image.open('original_image_3.jpeg').convert('L'))
          #converting the uint8 type numpy.ndarray to uint32 type
          img32 = np.array(img, dtype=np.uint32)
        if n=="4":
          print('You have chosen 4 \n')
          #converting the original RGB image to greyscale using the .convert() and 'L' argument
          ori_img = (Image.open('original_image_4.png').convert('L'))
          #showing the image that will be encrypted
          ori_img.show()
          img = np.array(Image.open('original_image_4.png').convert('L'))
          #converting the uint8 type numpy.ndarray to uint32 type
          img32 = np.array(img, dtype=np.uint32)
      
        #counting the no of rows and cols 
        a,b = img.shape  
        print('\n\nOriginal image matrix: ')
        print(img32)
        print((a,b))
        # store the number of rows and cols into a tuple
        tup = a,b
        flag=1
        #encryption
        while flag==1:
         s= str(input('DO YOU WANT TO ENCRYPT THE IMAGE ? (TYPE "YES" OR "NO") '))
         if s=="YES":
              #RSA algorithm implementation
              for i in range (0, tup[0]): #going through row 0 to the last row of the matrix 
               for j in range (0, tup[1]): #going through col 0 to the last col of the matrix
                x = img32[i][j] #storing the value of the element into a temp variable x
                x = (pow(x,3)%25777) #applying rsa keys 
                img32[i][j] = x #storing back the values to the original matrix from temp variable
              print('\n\nAfter using RSA algorithm: ')
              print(img32) 
              encrypted_img= Image.fromarray(img32) #making an image from the matrix
              encrypted_img.show() #showing the encrypted image
          #decryption
              img_en_32 = img32 
              #converting RSA matrix into uint32
              img_en_32 = np.array(img, dtype=np.uint32)
              #printing the encrypted image's matrix 
              print('\n\nEncrypted matrix: ')
              print(img_en_32)
              #counting the no of rows and cols
              a1,b1 = img_en_32.shape
              print((a1,b1))
              print('\nImage is successfully encrypted using RSA algorithm.\n')
              tup1 = a1,b1
              11
         elif s=="NO":
              print("YOU CHOSE NO")
              flag=0
         else :
              print("INVALID INPUT!! TRY AGAIN.")
        #decryption
         if s=="YES": 
           st= str(input('DO YOU WANT TO DECRYPT THE IMAGE ? (TYPE "YES" OR "NO")'))
           if st=="YES":
                 for i1 in range (0, tup1[0]):
                   for j1 in range (0, tup1[1]):
                       x1 = img_en_32[i1][j1] 
                       x1 = (pow(x,16971)%25777) 
                       img_en_32[i][j] = x1
                 #printing the decrypted image's matrix 
                 print('\n\nDecrypted matrix: ')
                 print(img_en_32)
                 #counting the no of rows and cols
                 a2,b2 = img_en_32.shape
                 print((a2,b2))
                 decrypted_img = Image.fromarray(img_en_32)
                 decrypted_img.show()  #showing the decrypted image
                 flag=0
                 print('\n Image is successfully decrypted\n')
                 tup1 = a2,b2
           elif st=="NO":
                 print("YOU CHOSE NO")
                 flag=0
           else :
                 print("INVALID INPUT")
                 flag=0 

    else:
       msg=messagebox.showinfo("","incorrect username and password")
       
    

root=Tk()
root.title("Login")
root.geometry("300x200")

global entry1
global entry2

Label(root,text="Username").place(x=20,y=20)
Label(root,text="Password").place(x=20,y=70)

entry1=Entry(root,bd=5)
entry1.place(x=140,y=20)

entry2=Entry(root,bd=5)
entry2.place(x=140,y=70)

Button(root,text="Login",command=login,height=3,width=13,bd=6).place(x=100,y=120)
root.mainloop()

 