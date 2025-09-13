import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

# Main app layout
def main():
    # Page config
    st.set_page_config(page_title="LinkedIn Post Generator", page_icon="📝", layout="wide")

    # Header
    st.title("🚀 LinkedIn Post Generator")
    st.markdown(
        """
        Create engaging LinkedIn posts instantly!  
        Select your **topic**, **post length**, and **language** – then let AI craft your post.  
        """
    )
    st.divider()

    # Create three columns for dropdowns
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()

    with col1:
        selected_tag = st.selectbox("🎯 Select a Topic", options=tags)

    with col2:
        selected_length = st.selectbox("📏 Post Length", options=length_options)

    with col3:
        selected_language = st.selectbox("🌐 Language", options=language_options)

    # Generate Button (center aligned)
    st.markdown("<br>", unsafe_allow_html=True)  # add space
    if st.button("✨ Generate My Post", use_container_width=True, type="primary"):
        with st.spinner("Crafting your post... ⏳"):
            post = generate_post(selected_length, selected_language, selected_tag)

        # Display result
        st.success("✅ Your LinkedIn Post is Ready!")

        # Copy to clipboard / display
        st.code(post, language="markdown")


# Run the app
if __name__ == "__main__":
    main()
