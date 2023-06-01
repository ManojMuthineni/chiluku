import streamlit as st
from PIL import Image
image= Image.open

col1, col2 = st.columns(2)

with col1:
   
   st.image("Snapchat-479589567.jpg",width=200)

with col2:
   st.header("Portfolio")
   st.write("NAME: Manoj Muttineni")
   st.markdown("Email : **:blue[manojmuthineni@gmail.com]**" )
   st.markdown("Phone : **:red[9989849723]**")


tab1, tab2, tab3, tab4, tab5 = st.tabs(["Carrier objective", "Techinical skills","Education","Projects","Languages"])

with tab1:
   st.write("A passionate and hardworking post graduate student in MBA specilization HR having knowledge in python,sql,machine learning,deep learning ability to learn new techologies and capable of working in teams by providing good valuable support and communicate with manner")
   

with tab2:
   st.write(" - Python")
   st.write(' - Sql')
   st.write(' - Tableau')
   st.write(' - statistics')
   st.write(' - Exploratory Data analysis')

with tab3:
   st.write(" - Vaagdevi institute of management and sciences-2023(CGPA - 6.3)")
   st.write(' - vaagdevi Degree and pg college-2020(per-69%)')
   st.write(' - Board of intermediate Education-2017(per-87%)')
   st.write(' - Board of secondary education-2015(per-82%)')

with tab4:
    st.write('TITLE:- Exploratoty data analysis on used box office mojo/IMDB pro')
    st.write('TECNOLOGIES:- Python')
    st.write('LIBRARIES AND MODULES:- Pandas,Numpy,selenium,Requests,BeautifulSoup,Matplotlib,Seaborn,Plotly')
    st.write('PLATFORM:- web Browser')   
    st.write('WEBSITE:- Box office mojo.com')

with tab5:
    st.write('- ENGLISH')
    st.write('- Telugu')

   




