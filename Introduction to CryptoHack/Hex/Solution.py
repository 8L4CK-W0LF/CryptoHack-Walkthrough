#paste the flag without b or ''
print(bytes.fromhex('63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'))

'''
This is or code if you want to copy the flag a more easily
flag = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
decoded = bytes.fromhex(flag)
decoded = str(decoded)
decoded = decoded.replace('b','')
decoded = decoded.replace("'",'')
print(decoded)
'''
