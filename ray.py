import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe

st.set_page_config(layout="centered", page_icon="👨‍🎓", page_title="Certificate Generator")
st.title("👨‍🎓 RAMOND CERTIFICATE GENERATOR")

st.write(
    "This app shows you how you can use Streamlit to make a PDF generator app in just a few lines of code!"
 )

left, right = st.columns(2)

right.write("Here's the template we'll be using:")

right.image("certy.png", width=300)

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("index.html")


left.write("Fill in the data:")
form = left.form("template_form")
student = form.text_input("Student name")
course = form.selectbox(
    "Choose course",
    ["FRONT-END DEVELOPMENT", "SERVER-SIDE DEVELOPEMENT","DATA SCIENCE","MOBILE APP PROGRAMMING","DESKTOP APPLICATION PROGRAMMING", "ARTIFICIAL INTELLIGENCE & MACHINE LEARNING"],
    index=0,
)
grade = form.slider("Grade", 1, 100, 60)
submit = form.form_submit_button("Generate PDF")

if submit:
    html = template.render(
        student=student,
        course=course,
        grade=f"{grade}/100",
        date=date.today().strftime("%B %d, %Y"),
    )

    pdf = pdfkit.from_string(html, False)
    st.balloons()

    right.success("🎉 Your diploma was generated!")
    # st.write(html, unsafe_allow_html=True)
    # st.write("")
    right.download_button(
        "⬇️ Download PDF",
        data=pdf,
        file_name="CERTIFICATE.PDF",
        mime="application/octet-stream",
    )
    
    
