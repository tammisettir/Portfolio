import streamlit as st
import streamlit.components.v1 as components
from constant import *
import base64
from PIL import Image

st.set_page_config(page_title='Resume' ,layout="wide",page_icon='👧🏻')

#style
#def local_css(file_name):
#    with open(file_name) as f:
#        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
#local_css("style/style.css")


#profile
profile_img = Image.open("images/profile.png")

# ----------------- sidebar ----------------- #
st.sidebar.markdown('''
# Sections
- [Skills](#skills)
- [Tableau](#tableau)
- [Streamlit](#streamlit)
- [ChatGPT](#chatgpt)
- [Resume](#resume)
- [Contact Me](#contact)
''', unsafe_allow_html=True)





# ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

with st.container():
    col1,col2 = st.columns([8,3])

full_name = info['Full_Name']
with col1:
    gradient('#FFD4DD','#000395','e0fbfc',f"Hi, I'm {full_name}👋", info["Intro"])
    st.write("")
    st.write(info['About'])
    
    
with col2:
    st.image(profile_img)
        

# ----------------- skillset ----------------- #
with st.container():
    st.subheader('⚒️ Skills', anchor = 'skills')
    col1, col2 = st.columns([2, 2])
    with col1:
        st.write("Python")
    with col2:
        st.write("GitHub")
    with col1:
        st.write("MySQL")
    with col2:
        st.write("Tableau")
    with col1:
        st.write("Microsoft Office")
    with col2:
        st.write("ChatGPT")
    
    

# -----------------  tableau  -----------------  #
with st.container():
    st.markdown("""""")
    st.subheader("📊 Tableau", anchor = 'tableau')
    col1,col2 = st.columns([0.95, 0.05])
    with col1:
        with st.expander('See the work'):
            components.html(
                """
                <!DOCTYPE html>
                <html>  
                    <title>Basic HTML</title>  
                    <body style="width:130%">  
						<div class='tableauPlaceholder' id='viz1705888249611' style='position: static'><noscript><a href='#'><img alt='Sheet 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;CO&#47;COVID19US_17050101547560&#47;Sheet1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='COVID19US_17050101547560&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;CO&#47;COVID19US_17050101547560&#47;Sheet1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>
						<script type='text/javascript'>                    
						    var divElement = document.getElementById('viz1705888249611');                    
						    var vizElement = divElement.getElementsByTagName('object')[0];                    
						    vizElement.style.width='100%';                    
						    vizElement.style.height='800px'; // Set a fixed height                   
						    var scriptElement = document.createElement('script');                    
						    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
						    vizElement.parentNode.insertBefore(scriptElement, vizElement);                
						</script>
                    </body>  
                </HTML>
                """
            , height=400, scrolling=True
            )
    st.markdown(""" <a href={}> <em>🔗 access to the link </a>""".format(info['Tableau']), unsafe_allow_html=True)
    
# ----------------- Streamlit ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader('✍️ Streamlit', anchor = 'streamlit')
    col1,col2 = st.columns([0.95, 0.05])
    with col1:
        with st.expander('Try the app'):
            components.html("""<iframe
            src="https://uscovid19.streamlit.app/?embed=true"
            height="450"
            width="100%"
            style={{ width: "100%", border: "none" }}
            ></iframe>""",height=400)
            
        st.markdown(""" <a href={}> <em>🔗 access to the link </a>""".format(info['COVIDStreamlit']), unsafe_allow_html=True)



# ----------------- ChatGPT ----------------- #
video_file = open('images/sortinghat_resized.mov', 'rb')
video_bytes = video_file.read()

# Assuming video_bytes contains your video data as shown in your initial snippet

# Encode the video bytes to Base64
video_base64 = base64.b64encode(video_bytes).decode('utf-8')

# Create a data URI for the video
video_data_uri = f"data:video/mp4;base64,{video_base64}"

# Use Streamlit's components.html to embed the video with the data URI as source
with st.container():
    st.markdown("""""")
    st.subheader('✍️ ChatGPT', anchor='chatgpt')
    col1, col2 = st.columns([0.95, 0.05])
    with col1:
        with st.expander('Watch a demo'):
            components.html(f"""<div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <video width="75%" controls autoplay muted>
            <source src="{video_data_uri}" type="video/mp4">
            Your browser does not support the video tag.
            </video></div>""", height=750)
            
        # Assuming info['ChatGPT'] is defined elsewhere and contains a valid URL
        st.markdown(f"""<a href={info['ChatGPT']}> <em>🔗 access to the link </em></a>""", unsafe_allow_html=True)





# ----------------- resume ----------------- #


with st.container():
    st.markdown("""""")
    st.subheader("📝 Resume", anchor = 'resume')
    col1, col2 = st.columns([0.95, 0.05])
    with col1:
        with st.expander('See the document and download it!'):
            with open("images/resume.pdf", "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                # Adjusting the iframe to fit within the column width and a more responsive height
                pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600px" type="application/pdf"></iframe>'
                st.markdown(pdf_display, unsafe_allow_html=True)



# -----------------  contact  ----------------- #


with st.container():
	st.subheader('Contact Me', anchor = 'contact')
	col1, col2 = st.columns([1, 5])
	with col1:
		st.write("LinkedIn")
	with col2:
		st.write("[Click here](https://www.linkedin.com/in/ramya-tammisetti/)")
	with col1:
		st.write("Email")
	with col2:
		st.write("ramya.tammisetti@gmail.com")
	with col1:
		st.write("Phone")
	with col2:
		st.write("(508) 579 - 1560")


