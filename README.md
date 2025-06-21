# 🤖 Conversational QA Bot (CoQA-Based)

This is a conversational Question Answering bot fine-tuned on the [CoQA dataset](https://stanfordnlp.github.io/coqa/). It uses a custom-trained T5 model to answer questions based on the provided context.

## 🚀 Features

- Fine-tuned T5 model using ~1.1 million examples from the CoQA dataset
- Context-aware question answering
- Deployed as a simple web app using Streamlit
- Fast and responsive interface
- Trained model saved and loaded from local directory

## 📁 Project Structure

├── Data
│ ├── coqa-dev-v1.0.json
│ └── coqa-train-v1.0.json
├── t5_coqa_final_model
│ └── t5_coqa_final_model
│ ├── config.json
│ ├── model.safetensors
│ ├── tokenizer_config.json
│ └── ...
├── app.py
├── utils.py
├── requirements.txt
└── README.md

## 🧠 Model

- **Model**: T5 (Text-to-Text Transfer Transformer)
- **Framework**: Hugging Face Transformers + PyTorch
- **Tokenizer**: SentencePiece
- **Training**: Fine-tuned for 3 epochs on a cleaned version of CoQA with early stopping and model checkpointing.

## ⚙️ Setup Instructions

### 1. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

2. Install dependencies

pip install -r requirements.txt

Run the Streamlit app

streamlit run app.py