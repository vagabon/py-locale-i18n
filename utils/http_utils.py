import requests
import json
import markdown

# call OwnYourChatbots API with a prompt and return the response without markdown or html
def api_post(url, content):
    data = {
        "content": content
    }
    print(f"Api calling: {url}")
    response = requests.post(url, json=data)
    print(f"Status code: {response.status_code}")
    
    json_response = json.loads(response.content)
    response_content = json_response["content"]

    plain_text = markdown.markdown(response_content)
    plain_text = plain_text.replace("<p>", "")
    plain_text = plain_text.replace("</p>", "")
    plain_text = plain_text.replace("<code>json", "")
    plain_text = plain_text.replace("</code>", "")
    plain_text = plain_text.replace("```json", "")
    plain_text = plain_text.replace("</code>", "")
    plain_text = plain_text.replace("&lt;", "<")
    plain_text = plain_text.replace("&gt;", ">")
    return plain_text

# call API to correct a french json
def api_json_correction(content):
    url = "https://api.ownyourchatbots.com/chatbot-publickey/send/e0754111-96cf-49a5-b880-cf9803a2897b"
    return api_post(url, content)

# call API to translate a french json into english json
def api_json_translate(content):
    url = "https://api.ownyourchatbots.com/chatbot-publickey/send/e0e726f7-53a2-40e2-8571-d912557443b5"
    return api_post(url, content)
