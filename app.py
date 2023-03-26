import streamlit as st

def getChessSquareColor(row: int, column: int) -> str:
        sum_row_colum = row + column
        if sum_row_colum % 2 == 0:
            return 'white'
        else:
            return 'black'
	

st.title(" First Calculator App :smile: ")

num_1 = st.number_input("Please enter a number",min_value=0,max_value=7,step=1,key=1)
num_2 = st.number_input("Please enter a number",min_value=0,max_value=7,step=1,key=2)

result = getChessSquareColor(num_1,num_2)

st.write("The result is :game_die: ",result.upper())