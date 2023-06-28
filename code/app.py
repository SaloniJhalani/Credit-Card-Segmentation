from pathlib import Path
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import main


if __name__ == "__main__":
    sns.set_theme(context='notebook', style='darkgrid', palette='Set2')  #Set Seaborn Theme
    #Default Configurations
    hide_default_format = """
           <style>
           #MainMenu {visibility: hidden; }
           footer {visibility: hidden;}
           </style>
           """
    st.set_page_config(page_title="Credit Card Segmentation App", page_icon=None, layout="centered",
                       initial_sidebar_state="auto")
    st.markdown(hide_default_format, unsafe_allow_html=True)

    #Display Header
    st.title("Credit Card Segmentation App")

    original_data = pd.read_csv(str(Path(__file__).parents[1] / 'data/credit_card_data.csv'))  #Load Data

    #Preprocessing on original data
    original_data = main.data_cleaning(original_data)
    data = original_data.copy()
    data = main.handle_skewness(data)
    X = main.handle_dimensions(data)

    # Define the sidebar radio buttons to switch between pages
    page = st.sidebar.radio("Select Page:", ('Show Features', 'Show Clusters'))

    if page == 'Show Features':
        st.write("""
            The Credit Card Segmentation App is a tool designed for analyzing credit card data and segmenting customers based on their spending patterns.
            
            This page provides a comprehensive view of the credit card dataset, displaying feature distributions and scatter plots to visualize relationships between different variables. 
            """)

        st.subheader('Explore Credit Card Data')

        # Checkbox to show/hide the entire data
        show_data = st.checkbox('Show Entire Data',value=True)
        if show_data:
            st.write(data)

        # Dropdown to select the column for feature distribution plot
        st.subheader('Feature Distribution')
        feature_column = st.selectbox('Select Column for Feature Distribution:', original_data.columns)
        #Display Feature Distribution
        fig = plt.figure(figsize=(10, 4))
        if feature_column in ['TENURE']:
            sns.countplot(x=feature_column, data=original_data)
        else:
            sns.histplot(x=feature_column, data=original_data)
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # Dropdowns to select columns for scatter plot
        st.subheader('Scatter Plot')
        scatter_x = st.selectbox('Select X Column for Scatter Plot:', original_data.columns)
        scatter_y = st.selectbox('Select Y Column for Scatter Plot:', original_data.columns,index=2)
        # Plotting a scatter plot
        fig = plt.figure(figsize=(10, 4))
        sns.scatterplot(data=original_data, x=scatter_x, y=scatter_y)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    elif page == 'Show Clusters':
        st.write("""
            This page focuses on credit card segmentation. Please choose the number of clusters within a range of 2 to 10. The app employs clustering algorithms, such as K-means, to group similar credit card users based on various features. 
        """)

        st.subheader('Cluster Visualization')
        # Code for cluster-related functionalities
        n_clusters = st.slider("Number of Clusters", min_value=2, max_value=10, value=4)
        labels, model = main.model_training(X, n_clusters=n_clusters)
        original_data["Cluster"] = labels

        #Select X and Y values
        scatter_x = st.selectbox('Select X Column for Scatter Plot:', original_data.columns, index=3)
        scatter_y = st.selectbox('Select Y Column for Scatter Plot:', original_data.columns, index=2)

        # Plot scatter plot
        fig = plt.figure(figsize=(10, 4))
        sns.scatterplot(data=original_data, x=scatter_x, y=scatter_y,hue="Cluster")
        st.pyplot(fig)








