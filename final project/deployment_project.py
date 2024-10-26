import pickle
import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler

model = pickle.load(open('survivng_prediction_3.sav','rb'))

st.title('Titanic-Survived_Prediction')
st.info('Easy app to predict survivng')
st.sidebar.header('feature selection')

gender_option  = ['male','female']
Age_stage_option = ['Adult','old','young']
Nickname_option = ['Mrs','Miss','Mr']
Embarked_options = ['C','Q','S']
Pclass_option = ['1','2','3']


sex = st.selectbox('choose an option',options=gender_option,key='1')
if sex == 'male':
    male = 1
    female = 0
else:
    male = 0
    female = 1
st.write(f"selected is: {sex}")
Age_stage = st.selectbox('choose your Gender',options=Age_stage_option,key='2')
if Age_stage == 'old':
    old = 1
    Adult = 0
    young = 0
elif Age_stage == 'Adult':
    old = 0
    Adult = 1
    young = 0
else:
    old = 0
    Adult = 0
    young = 1
st.write(f"selected is: {Age_stage}")
Nickname = st.selectbox('choose your Nickname',options=Nickname_option,key='3')
if Nickname == "Mr":
    Mr = 1 
    Mrs = 0
    Miss = 0
elif Nickname == "Mrs":
    Mr = 0
    Mrs = 1
    Miss = 0
else:
    Mr = 0 
    Mrs = 0
    Miss = 1
st.write(f"selected is: {Nickname}")
Embarked =  st.selectbox('choose your Embarked',options=Embarked_options,key='4')
if Embarked == 'Q':
    Q = 1
    S = 0
    C = 0
elif Embarked == "S":
    Q = 0 
    S = 1
    C = 0
else:
    Q = 0
    S = 0
    C = 1
st.write(f"selected is: {Embarked}")
Pclass = st.selectbox('choose your Pclass',options=Pclass_option,key='5')
st.write(f"selected is: {Pclass}")


age = st.number_input('Enter your Age:')
st.write(f"You entered: {age} (type: {type(age)})")
Parch = st.number_input('How many Parch:',step=1,format="%d")
st.write(f"You entered: {Parch} (type: {type(Parch)})")
SibSp = st.number_input('How many SibSp:',step=1,format="%d")
st.write(f"You entered: {SibSp} (type: {type(SibSp)})")
Fare = st.number_input('Enter the Fare:')
st.write(f"You entered: {Fare} (type: {type(Fare)})")


df = pd.DataFrame({
    'Sex':[sex],
    'male':[male],
    'female':[female],
    'Age_stage':[Age_stage],
    'Old':[old],
    'Adult':[Adult],
    'Young':[young],
    'Nickname':[Nickname],
    'Mr':[Mr],
    "Mrs":[Mrs],
    'Miss':[Miss],
    'Embarked':[Embarked],
    'S':[S],
    'C':[C],
    'Q':[Q],
    'Age':[age],
    'Parch':[Parch],
    'SibSp':[SibSp],
    'Fare':[Fare],
    'Pclass':[int(Pclass)]
})

con = st.sidebar.button('confirm')


if con:
    result = model.predict(df.drop(['Age_stage','Embarked','Sex','Nickname'],axis=1))
    if result == 0:
        st.sidebar.write('Died')
    else:
        st.write('Survived')