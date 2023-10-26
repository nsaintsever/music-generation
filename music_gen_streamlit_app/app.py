import streamlit as st
import torch
import torchaudio
from audiocraft.models import MusicGen
import os
import numpy as np
import base64

def load_model():
    model = MusicGen.get_pretrained('facebook/musicgen-large')
    return model


def generate_music_tensors(description, duration: int):
    model = load_model()

    model.set_generation_params(
        use_sampling=True,
        top_k=250,
        duration=duration
    )

    output = model.generate(
        descriptions=[description],
        progress=True,
        return_tokens=True
    )
    return output[0]


def save_audio(samples: torch.Tensor):
    """Renders an audio player for the given audio samples and saves them to a local directory.

    Args:
        samples (torch.Tensor): a Tensor of decoded audio samples
            with shapes [B, C, T] or [C, T]
        sample_rate (int): sample rate audio should be displayed with.
        save_path (str): path to the directory where audio should be saved.
    """

    print("Samples (inside function): ", samples)
    sample_rate = 30000
    save_path = "audio_output/"
    assert samples.dim() == 2 or samples.dim() == 3

    samples = samples.detach().cpu()
    if samples.dim() == 2:
        samples = samples[None, ...]

    for idx, audio in enumerate(samples):
        audio_path = os.path.join(save_path, f"audio_{idx}.wav")
        torchaudio.save(audio_path, audio, sample_rate)

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

st.set_page_config(
    page_icon= "musical_note",
    page_title= "Music Gen"
)

def main():
    with st.sidebar:
        st.header("""⚙️ Parameters ⚙️""",divider="rainbow")
        st.text("")
        st.subheader("1. Enter your music description.......")
        text_area = st.text_area('Ex : 80s rock song with guitar and drums')
        st.text('')
        st.subheader("2. Select time duration (In Seconds)")

        time_slider = st.slider("Select time duration (In Seconds)", 0, 20, 10)

    st.title("""🎵 Text to Music Generator 🎵""")
    st.text('')
    left_co,right_co = st.columns(2)
    left_co.write("""Music Generation using Meta AI, through a prompt""")
    left_co.write(("""PS : First generation may take some time as it loads the full model and requirements"""))
    #container1 = st.container()
    #container1.write("""Music coupled with Image Generation using a prompt""")
    #container1.write("""PS : First generation may take some time as it loads the full model and requirements""")


    if st.sidebar.button('Generate !'):
        gif_url = "https://media.giphy.com/media/26Fffy7jqQW8gVg8o/giphy.gif"
        with right_co:
            with st.spinner("Generating"):
                st.image(gif_url,width=250)
        with left_co:
            st.text('')
            st.text('')
            st.text('')
            st.text('')
            st.text('')
            st.text('')
            st.subheader("Generated Music")

            music_tensors = generate_music_tensors(text_area, time_slider)
            save_music_file = save_audio(music_tensors)
            audio_filepath = 'audio_output/audio_0.wav'
            audio_file = open(audio_filepath, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes)
            st.markdown(get_binary_file_downloader_html(audio_filepath, 'Audio'), unsafe_allow_html=True)


if __name__ == "__main__":
    main()
