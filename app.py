from flask import Flask, request, jsonify
from google import genai
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()
app = Flask(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Main system prompt to enforce JSON format
SYSTEM_PROMPT = """
You are a command-line data parser and formatter.

...

Return this strict JSON format:

{
  "type": "extraction_result",
  "data": {
    "key1": value1,
    "key2": value2
  },
  "charts": [
    {
      "recommended": true | false,
      "chartType": "bar" | "line" | "pie",
      "title": "Short title for the chart",
      "labels": [...],
      "data": [...]
    }
  ],
  "note": "Brief context about data or reasoning"
}

Instructions:
- Include multiple chart entries if user prompt implies multiple visualizations.
- If no chart is needed, set "recommended": false and leave chart fields empty.
- Output must be valid JSON. No explanation or markdown.
"""

@app.route("/process", methods=["POST"])
def process_command():
    command_output = request.json.get("command_output", "")
    user_prompt = request.json.get("user_prompt", "")

    if not command_output or not user_prompt:
        return jsonify({"error": "Both command_output and user_prompt are required"}), 400

    # Build full input
    full_input = f"{command_output}\n\n{SYSTEM_PROMPT}\n{user_prompt}"

    try:
        # Get Gemini response
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=full_input,
        )

        response_text = response.text

        # Extract the JSON block
        match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if match:
            result_json = json.loads(match.group(0))
            return jsonify({"status": "success", "data": result_json})
        else:
            return jsonify({"status": "error", "message": "No valid JSON found in Gemini response"}), 500

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

