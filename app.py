import streamlit as st
import pandas as pd
st.set_page_config(
    page_title='Correlation Analysis',page_icon='📊')
st.sidebar.success('Pages Above')
st.title("Correlation Analysis")
st.header("Karl Pearson",divider=True) 
col1,col2=st.columns(2)
with st.sidebar:
    st.link_button('Karl Pearson ','https://en.wikipedia.org/wiki/Karl_Pearson')
with col1:
    st.image('karl.jpg')

with col2:
    st.text('Karl Pearson Through his mathematical work and his institution building, Pearson played a leading role in the creation of modern statistics. The basis for his statistical mathematics came from a long tradition of work on the method of least squares approximation, worked out early in the 19th century in order to estimate quantities from repeated astronomical and geodetic measures using probability theory. Pearson drew from these studies in creating a new field whose task it was to manage and make inferences from data in almost every field. His positivistic philosophy of science (see positivism) provided a persuasive justification for statistical reasoning and inspired many champions of the quantification of the biological and social sciences during the early decades of the 20th century. He was the first to introduce the probability value, or p-value, which has since become a core tool of testing hypotheses in statistical studies in a wide variety of fields.')
st.divider()
























