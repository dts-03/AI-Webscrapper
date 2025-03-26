from flask import Flask, render_template, request, jsonify
from scraper import scrape_website
import ollama

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        scraped_text = scrape_website(url)
        
        # Summarize using Ollama (Replace 'mistral' with your preferred model)
        response = ollama.chat(model="mistral", messages=[{"role": "user", "content": f"Summarize this: {scraped_text}"}])
        summary = response["message"]["content"] if response and "message" in response else "No summary generated."

        return jsonify({"scraped_text": scraped_text, "summary": summary})

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
