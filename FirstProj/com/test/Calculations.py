'''
Created on Nov 18, 2018

@author: Mgmi
'''
import numpy as np

def main():
    
    #numarr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
    list_1=[1,2,3]
    list_2=[4,5,6]
    list_3=[7,8,9]
    numarr1 = np.array([list_1, list_2, list_3])
    numarr2=np.full((5,3),8)
    print(numarr2)

if __name__ == '__main__':
    main()