import requests
import streamlit as st
st.title("The AI Image Studio")

st.sidebar.header("Image Dimensions")
Art_Style = st.sidebar.selectbox("Select Art Style",[
    "Realistic", "Cartoon", "Anime", "Abstract", "Surrealism", "Pop Art", "Impressionism", "Cubism", "Minimalism", "Expressionism"])


width = st.sidebar.slider("Image Width", min_value=256, max_value=1024, value=768, )
height = st.sidebar.slider("Image Height", min_value=256, max_value=1024, value=768,)

user_prompt = st.text_input("Describe the image you want to generate:")

#add a button 
if st.button("Generate Image"):
    if user_prompt:
        with st.spinner("Rendering the image..."):
            full_prompt=f"{user_prompt},make the art style: {Art_Style}"
            url=f"https://image.pollinations.ai/prompt/{full_prompt}?width={width}&height={height}"
            response = requests.get(url) 

            if response.status_code == 200:
                st.success("Image generated successfully!")
                # st.write(response)
                # convert the binary content to an image and display it
                st.image(response.content, caption=full_prompt)
                st.download_button(
                    label ="Download Image",
                    data = response.content,
                    file_name = "generated_image.png",
                    mime = "image/*"
                )
            else:
                st.error(f"Failed to generate image. Status code: {response.status_code}")
    else:
        st.warning("Please enter a prompt to generate an image.")           
       