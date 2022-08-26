import streamlit as st

def main_page():
    st.markdown("# Accueil 🎈")
    st.sidebar.markdown("# Accueil 🎈")
    st.title("Bienvenue sur notre site de recommandation de prix de location avec GetAround 🚗")

    st.markdown("""
        Welcome to this awesome `streamlit` dashboard. This library is great to build very fast and
        intuitive charts and application running on the web. Here is a showcase of what you can do with
        it. Our data comes from an e-commerce website that simply displays samples of customer sales. Let's check it out.
        Also, if you want to have a real quick overview of what streamlit is all about, feel free to watch the below video 👇
    """)


    st.markdown("---")

def page2():
    import streamlit as st
    import pandas as pd
    import plotly.express as px 
    import plotly.graph_objects as go
    import numpy as np


    ### Config

    DATA_URL = 'get_around_delay_analysis.csv'


    ### App
    st.title("Build dashboards with Streamlit 🎨")

    st.markdown("""
        Welcome to this awesome `streamlit` dashboard. This library is great to build very fast and
        intuitive charts and application running on the web. Here is a showcase of what you can do with
        it. Our data comes from an e-commerce website that simply displays samples of customer sales. Let's check it out.
        Also, if you want to have a real quick overview of what streamlit is all about, feel free to watch the below video 👇
    """)


    st.markdown("---")


    # Use `st.cache` when loading data is extremly useful
    # because it will cache your data so that your app 
    # won't have to reload it each time you refresh your app
    @st.cache(allow_output_mutation=True)
    def load_data2():
        data2 = pd.read_csv(DATA_URL, sep=';')
        return data2

    st.subheader("Load and showcase data")

    data_load_state = st.text('Loading data...')
    dataset_delay = load_data2()
    data_load_state.text("") # change text from "Loading data..." to "" once the the load_data function has run
    #Count the number of cases where the delay at check out was higher than expected
    dataset_delay.dropna(subset=['delay_at_checkout_in_minutes'], inplace=True)
    dataset_delay = dataset_delay.reset_index(drop=True)
    dataset_delay['delay_problem']= dataset_delay['delay_at_checkout_in_minutes']-dataset_delay['time_delta_with_previous_rental_in_minutes']
    def compute_stats_threshold(delay_tresh, check_type):
        if check_type == 'connect':
            nb_rent_above_threshold = dataset_delay[(dataset_delay['delay_problem'] > delay_tresh) & (dataset_delay['checkin_type']=='connect')].count()
        else :
            nb_rent_above_threshold = dataset_delay[(dataset_delay['delay_problem'] > delay_tresh) & (dataset_delay['checkin_type']=='mobile')].count()
        return nb_rent_above_threshold

    x_plot=dict()
    y_mobile=dict()
    y_connect=dict()
    y_mobile_ratio=dict()
    y_connect_ratio=dict()

    nb_rent_connect=  dataset_delay[dataset_delay['checkin_type']=='connect'].count()[0]
    nb_rent_mobile=  dataset_delay[dataset_delay['checkin_type']=='mobile'].count()[0]

    for i in range (0,400):
        x_plot[i]=i
        y_mobile[i]=(compute_stats_threshold(i,'mobile')[0])
        y_connect[i]=(compute_stats_threshold(i,'connect')[0])
        y_mobile_ratio[i]=(compute_stats_threshold(i,'mobile')[0])/nb_rent_mobile*100
        y_connect_ratio[i]=(compute_stats_threshold(i,'connect')[0])/nb_rent_connect*100
    df_delay_stat_treshold = pd.DataFrame({'Threshold (min)': x_plot.values(),'Rent_lost_mobile(%)': y_mobile_ratio.values(),'Rent_lost_connect(%)': y_connect_ratio.values()})

    st.line_chart(data=df_delay_stat_treshold, x='Threshold (min)', y=["Rent_lost_mobile(%)", 'Rent_lost_connect(%)'], use_container_width=True)
    values = st.slider('Select a range of values',0.0, 100.0, (25.0, 75.0))
    st.write('Values:', values)


def page3():
    import streamlit as st
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pickle
    from sklearn.linear_model import LogisticRegression
    
    DATA_URL = 'get_around_pricing_project.csv'
    @st.cache(allow_output_mutation=True)
    def load_data():
        data = pd.read_csv(DATA_URL)
        return data
    
    data_load_state = st.text('Chargement...')
    dataset_pricing = load_data()
    data_load_state.text("") # change text from "Loading data..." to "" once the the load_data function has run
    
    def predict_price(values):
        import joblib
        predict_array = np.zeros((1,13))
        im_df = pd.DataFrame(predict_array, columns=['model_key', 'mileage', 'engine_power', 'fuel', 'paint_color',
       'car_type', 'private_parking_available', 'has_gps',
       'has_air_conditioning', 'automatic_car', 'has_getaround_connect',
       'has_speed_regulator', 'winter_tires'])
        im_df[0:1] = values
        loaded_model = joblib.load('finalized_model.sav')
        pipeline = joblib.load('finalized_prepoc.sav')
        result = loaded_model.predict(pipeline.transform(im_df))
        return result[0]
    st.markdown("# Prédiction")
    st.sidebar.markdown("# Prédiction 🎉")
    st.markdown("**Veuillez entrer les informations concernant votre véhicule :**")
    marque = st.selectbox('Marque :',tuple(dataset_pricing['model_key'].unique()))
    kil = st.text_input('Entrer le kilométrage :', '')
    puissance = st.text_input('Entrer la puissance du véhicule (en CV) :', '')
    energie = st.selectbox('Carburant :',tuple(dataset_pricing['fuel'].unique()))
    couleur = st.selectbox('Couleur du véhicule :',tuple(dataset_pricing['paint_color'].unique()))
    car_type = st.selectbox('Type de véhicule :',tuple(dataset_pricing['car_type'].unique()))
    parking = st.selectbox('Place de parking privéê :',('Yes', 'No'))
    if parking == 'Yes':
        parking = True
    else:
        parking = False
    gps = st.selectbox('GPS intégré :',('Yes', 'No'))
    if gps == 'Yes':
        gps = True
    else:
        gps = False
    ac = st.selectbox('Climatisation :',('Yes', 'No'))
    if ac == 'Yes':
        ac = True
    else:
        ac = False
    auto = st.selectbox('Boîte automatique :',('Yes', 'No'))
    if auto == 'Yes':
        auto = True
    else:
        auto = False
    gac = st.selectbox('GetAround Connect :',('Yes', 'No'))
    if gac == 'Yes':
        gac = True
    else:
        gac = False
    speed = st.selectbox('Régulateur de vitesse :',('Yes', 'No'))
    if speed == 'Yes':
        speed = True
    else:
        speed = False
    hiver = st.selectbox('Pneus hiver :',('Yes', 'No'))
    if hiver == 'Yes':
        hiver = True
    else:
        hiver = False
    if st.button("Predict"):
        list_values = [marque,int(kil), int(puissance), energie, couleur, car_type, parking, gps, ac, auto, gac, speed, hiver]
        result = predict_price(list_values)
        st.success(f"Le montant de location à la journée de votre véhicule s'élève à {result:.2f} €")
page_names_to_funcs = {
    "Main Page": main_page,
    "Dashboard": page2,
    "Prédiction": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
