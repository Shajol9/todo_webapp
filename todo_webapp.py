import streamlit as st
import functions


todo_list = functions.get_todo()

def add_todo():
    newtodo = st.session_state["new_todo"] + "\n"
    # if newtodo not in todo_list:
    todo_list.append(newtodo)
    functions.write_todo(todo_list)
    st.session_state["new_todo"] = ""

st.title("My TO-DO App")
st.subheader("This is a simple Todo app.")
st.write('''You can add a new todo by typing it in the text box and 
         then hitting enter.\nYou can also marke a todo as completed 
         by clikcing the coresponding checkbox and the todo will be 
         deleted.''')

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        completed_item =  todo_list.pop(index)
        functions.write_todo(todo_list)
        del st.session_state[index]
        st.rerun()

st.text_input(label ="Add new todo:", 
              placeholder="Type here to add nwe todo...",
              key="new_todo")

st.button(label="Add" ,on_click=add_todo, key="add")

#st.session_state