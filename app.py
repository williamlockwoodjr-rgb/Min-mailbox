
import os
from flask import Flask, jsonify, request, render_template
from openai import OpenAI

app = Flask(__name__)





@app.get("/")
def home():
    return render_template("index.html")


@app.get("/api/health")
def health():
        if not os.environ.get("OPENAI_API_KEY"):
                return jsonify(
                            ok=False,
                                        error="Server is missing its OPENAI_API_KEY setting."
                                                ), 503
        return jsonify(ok=True)


@app.post("/api/chat")
def chat():
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
               return jsonify({
                    "error:"The server administrator has not configured the OpenAI API key yet."
            
            }), 503

        body = request.get_json(silent=True) or{}
                                                                                                messages = body.get("input", [])

                                                                                                    if not isinstance(messages, list) or not messages:
                                                                                                            return jsonify(error="Please send a message and try again."), 400

                                                                                                                clean_input = []
                                                                                                                    for item in messages[-30:]:
                                                                                                                            if not isinstance(item, dict):
                                                                                                                                        continue
                                                                                                                                                role = item.get("role")
                                                                                                                                                        content = item.get("content")
                                                                                                                                                                if role in ("user", "assistant") and isinstance(content, str):
                                                                                                                                                                            clean_input.append({
                                                                                                                                                                                            "role": role,
                                                                                                                                                                                                            "content": content[:8000]
                                                                                                                                                                                                                        })

                                                                                                                                                                                                                            if not clean_input:
                                                                                                                                                                                                                                    return jsonify(error="No valid message was received."), 400

                                                                                                                                                                                                                                        try:
                                                                                                                                                                                                                                                client = OpenAI(api_key=api_key)
                                                                                                                                                                                                                                                        response = client.responses.create(
                                                                                                                                                                                                                                                                    model="gpt-5-mini",
                                                                                                                                                                                                                                                                                instructions=(
                                                                                                                                                                                                                                                                                                "You are the friendly AI inside a small personal mailbox. "
                                                                                                                                                                                                                                                                                                                "Reply naturally, helpfully, and conversationally. "
                                                                                                                                                                                                                                                                                                                                "Keep replies reasonably concise."
                                                                                                                                                                                                                                                                                                                                            ),
                                                                                                                                                                                                                                                                                                                                                        input=clean_input,
                                                                                                                                                                                                                                                                                                                                                                    max_output_tokens=700,
                                                                                                                                                                                                                                                                                                                                                                            )
                                                                                                                                                                                                                                                                                                                                                                                    return jsonify(reply=response.output_text or "")
                                                                                                                                                                                                                                                                                                                                                                                        except Exception as exc:
                                                                                                                                                                                                                                                                                                                                                                                                message = str(exc)
                                                                                                                                                                                                                                                                                                                                                                                                        if "401" in message or "authentication" in message.lower():
                                                                                                                                                                                                                                                                                                                                                                                                                    error = "Check the server's OPENAI_API_KEY setting."
                                                                                                                                                                                                                                                                                                                                                                                                                            elif "429" in message or "quota" in message.lower():
                                                                                                                                                                                                                                                                                                                                                                                                                                        error = "Check API billing, quota, or rate limits."
                                                                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                            error = "The server could not get an AI reply. Check server logs."
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    app.logger.exception("OpenAI request failed")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            return jsonify(error=error), 502


                                                                                                                                                                                                                                                                                                                                                                                                                                                                            if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                app.run(
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        host="0.0.0.0",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                port=int(os.environ.get("PORT", "5000"))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    )
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
