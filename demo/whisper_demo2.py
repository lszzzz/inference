from xinference.client import Client

client = Client("http://127.0.0.1:9997")

model = client.get_model("whisper-base")
with open("/Users/samlee/Documents/sample/asr/longwav_2.wav", "rb") as audio_file:
    print(model.transcriptions(
        audio=audio_file.read(),
        response_format='verbose_json'
    ))