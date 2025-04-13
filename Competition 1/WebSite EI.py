import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Smart City Solutions (By Omar)", page_icon=":cityscape:", layout="wide")

st.subheader("Hi, I am Omar 👋")
st.title("A Student from [Codingal](https://www.codingal.com)")
st.write("My mission is to develop WebSites for smart city solutions that improve sustainability, enhance transportation, and leverage technology for healthier communities.")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.header("Smart City Solutions")
        st.write("""
#### Sustainability
1. **Solar Panels**: Incentives for installation to reduce reliance on fossil fuels.
2. **Urban Gardens**: Encouraging local food production and improving air quality.
3. **Waste Management**: Connected bins to optimize collection and reduce emissions.
4. **Green Roofs**: Enhancing insulation and reducing urban heat.

#### Transportation
1. **Smart Traffic Lights**: Adjusting based on real-time data to ease congestion.
2. **Public Transport App**: Real-time updates on schedules and routes.
3. **Bike-Sharing Systems**: Promoting cycling as a sustainable transport option.
4. **EV Charging Stations**: Expanding infrastructure for electric vehicles.

#### Technology
1. **IoT Sensors**: Collecting data on air quality, traffic, and energy use for urban planning.
2. **Community Feedback App**: Allowing residents to report issues and provide input.
3. **Smart Lighting**: Streetlights that adjust based on traffic for improved safety.
4. **Data Visualization Dashboards**: Visualizing urban trends for informed decision-making.
""")

    with right_column:
        image_url = "https://www.milesight.com/static/mobile/en/solution/smart-city/v2/smart-city-solution-challenge-mobile.png?t=1729851404490"
        st.image(image_url, caption="Smart City Solutions", use_column_width='auto', width=100)  # Ajuster la largeur de l'image
        
        # Ajout de la vidéo sous l'image


with st.container():
    st.write("---")
    st.header("Youtube Video")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        video_url = "https://www.youtube.com/watch?v=gXuPXqNdCLw&t=5s"  # Remplacez par l'URL de votre vidéo
        st.video(video_url)  # La vidéo s'ajuste automatiquement à la largeur de la colonne
    
    with text_column:
        st.subheader("Youtube Video for Smart Cities Solution")
        st.write("""What does it really mean to make a city smart ? This video will explain how tomorrow's smart cities will share data between governmental departments and citizens to make everyday life more efficient.""")
        st.write("""Explore how smart city solutions are changing urban life for the better! In this video, we’ll look at technologies like IoT and AI that improve transportation, energy use, and public safety. Discover real-world examples of smart cities making a positive impact on communities and learn how these innovations can create cleaner, safer, and more efficient living spaces. Join us to see how the cities of the future are being built today !""")
        st.write("[Watch The Video On Youtube  >](https://www.youtube.com/watch?v=gXuPXqNdCLw)")

with st.container():
    st.write("---")
    st.header("Codingal")
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVcZ4pP_fMZ9ji8LrccMxDekGqzu6E6e1Jow&s"
        st.image(image_url, caption="Codingal Logo", use_column_width='auto', width=300)  # Ajuster la largeur de l'image
    with text_column:
        st.subheader("About Codingal")
        st.write("""Codingal is an online learning platform designed for children and teenagers to learn coding and computer science skills. It offers a variety of courses for different age groups and skill levels, focusing on interactive and project-based learning. 

The platform covers programming languages like Python, Java, and Scratch, along with concepts such as game development, app creation, and web development. 

Students can participate in live, instructor-led classes that provide real-time interaction and personalized feedback. They also work on hands-on projects to apply their knowledge and build a portfolio of work. """)
        st.write(" -   To learn more, visit the Codingal website to explore the courses, projects, and opportunities available !     [Codingal   >](https://www.codingal.com)")

    st.write("---")
    st.write("###")
    st.header("Thank You")
    st.write("""Thank you for exploring our site ! We hope you found valuable insights into how we can create smarter, more sustainable urban environments. If you have questions or want to learn more about our initiatives, please don't hesitate to reach out. Together, let's build better cities for a brighter future !""")
