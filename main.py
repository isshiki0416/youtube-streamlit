import streamlit as st
import time

st.title("streamlit 入門")

st.write("プログレスバーの表示")
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i + 1}')
  bar.progress(i + 1)
  time.sleep(0.1)

"Done!!"

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
  right_column.write("ここは右カラムです")

expamder = st.expander("問い合わせ")
expamder.write("問い合わせ内容")
# text = st.text_input("あなたの趣味を教えてください")
# condition = st.slider("あなたの調子は?",0,10,5)

# "趣味:",text,"です"
# "コンディション:",condition,"です"

# if st.checkbox('Show Image'):
#   img = Image.open('sample.png')
#   st.image(img, caption="otonashi hito",use_column_width=True)
# df = pd.DataFrame(
#   np.random.rand(100,2)/[50,50]+[35.69,139.70],
#   columns=['lat','lon']
# )

# st.map(df)

# st.dataframe(df.style.highlight_max(axis=0), width=250, height=00)
# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """