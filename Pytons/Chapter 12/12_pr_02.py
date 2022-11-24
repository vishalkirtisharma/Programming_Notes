from email.encoders import encode_noop


a=[1,2,3,4,5,6,7,87,9]

for i,a in enumerate(a):
    if i == 2 or i== 4 or i== 6:
        print(a)