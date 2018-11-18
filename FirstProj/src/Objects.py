'''
Created on Nov 18, 2018

@author: Mgmi
'''


def valIdentity() :
    p=[1,2,3]
    q=p
    print ('identity of p:', id(p), ' identity of q: ', id(q), 'Value equality: ', p==q, '  Reference equality:', p is q)
    q=[1,2,3]
    print ('identity of p:', id(p), ' identity of q: ', id(q), 'Value equality: ', p==q, '  Reference equality:', p is q)
 

if __name__=='__main__':
    valIdentity()