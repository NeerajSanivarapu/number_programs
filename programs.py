import streamlit as st
# st.text_input('Name')
# st.number_input('PHNO')
# st.header('WELOME TO THE E15 BATCH')
# st.subheader(' i AM A SUB HEADER')
# st.title('I AM A TITLE')
# st.button('PRIME')
#=====================







st.title('NUMBER PROGRAMS')
st.image('images.jpg') # download the image in the same path where program file is present
no=st.number_input("ENTER THE NUMBER",min_value=0)
prime=st.button('PRIME',type='primary')
factorial=st.button('FACTORIAL',type='primary')
perfect_number=st.button('PERFECT NUMBER',type='primary')
if prime:
    for i in range(2,no):
        if no% i==0:
            st.error(f'{no}is not a prime number')
            break
    else:
        st.success(f'{no} is a prime number')
        st.balloons()
elif factorial:
    temp=no
    fact=1
    while no>0:
        fact=fact*no
        no=no-1
    st.success(f'factorial of {temp} is :{fact}')
elif perfect_number:
    sum=0
    for i in range(1,no):
        if no % i==0:
            sum+=i
    if sum==no:
        st.success('perfect number')
    else:
        st.error('not a perfect number')