import streamlit as st
from langgraph import LangGraph
from plan_agent import PlanAgent
from tool_agent import ToolAgent
from reflection import Reflection

# Initialize components
lang_graph = LangGraph()
plan_agent = PlanAgent(lang_graph)
tool_agent = ToolAgent(lang_graph)
reflection = Reflection(lang_graph)

# Streamlit app
st.title("Task Workflow System")

# Input form for user query
user_query = st.text_input("Enter your query:")

if st.button("Process Query"):
    if user_query:
        # Process the query
        plan_agent.split_query(user_query)

        results = []
        feedbacks = []

        # Solve tasks and collect results
        for task_id in lang_graph.list_tasks().keys():
            result = tool_agent.solve_task(task_id)
            results.append(result)

        # Provide feedback
        for task_id in lang_graph.list_tasks().keys():
            feedback = reflection.reflect_on_task(task_id)
            feedbacks.append(feedback)

        # Display results
        st.subheader("Results")
        for result in results:
            st.write(result)

        st.subheader("Feedback")
        for feedback in feedbacks:
            st.write(feedback)
    else:
        st.warning("Please enter a query.")
