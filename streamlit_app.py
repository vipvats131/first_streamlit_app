import streamlit
streamlit.title('My Parents new healthy diner')
streamlit.header('Starting with Breakfast Menu')
streamlit.text('\N{bread} \N{butter} \N{hot beverage} Toasted Bread with Butter along with Tea')
streamlit.text('\N{bowl with spoon} Cereal with choice of your falvor')
streamlit.text('\N{flatbread} Aalo Parantha with Pudina Chutney')
streamlit.header('\N{banana} \N{strawberry} Build your own smoothie \N{blueberries} \N{peach}')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)),['Avacado','Strawberries']

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
