import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pickle
import warnings
warnings.filterwarnings('ignore')
import streamlit.components.v1 as components
st.set_option('deprecation.showPyplotGlobalUse', False)
components.html(
    """
    <div class="intro" style="border: 2px solid black; border-radius: 25px; background-color: cornflowerblue;font-family:Trebuchet MS,Garamond ;font-size: 18px;text-align: center; ">
        <h1 style="margin: 0.25;"><strong>Placement Predictor</strong></h1>
        <h2 style="margin: 0.25;">A webapp that can predict student's placements</h2>
    </div>
    <br>
    """,
    height=200,
)

with st.sidebar:

    st.title('Sprint - 2 Assignment')
    st.header('About the Web-App:')
    st.write('This is a web-app that analyses the data provided and predicts whether or not a student is successfully placed.')

    st.header('How does it work ?')
    st.write('● The ML model has been trained using algorithms on the MBA students data.\n')
    st.write('● Enter your data and click on SUBMIT to view the results. ')
    st.sidebar.markdown('![Visitor count](https://shields-io-visitor-counter.herokuapp.com/badge?page=https://share.streamlit.io/am-ram/placementprediction/main/app.py&label=VisitorsCount&labelColor=000000&logo=GitHub&logoColor=FFFFFF&color=1D70B8&style=for-the-badge)')
model = pickle.load(open(r'model_rt', 'rb'))
with st.form('my_form'):
    col1, col2  = st.columns(2)
    with col1:
        ssc = st.number_input(label="Enter SSC percentage",step=1,format="%i")
        hsc = st.number_input(label="Enter HSC percentage",step=1,format="%i")
        deg = st.number_input(label="Enter Degree percentage",step=1,format="%i")
        etest = st.number_input(label="Enter E-test percentage",step=1,format="%i")
        mba = st.number_input(label="Enter MBA percentage",step=1,format="%i")
        
    with col2:
        #6,7
        hs_spec = st.selectbox('What was your High School Specialization ? ',('Arts','Commerce','Others'))
        if(hs_spec=='Arts'): arts=1; comm=0
        elif(hs_spec=='Commerce'): arts=0; comm=1
        else: arts=0; comm=0
        #8
     
    
        others=-1
        isMkt = st.selectbox('Select your degree type. ',('Commerce & Management','Others'))
        if(isMkt): comm_mng=1    
        else : others = 0
    
        #9 10
        mkt_fin=-1;
        isSpec = st.selectbox('What is your MBA Specicialization ? ',('Marketing & Finance','Marketing and HR',))
        if(isSpec=='Marketing & Finance'):mkt_fin=1
        st.write('');st.write('');st.write('');
        isExp = st.checkbox('Do you have prior working experience ?')
        if(isExp): isExp=1
        else : isExp=0
        
        st.write('');st.write('');st.write('');
        x=st.form_submit_button(label="Submit")
if(x):
    ans = model.predict([[ssc,hsc,deg,etest,mba,   arts,comm,   comm_mng,others,  isExp,mkt_fin]])
    if(ans==1): st.success('Congratulations!! The Student is successfully Placed') ; st.balloons()
    elif(ans==0): st.error('Unfortunately, Student is not Placed') 
    components.html(
            """
                <div class="x" style="border: 2px solid black;background-color: rgb(150, 213, 245);font-family:sans serif ;font-size: 12px; padding-left:5px;border-radius:7px">
                    <h1 style="margin: 0.25;"><strong>Metrics of Predicted Results</strong></h1>
                    <h2 style="margin: 0.25;text-align:center">Accuracy: <span>97.54%</span> | Precision: <span>0.97</span></h2>
                    
                    <h2 style="margin: 0.25; text-align:center">Recall: <span>0.99 | F-1 Score: <span>0.87</span></span></h2>
                    
                </div>
            """
        )
    #ans = model.predict([[ssc,hsc,deg,etest,mba,arts,comm,isDeg,others,isExp,mkt_fin]])
