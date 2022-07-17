import streamlit as st
import pandas as pd
import numpy as np

########################################Text elements##########################################################################
st.title('Guide')

st.header("header")
st.subheader("subheader")
st.caption("caption")

st.write('''st.write:  La "comilla triple" nos permite insertar un string con todas 
las líneas que deseemos. Basta que enmarquemos un bloque de texto entre 
comillas triples (da igual si son simples o dobles) y Python respetará 
        el aspecto y formato completo del texto.''')

st.markdown('Markdown... Streamlit is **_really_ cool**.')
st.markdown('Markdown... Streamlit is **_really_ cool**.')

code = '''def hello():
     print("Hello, Streamlit!")'''
st.code(code, language='python')

st.text('Write fixed-width and preformatted text.')

# r de raw string
st.latex(r''' 
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

##################################### DATA display elements#####################################################


df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

#Tablas estáticas:

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))

st.table(df)


#Formato de ciertas unidades

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")


#Embellecer json
st.json({
     'foo': 'bar',
     'baz': 'boz',
     'stuff': [
         'stuff 1',
         'stuff 2',
         'stuff 3',
         'stuff 5',
     ],
 })


###############################################Chart elements###############################################


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#Barchart
chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=["a", "b", "c"])

st.bar_chart(chart_data)

###### map
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])

st.map(df)


############################################ Widgets de entrada  #############################################################

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

#Para descargar csv...
"""
@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

csv = convert_df(my_large_df)

st.download_button(
     label="Download data as CSV",
     data=csv,
     file_name='large_df.csv',
     mime='text/csv',
 )"""

#checkbox
agree = st.checkbox('I agree')

if agree:
     st.write('Great!')

#redio button
genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")


#Selectbox
option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

#Multiselect the
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

#Slider 
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

#text input
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

#number Inputnumber = st.number_input('Insert a number')
number = st.number_input('Insert a number')
st.write('The current number is ', number)

#Color input
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)


############################################Subir imagen#################
from PIL import Image
#image = Image.open('sunrise.jpg')

#st.image(image, caption='Sunrise by the mountains')

################################################Layouts and containers##############################################

st.sidebar.markdown("## Controls")


col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    

with col2:
    st.header("A dog")
    

with col3:
    st.header("An owl")


#tabs
tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)

tab1.subheader("A tab with a chart")
tab1.line_chart(data)

tab2.subheader("A tab with the data")
tab2.write(data)

#Expander

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
     st.write("""
         The chart above shows some numbers I picked for you.
         I rolled actual dice for these, so they're *guaranteed* to
         be random.
     """)
     st.image("https://static.streamlit.io/examples/dice.jpg")



#Container 
with st.container():
    st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")


#Empty

import time

with st.empty():
     for seconds in range(60):
         st.write(f"⏳ {seconds} seconds have passed")
         time.sleep(1)
     st.write("✔️ 1 minute over!")


###############################################################################################################