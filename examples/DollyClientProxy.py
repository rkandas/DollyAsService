import requests

class DollyClientProxy:
    url: str
    def __init__(self, url: str = "http://127.0.0.1:8000/api/"):
        self.url = url
    def instruct_generate(self,prompt: str, temperature: float = 0.95, max_tokens: int = 64, top_k: int = 500, end_key: str = "### End", do_sample: bool = True):
        params = {
            "temperature": temperature,
            "max_tokens": max_tokens,
            "top_k": top_k,
            "end_key": end_key,
            "do_sample": do_sample
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        data = {
            "prompt": prompt
        }
        response = requests.post(f"{self.url}instruct_generate", params=params, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()["response"]
        else:
            raise Exception("Error generating response: " + response.text)
        
    def prompt_generate(self,prompt: str, temperature: float = 0.95, max_tokens: int = 64, top_k: int = 500, end_key: str = "### End", do_sample: bool = True):
        params = {
            "temperature": temperature,
            "max_tokens": max_tokens,
            "top_k": top_k,
            "end_key": end_key,
            "do_sample": do_sample
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        data = {
            "prompt": prompt
        }
        response = requests.post(f"{self.url}freeform_generate", params=params, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()["response"]
        else:
            raise Exception("Error generating response: " + response.text)
