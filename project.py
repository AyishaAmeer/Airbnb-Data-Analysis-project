import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import seaborn as sns
from PIL import Image
import matplotlib as plt
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(layout='wide',page_icon='🌏')

st.title(":blue[AIRBNB DATA ANALYSIS]")
with st.sidebar:
    select=option_menu("Main menu",["HOME","DATA INSIGHTS","DATA EXPLORATION"],icons=["house","upload","gear"])
if select=="HOME":
    #original_title = '<h1 style="font-family: serif; color:white; font-size: 20px;">Streamlit CSS Styling✨ </h1>'
    #st.markdown(original_title, unsafe_allow_html=True)
    # Set the background image
    background_image = """
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-image: url("https://wallpapers.com/images/hd/simple-background-79pwlqnyv5zdcoa0.jpg");
        background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
        background-position: center;  
        background-repeat: no-repeat;
    }
    </style>
    """
    st.markdown(background_image, unsafe_allow_html=True)
    col1,col2=st.columns(2)
    with col2:
        img=Image.open('C:/Users/ayish/GuviProjects/airbnb project/PHOTO.png')
        st.image(img,width=500,channels="RGB")
    
    st.markdown("## :green[:point_right: **Introduction to Airbnb :**] :rainbow[Founded in August of 2008 and based in San Francisco, California, Airbnb is a trusted community marketplace for people to list, discover, and book unique accommodations around the world — online or from a mobile phone or tablet. Whether a spare bedroom, an apartment, a villa or a private island, Airbnb connects travelers to a more diverse and authentic range of experiences in over 34,000 cities and 190 countries.]")
    st.markdown("## :green[:point_right: **Skills take away From This Project:**] :rainbow[Python scripting, Data Preprocessing, Visualization, EDA, Streamlit, MongoDb and Tableau ]")
    st.markdown('## :green[:point_right: **The learning outcomes of this project are:**]')
    st.markdown('## :orange[**1.MongoDB Atlas:**] :rainbow[Gain proficiency in working with MongoDB Atlas to store and retrieve the Airbnb dataset, developing skills in data management with a NoSQL database technology.]')
    st.markdown('## :orange[**2.Streamlit Web Application:**] :rainbow[ Build a user-friendly web application using Streamlit, enhancing skills in web application development for interactive data exploration and visualization.]')
    st.markdown('## :orange[**3.Python Data Analysis:**]:rainbow[Utilize Python for data cleaning, analysis, and visualization tasks, developing expertise in Python libraries such as Pandas and NumPy for data manipulation.]')
    st.markdown('## :orange[**4.Tableau:**]:rainbow[Create interactive dashboards using tools like Tableau, refining skills in data visualization and dashboard creation for comprehensive data presentation.]')
    st.markdown('## :orange[**5.Data Cleaning and Preparation:**]:rainbow[Develop proficiency in cleaning and preparing the Airbnb dataset, including handling missing values, duplicates, and data type conversions, ensuring data quality and consistency.]')
    st.markdown('## :orange[**6.Data Visualization Techniques:**]:rainbow[Master data visualization techniques to effectively communicate insights, developing skills in creating visually appealing and informative charts, maps, and plots.]')
    st.markdown('## :orange[**7.Problem-Solving Skills:**]:rainbow[Apply analytical skills to analyze pricing dynamics, availability patterns, and other factors, developing problem-solving abilities in extracting valuable insights from data.]')
    st.markdown('## :orange[**8.Data-Driven Decision Making:**]:rainbow[Enhance decision-making skills by enabling stakeholders to make informed choices based on the insights and visualizations provided by the project.]')
    st.markdown('## :orange[**9.Collaboration and Project Management:**]:rainbow[Strengthen collaboration and project management skills through the end-to-end development of the project, including task planning, coordination, and timely delivery of project milestones.]')
elif select=="DATA INSIGHTS":
    st.markdown('## :green[**Goal of the Project:] :orange[Understand the popularity of Airbnb based on locations. Analyze the reason about variation based on locations by prices (which area is expensive), reviews (which area is the best), and type of rooms. Realize the situation of the busyness of the host. Predict the future 2020 Airbnb performance in New York City.]')
    st.markdown('## :green[**Description of Data:]')
    st.markdown('## :orange[:point_right: location - Provides details about Airbnb location in New York city. Four attributes including neighbourhood_group (main area), neighbourhood (area), longitude, and latitude .]')
    st.markdown('## :orange[:point_right: listings - Detailed listings data about hosts, Airbnb houses and price. The attributes used in the analysis are id (listing ID), name (name of the listing), host_id (host ID), host_name (name of the host), room_type (listing space type), and price (price in dollars).]')
    st.markdown('## :orange[:point_right: reviews - Detailed reviews given by the guests. Key attributes include number_of_reviews (number of reviews), last_review (latest review), and reviews_per_month (number of reviews per month).]')
    st.header("Data visualisation of Airbnb data using PowerBI")
    img=Image.open('C:/Users/ayish/GuviProjects/airbnb project/power.png')
    st.image(img,width=1000,channels="RGB")

elif select=="DATA EXPLORATION":
    #st.set_page_config(page_title="Airbnb",layout='wide')
    st.title(":bar_chart: Airbnb Analysis")
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

    file=st.file_uploader(":file_folder: Upload a file", type=(['csv','txt','xlsx','xls']))
    if file is not None:
        filename=file.name
        st.write(filename)
        df=pd.read_csv(filename,encoding="ISO-8859-1")
    else:
        os.chdir(r'C:\Users\ayish\GuviProjects\airbnb project')
        df=pd.read_csv('AIRBNB.csv',encoding="ISO-8859-1")

    st.sidebar.header("choose your filter: ")
    region=st.sidebar.multiselect("Pick your neighbourhood group",df['neighbourhood_group'].unique())

    if not region:
        df2=df.copy()
    else:
        df2=df[df["neighbourhood_group"].isin(region)]

    nbghood=st.sidebar.multiselect("Pick the neighbourhood",df2['neighbourhood'].unique())
    if not nbghood:
        df3=df2.copy()
    else:
        df3=df2[df2['neighbourhood'].isin(nbghood)]

    if not region and not nbghood:
        filtered_df=df
    elif not nbghood:
        filtered_df=df[df['neighbourhood_group'].isin(region)]
    elif region and nbghood:
        filtered_df=df3[df['neighbourhood_group'].isin(region) & df3['neighbourhood'].isin(nbghood)]
    elif nbghood:
        filtered_df=df3[df3["neighbourhood"].isin(nbghood)]
    elif region:
        filtered_df=df3[df3["neighbourhood_group"].isin(region)]
    else:
        filtered_df=df3[df3['neighbourhood_group'].isin(region) & df3['neighbourhood'].isin(nbghood)]

    Roomtype=filtered_df.groupby(by=['room_type'],as_index=False)["price"].sum()
    col1,col2=st.columns(2)
    with col1:
        st.subheader("Room Type of neighbourhood")
        fig=px.bar(Roomtype, x='room_type', y='price',text=['${:,.2f}'.format(x) for x in Roomtype['price']],template='seaborn')
        st.plotly_chart(fig, use_container_width=True,height=200)

    with col2:
        st.subheader("neighbourhood group view")
        fig=px.pie(filtered_df, values='price', names='neighbourhood_group',hole=0.5)
        fig.update_traces(text=filtered_df['neighbourhood_group'],textposition='outside')
        st.plotly_chart(fig,use_container_width=True)

    col1,col2=st.columns(2)
    with col1:
        with st.expander("Roomtype Dataview"):
            st.write(Roomtype.style.background_gradient(cmap="Blues"))
            csv=Roomtype.to_csv(index=False).encode('utf-8')
            st.download_button("Download Data", data=csv, file_name="Roomtype.csv", mime="text/csv",
                            help='click here to download the data as a csv file')
            
    with col2:
        with st.expander('Neighbourhood Group Dataview'):
            region=filtered_df.groupby(by="neighbourhood_group",as_index=False)["price"].sum()
            st.write(region.style.background_gradient(cmap='Oranges'))
            csv=region.to_csv(index=False).encode('utf-8')
            st.download_button("Download Data", data=csv, file_name="Neighbourhood_group.csv",mime="text/csv",
                            help='click here to download data as a csv file')
            
    st.subheader("Hierarchial view of Price using Treemap")
    fig2=px.treemap(filtered_df, path=["neighbourhood_group","room_type"], values="price",hover_data=['price'],
                    color="room_type")
    fig2.update_layout(width=200, height=650)
    st.plotly_chart(fig2, use_container_width=True)

    col1,col2=st.columns(2)
    with col1:
        st.subheader('Available days of Neighbourhood group')
        calculate=df.groupby(by='neighbourhood_group',as_index=False)["availability_365"].mean()
        fig=px.bar(calculate, x='neighbourhood_group', y='availability_365',template='seaborn')
        st.plotly_chart(fig, use_container_width=True,height=200)

    with col2:
        calculate=df.groupby(by='neighbourhood_group',as_index=False)["availability_365"].mean()
        fig=px.pie(calculate, values="availability_365",names="neighbourhood_group",hole=0.5)
        st.plotly_chart(fig)

    st.subheader(':point_right: High five Price Summary ')
    with st. expander("Summary_table"):
        df_sample= filtered_df[0:5][["name","host_name","neighbourhood_group","neighbourhood","room_type","price","minimum_nights","availability_365"]]
        fig=ff.create_table(df_sample.sort_values(by='price',ascending=False),colorscale="Cividis")
        st.plotly_chart(fig, use_container_width=True)
    st.subheader(':point_right: Room type Price Summary ')
    with st. expander("Summary_table"):
        table=pd.pivot_table(filtered_df,values="price",index=["neighbourhood_group"] , columns="room_type")
        st.write(table.style.background_gradient(cmap="Blues"))

    st.subheader("Scatter Plot of Neighbourhood group with Reviews")
    data1=px.scatter(filtered_df,x="neighbourhood_group",y="number_of_reviews",color="room_type",size="reviews_per_month",
                    symbol="room_type",hover_data=['neighbourhood'])
    st.plotly_chart(data1,use_container_width=True)

    #fig,ax=plt.subplots()
    plot=px.box(filtered_df,x="neighbourhood_group", y="availability_365")
    st.plotly_chart(plot)

    with st.expander("view data"):
        st.write(filtered_df.iloc[:500,1:20:1].style.background_gradient(cmap='Oranges'))

    csv=df.to_csv(index=False).encode("utf-8")
    st.download_button("Download Dataset", data=csv, file_name="AIRBNB.csv", mime="text/csv")

