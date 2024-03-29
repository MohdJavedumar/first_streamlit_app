import streamlit
streamlit.title('Umar Healthy Diner')
streamlit.header('🥗 Breakfast Menu')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text(' Kale, spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-boiled Free Range Egg')
streamlit.text('🥑 🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits: ",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/kiwi")
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
streamlit.text(fruityvice_response)
#streamlit.stop()
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchall()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
my_cur.execute("select * from pc_rivery_db.public.FRUIT_LOAD_LIST")
my_data_row=my_cur.fetchall()
streamlit.text(my_data_row)
fruit_choice = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding ', fruit_choice)
my_cur.execute ("insert into fruit_load_list values ('from streamlit')")
my_cur.execute ("insert into fruit_load_list values ('test')")
my_cur.execute ("insert into fruit_load_list values ('Guava')")

#from urllib.error import URLError
