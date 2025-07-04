from flask import Flask, request, jsonify
import replicate
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables CORS for all domains on all routes

# Replicate API key from environment variable
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")

@app.route("/style-transfer", methods=["POST"])
def style_transfer():
    data = request.json
    image_url = data.get("imageUrl")
    style = data.get("style", "Van Gogh")

    if not image_url:
        return jsonify({"error": "Image URL is required"}), 400

    try:
        prompt = f"{style} style painting"

        output = replicate.run(
            "cjwbw/stable-diffusion-v1-5-img2img:db21e45a13cbb61dc8c2810ff038f6c92774a2f12d992e41e122a3a7b0c6b71c",
            input={
                "image": image_url,
                "prompt": prompt,
                "strength": 0.75,
                "num_outputs": 1
            }
        )

        return jsonify({"stylizedImageUrl": output[0]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)