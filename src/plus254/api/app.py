from flask import Flask, jsonify
from dotenv import load_dotenv
from datasets import load_dataset
import os

load_dotenv()

HF_REPO_ID = os.environ.get("HF_REPO_ID")

app = Flask(__name__)

@app.route("/tea")
def get_tea():
    dataset = load_dataset(HF_REPO_ID, split="train")
    return dataset.to_list()


if __name__ == "__main__":
    app.run(debug=True, port=5000)
