import streamlit as st
import time

st.title('streamlit 超入門')

st.title('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()#何も書いていない
bar = st.progress(0)

for i in range(100):
	latest_iteration.text(f'Iteration{i+1}')#fstring
	bar.progress(i+1)
	time.sleep(0.1)#0.1秒スリープする

# st.write('DataFrame')

# df = pd.DataFrame(
# 	np.random.rand(20,3),#20行3列の乱数を正規分布から生成する
# 	columns =['a','b','c']
# )

# st.write('st.write(df)')
# st.write(df)

# st.write('st.dataframe(df)：表のサイズをpxで指定できる。')
# st.dataframe(df.style.highlight_max(axis=0),width=300,height=300)

# st.write('静的な表を表示したいときは、tableを使う')
# st.table(df.style.highlight_max(axis=0))

# """
# ### マークダウン記法を適用することができる
# ```python
# import streamlit as st 
# import numpy as np 
# import pandas as pd 
# ```

# なんてこっちゃ。
# """

# """
# ### 折れ線グラフを書く
# """

# st.line_chart(df)

# st.area_chart(df)

# st.bar_chart(df)


# df2 = pd.DataFrame(
# 	np.random.rand(100,2)/[50,50] + [35.69,139.70],
# 	columns=['lat','lon']
# )

# st.map(df2)

# st.write('Interactive Widgets')

# left_column, right_column = st.beta_columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
# 	right_column.write('ここは右カラムです')

# expander = st.beta_expander('問い合わせ')
# expander.write('問い合わせ内容を書く')
# expander.write('問い合わせ内容を書く')
# expander.write('問い合わせ内容を書く')

# st.color_picker("色を選んでください","#D28383")


# option_t = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味は、',option_t,'です'
# 'あなたのコンディションは、',condition,'です'

option = st.selectbox(
	'あなたが好きな数字を教えてください、',
	list(range(1,11))
)

'あなたの好きな数字は、',option,'です'

if st.checkbox('Show Image'):
	img = Image.open('img.jpg')
	st.image(img, caption="サンプル画像", use_column_width=True)#横幅にあわせて表示する

