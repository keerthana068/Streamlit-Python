import streamlit as st
import pandas as pd
import numpy as np


def main():
    st.title("Food Demand Forecasting")
    
    menu = ["Home", "Dataset"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader('Home')
        
    elif choice =="Dataset":
        st.subheader("Dataset")
        
    return choice


if __name__ == '__main__':
    choice = main()
    
    
if choice == "Home":
    """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Volutpat blandit aliquam etiam erat velit. Elementum pulvinar etiam non quam lacus. Malesuada proin libero nunc consequat interdum varius sit. Ac turpis egestas integer eget aliquet nibh praesent tristique. Ullamcorper eget nulla facilisi etiam dignissim diam quis. Feugiat sed lectus vestibulum mattis ullamcorper velit sed ullamcorper morbi. Eu nisl nunc mi ipsum. Sem integer vitae justo eget magna fermentum iaculis eu non. Neque volutpat ac tincidunt vitae semper quis lectus nulla at. Leo a diam sollicitudin tempor."""

    
elif choice == "Dataset":
    
    @st.cache
    def load_data(nrows):
        data = pd.read_csv('train.csv', nrows=nrows)
        return data
    
    @st.cache
    def load_center_data(nrows):
        data = pd.read_csv('fulfilment_center_info.csv', nrows=nrows)
        return data
    
    @st.cache
    def load_meal_data(nrows):
        data = pd.read_csv('meal_info.csv', nrows=nrows)
        return data
       
    weekly_data = load_data(1000)
    center_info_data = load_center_data(1000)
    meal_data = load_meal_data(1000)
    
    
#Weekly demand    
    st.subheader('Weekly Demand Data')
    if st.checkbox('Show Weekly Demand Data'):
        st.subheader('Weekly Demand Data')
        st.write(weekly_data)
        st.bar_chart(weekly_data['num_orders'])
        df = pd.DataFrame(weekly_data[:40], columns=['num_orders', 'base_price'])
        st.area_chart(df)
        df = pd.DataFrame(weekly_data[:200], columns = ['num_orders','checkout_price','base_price'])
        st.line_chart(df)
        df.hist()
        

#Center Information
    st.subheader('Center Information')
    if st.checkbox('Show Center Information Data'):
        st.subheader('Center Information Data')
        st.write(center_info_data)

        st.bar_chart(center_info_data['region_code'])
        st.bar_chart(center_info_data['center_type'])

        hist_data = [center_info_data['center_id'],center_info_data['region_code']]
        group_labels = ['Center Id', 'Region Code']
        fig = ff.create_distplot(hist_data, group_labels, bin_size=[10, 25])
        st.plotly_chart(fig, use_container_width=True)

#Meal Information        
    st.subheader('Meal Information')
    if st.checkbox('Show Meal Information Data'):
        st.subheader('Meal Information Data')
        st.write(meal_data)
        st.bar_chart(meal_data['cuisine'])
        agree = st.button('Click to see Categories of Meal')
        if agree:
            st.bar_chart(meal_data['category'])
