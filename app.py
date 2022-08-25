import streamlit as st

def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

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
    @st.cache
    def load_data():
        data = pd.read_csv(DATA_URL)
        return data

    st.subheader("Load and showcase data")
    st.markdown("""
        You can use the usual Data Science libraries like `pandas` or `numpy` to load data. 
        Then simply use [`st.write()`](https://docs.streamlit.io/library/api-reference/write-magic/st.write) to showcase it on your web app. 
    """)

    data_load_state = st.text('Loading data...')
    dataset_delay = load_data()
    data_load_state.text("") # change text from "Loading data..." to "" once the the load_data function has run

    #dataset_delay = dataset_delay.dropna(subset = ['delay_at_checkout_in_minutes'])

    # listing dataframes types
    list(set(dataset_delay.dtypes.tolist()))
    # include only float and integer
    df_delay_num = dataset_delay.select_dtypes(include = ['float64', 'int64', 'UInt32'])
    # display what has been selected
    df_delay_num.head()
    # plot
    #df_delay_num.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8);

    #------------------------------
    import matplotlib.pyplot as plt
    import numpy as np
    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    st.pyplot(fig)

    #------------------------------

    #Count the number of cases where the delay at check out was higher than expected
    # dataset_delay['delay_problem']= dataset_delay['delay_at_checkout_in_minutes']-dataset_delay['time_delta_with_previous_rental_in_minutes']


    # def compute_stats_threshold(delay_tresh, check_type):
    #     if check_type == 'connect':
    #         nb_rent_above_threshold = dataset_delay[(dataset_delay['delay_problem'] > delay_tresh) & (dataset_delay['checkin_type']=='connect')].count()
    #     else :
    #         nb_rent_above_threshold = dataset_delay[(dataset_delay['delay_problem'] > delay_tresh) & (dataset_delay['checkin_type']=='mobile')].count()
    #     return nb_rent_above_threshold

    # x_plot=dict()
    # y_mobile=dict()
    # y_connect=dict()
    # y_mobile_ratio=dict()
    # y_connect_ratio=dict()

    # nb_rent_connect=  dataset_delay[dataset_delay['checkin_type']=='connect'].count()[0]
    # nb_rent_mobile=  dataset_delay[dataset_delay['checkin_type']=='mobile'].count()[0]

    # for i in range (0,400):
    #     x_plot[i]=i
    #     y_mobile[i]=(compute_stats_threshold(i,'mobile')[0])
    #     y_connect[i]=(compute_stats_threshold(i,'connect')[0])
    #     y_mobile_ratio[i]=(compute_stats_threshold(i,'mobile')[0])/nb_rent_mobile*100
    #     y_connect_ratio[i]=(compute_stats_threshold(i,'connect')[0])/nb_rent_connect*100

    #     # Plot the responses for different events and regions
    # df_delay_stat_treshold = pd.DataFrame({'Threshold (min)': x_plot.values(),'Rent_lost_mobile(%)': y_mobile_ratio.values(),'Rent_lost_connect(%)': y_connect_ratio.values()})

    # st.line_chart(data=df_delay_stat_treshold, x='Threshold (min)', y=["Rent_lost_mobile(%)", 'Rent_lost_connect(%)'], use_container_width=True)


def page3():
    import streamlit as st
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    DATA_URL = 'get_around_pricing_project.csv'
    @st.cache
    def load_data():
        data = pd.read_csv(DATA_URL)
        return data
    st.subheader("Load and showcase data")
    st.markdown("""
        You can use the usual Data Science libraries like `pandas` or `numpy` to load data. 
        Then simply use [`st.write()`](https://docs.streamlit.io/library/api-reference/write-magic/st.write) to showcase it on your web app. 
    """)

    data_load_state = st.text('Loading data...')
    dataset_pricing = load_data()
    data_load_state.text("") # change text from "Loading data..." to "" once the the load_data function has run

    
    st.markdown("# Prédiction")
    st.sidebar.markdown("# Prédiction 🎉")
    st.markdown("**Veuillez entrer les informations concernant votre véhicule :**")
    option = st.selectbox('Marque :',tuple(dataset_pricing.model_key.unique()))
    #sepal_width = st.text_input('Enter sepal_width', '')
    #petal_length = st.text_input('Enter petal_length', '')
    #petal_width = st.text_input('Enter petal_width', '')
    #if st.button("Predict"):
        #predict_class()

page_names_to_funcs = {
    "Main Page": main_page,
    "Dashboard": page2,
    "Prédiction": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
