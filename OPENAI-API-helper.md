## OPENAI API

URL: https://api.openai.com/v1/chat/completions

**Request** to the proxy server:

```
curl -X POST http://0.0.0.0:5500/api/openai \
-u "username:password" \
-H "Content-Type: application/json" \
-H "X-OpenAI-Authorization: Bearer OPENAI_API_KEY"
-d '{
  "model": "gpt-4o",
  "messages": [
    {
      "role": "assistant",
      "content": "You are a helpful assistant designed to output JSON and your purpose is to decide the industry of the given company name."
    },
    {
      "role": "user",
      "content": "I will give you the name of the company and you will decide the NAICS code it belongs to.\nPlease return the result in the following format, do not include any explanations:\n{\n\"NAICS_code\": \"NAICS code\"\n}\nUtilize your expertise to generate the most pertinent information.\nCompany Name: \"Sony\"\nResponse: {\"NAICS code\": \"334610\"}\nCompany Name: \"SOCAR\""
    }
  ],
  "temperature": 0.001,
  "max_tokens": 300,
  "frequency_penalty": 0.0,
  "n": 3,
  "response_format": {
    "type": "json_object"
  }
}'
```

Request in the proxy server to the OPENAI api using curl:

```bash
curl -X POST https://api.openai.com/v1/chat/completions \
-H "Authorization: X-OpenAI-Authorization" \
-H "Accept-Encoding: identity" \
-H "Content-Type: application/json" \
-d '{
  "model": "model name",
  "messages": [
    {
      "role": "assistant",
      "content": "asistant prompt content"
    },
    {
      "role": "user",
      "content": "user prompt content"
    }
  ],
  "temperature": temperature,
  "max_tokens": max_tokens,
  "frequency_penalty": freq-penalty,
  "n": number of completions,
  "response_format": "json_object"
}'
```

in PYTHON:

```python
@app.post("/api/openai")
async def openai_proxy(request: Request, credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    data = await request.json()
    # Call the OpenAI API
    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={'Authorization': request.headers["X-OpenAI-Authorization"],  'Accept-Encoding': 'identity'},
        json=data
    )
    return response.json()
```

