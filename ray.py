import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe


menu = ["Home","About"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
    st.set_page_config(layout="centered", page_icon="👨‍🎓", page_title="Certificate Generator")
    st.title("👨‍🎓 RAMOND CERTIFICATE GENERATOR")

    st.write(
        "This app was created by Fasasi Abdul-Rahman (A MACHINE LEARNING AND AI DEVELOPER) for the purpose generating your cerificate in pdf format"
    )

    left, right = st.columns(2)

    right.write("Here's the template we'll be using:")

    right.image("template.png", width=300)

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

     
    elif submit:
        
        
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
    
    
else:
    st.subheader("ABOUT THE DEVELOPER")
    st.text('''
    MY NAME IS FASASI ABDULRAHMAN TEMITOPE.
    I'M A MACHINE LEARNING AND ARTIFICIAL INTELLIGIENCE DEVELOPER.
    I CREATED THIS APPLICATION SO AS TO HELP PEOPLE TO BE ABLE TO PRINT OUT CERTIFICATE IN PDF FORMAT.
            ''')
    image =("my (2).jpg")
    st.image(image,caption=None, width=490, use_column_width=100, clamp=False, channels="RGB", output_format="auto")
    
    
    st.subheader("ABOUT THE APP")
    st.text("CERTIFICATE GENERATOR")
    st.text("POWERED BY:FASASI ABDULRAHMAN TEMITOPE")
    st.text("I can see that you are impressed after checking my work")
    st.text("Oya start bringing work ooo")
    st.success("AN NLP PROJECT")
    st.balloons()    
