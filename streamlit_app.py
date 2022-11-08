import streamlit
streamlit.title('My Parents new healthy diner')
streamlit.header('Starting with Breakfast Menu')
streamlit.text('\N{bread} \N{butter} \N{hot beverage} Toasted Bread with Butter along with Tea')
streamlit.text('\N{bowl with spoon} Cereal with choice of your falvor')
streamlit.text('\N{flatbread} Aalo Parantha with Pudina Chutney')
streamlit.header('\N{banana} \N{strawberry} Build your own smoothie \N{blueberries} \N{peach}')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
