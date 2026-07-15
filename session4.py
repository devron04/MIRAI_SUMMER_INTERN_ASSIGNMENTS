import requests

user_prompt = "Nvidia , Google logo collab"


url= f"https://image.pollinations.ai/prompt/{user_prompt}"

print("Generating for:{user_prompt}")

response = requests.get(url)

if response.status_code == 200:
    with open("output.png", "wb") as f:
        f.write(response.content)
    print("Image saved as output.png")
else:
    print(f"Failed to generate image. Status code: {response.status_code}")