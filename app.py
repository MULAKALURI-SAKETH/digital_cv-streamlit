from pathlib import Path

import streamlit as st
from PIL import Image


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

PAGE_TITLE = "Digital CV | Saketh Mulakaluri"
PAGE_ICON = ":wave:"
NAME = "Saketh Mulakaluri"
DESCRIPTION = """
Student at CVR College of Engineering
"""
EMAIL = "sakethmulakaluri02@gmail.com"
SOCIAL_MEDIA = {
	"LinkedIn": "https://www.linkedin.com/in/saketh-mulakaluri-3b441921a",
	"GitHub": "https://github.com/MULAKALURI-SAKETH/",
	"Twitter": "https://twiiter.com/sakethm123",
}
PROJECTS = {
	"Flask web app for Movie Recommender System": "https://github.com/MULAKALURI-SAKETH/Flask-app-Movie_Recommender_System",
	"Titanic Survival Prediction": "https://github.com/MULAKALURI-SAKETH/Spaceship-Titanic-survival-prediction",
	"Sales forecasting": "https://github.com/MULAKALURI-SAKETH/Walmart-Sales-Forecasting",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)



with open(css_file) as f:
	st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
	PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

col1, col2 = st.columns(2, gap="small")
with col1:
	st.image(profile_pic, width=230)

with col2:
	st.title(NAME)
	st.write(DESCRIPTION)
	st.download_button(
		label=" 📄 Download Resume",
		data=PDFbyte,
		file_name=resume_file.name,
		mime="application/octet-stream",
	)
	st.write("📫", EMAIL)


st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
	cols[index].write(f"[{platform}]({link})")


st.write("#")
st.subheader("Skills")
st.write(
	"""
- Programming: Python, Java, SQL
- Data Visualization: Tableau
- Data science with Python
- Databases: MySQL
"""
)




st.write("#")
st.subheader("Internships")
st.write("---")


st.write("Salesforce Developer Virtual Internship")
st.write("08/2023 - 10/2023")




st.write("#")
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
	st.write(f"[{project}]({link})")