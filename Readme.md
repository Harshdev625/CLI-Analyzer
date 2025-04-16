# CLI-Analyzer

**CLI-Analyzer** is a Flask-based API that uses Google's Gemini API to parse raw command-line outputs and generate structured, programmatically-usable JSON responses — optionally suggesting chart types for easy visualization.

---

## 🚀 Features

- 🔍 Extracts useful information from raw terminal output
- 🧠 Understands user prompts and instructions
- 📦 Returns structured JSON data
- 📊 Recommends chart types with labels and data (bar, line, pie)
- 🤖 Powered by Gemini AI (via Google GenAI)

---

## 📂 Project Structure
```
CLI-Analyzer/
├── app.py              # Main Flask application
├── .env                # Environment variables (API key)
├── .gitignore          # Ensures .env is not tracked
├── requirements.txt    # Python dependencies
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Harshdev625/CLI-Analyzer.git
cd CLI-Analyzer
```

### 2. Create `.env` File
Create a `.env` file in the root directory and add your Gemini API key:
```
GEMINI_API_KEY=your_key_here
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask App
```bash
python app.py
```
Server will run at `http://127.0.0.1:5000/`

---

## 📮 API Endpoint

### POST `/process`

**Request Body (JSON):**
```json
{
  "command_output": "<your_raw_terminal_output_here>",
  "user_prompt": "<what_you_want_to_extract_or_know>"
}
```

**Response (JSON):**
```json
{
  "response": {
    "type": "extraction_result",
    "data": {
      "key1": "value1",
      "key2": "value2"
    },
    "chart": {
      "recommended": true,
      "chartType": "bar",
      "labels": ["label1", "label2"],
      "data": [10, 20]
    },
    "note": "Brief context about data or reasoning"
  }
}
```

---

## 📌 Notes
- The `.env` file is ignored via `.gitignore` and should never be pushed to GitHub.
- Only the structured JSON response will be returned — no additional explanations.
- Useful for visualizing system logs, performance stats, or structured command-line data.

---

## 🧠 Powered By
- [Flask](https://flask.palletsprojects.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [Google GenAI](https://ai.google.dev/)

---

## 📃 License
MIT License

---

## 👤 Author
**Harsh Dev**

