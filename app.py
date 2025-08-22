import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup

st.title("📊 Instagram Unfollowers Checker")

# Displaying the Tutorial Video
st.subheader("Video Tutorial")
try:
    with open("Tutorial_Insta_Unfollowers_App.mp4", "rb") as tutorial_vid:
        video_bytes = tutorial_vid.read()
    st.video(video_bytes)
except FileNotFoundError:
    st.error("ERROR: Unable to Display Video")

# File Upload Widgets
st.subheader("Upload Your Files")
followers_file = st.file_uploader("Upload your 'Followers' file (followers_1.html)", type="html")
following_file = st.file_uploader("Upload your 'Following' file (following.html)", type="html")

if followers_file and following_file:

    followers_soup = BeautifulSoup(followers_file, "html.parser")
    following_soup = BeautifulSoup(following_file, "html.parser")

    follower_blocks = followers_soup.find_all('div', class_="pam")
    following_blocks = following_soup.find_all('div', class_="pam")

    followers = [block.find("a").text.strip() for block in follower_blocks if block.find("a")]
    following = [block.find("a").text.strip() for block in following_blocks if block.find("a")]

    dont_follow_back = [followed for followed in following if followed not in followers]

    df = pd.DataFrame({"Username": dont_follow_back})
    df.index += 1

    # Displaying Results
    st.subheader("Results")
    st.write(f"Total Followers: {len(followers)}")
    st.write(f"Total Following: {len(following)}")
    st.write(f"❌ Don't Follow Back: {len(dont_follow_back)}")

    st.subheader("List of People Who Don't Follow You Back")

    st.dataframe(df, use_container_width=True)
