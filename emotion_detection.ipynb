{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4561b6b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting transformers\n",
      "  Using cached transformers-5.5.4-py3-none-any.whl.metadata (32 kB)\n",
      "Collecting torch\n",
      "  Using cached torch-2.11.0-cp313-cp313-win_amd64.whl.metadata (29 kB)\n",
      "Collecting pandas\n",
      "  Using cached pandas-3.0.2-cp313-cp313-win_amd64.whl.metadata (19 kB)\n",
      "Requirement already satisfied: numpy in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (2.4.4)\n",
      "Collecting huggingface-hub<2.0,>=1.5.0 (from transformers)\n",
      "  Using cached huggingface_hub-1.11.0-py3-none-any.whl.metadata (14 kB)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from transformers) (26.1)\n",
      "Requirement already satisfied: pyyaml>=5.1 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from transformers) (6.0.3)\n",
      "Requirement already satisfied: regex>=2025.10.22 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from transformers) (2026.4.4)\n",
      "Collecting tokenizers<=0.23.0,>=0.22.0 (from transformers)\n",
      "  Using cached tokenizers-0.22.2-cp39-abi3-win_amd64.whl.metadata (7.4 kB)\n",
      "Collecting typer (from transformers)\n",
      "  Using cached typer-0.24.1-py3-none-any.whl.metadata (16 kB)\n",
      "Requirement already satisfied: safetensors>=0.4.3 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from transformers) (0.7.0)\n",
      "Requirement already satisfied: tqdm>=4.27 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from transformers) (4.67.3)\n",
      "Requirement already satisfied: filelock in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from torch) (3.28.0)\n",
      "Requirement already satisfied: typing-extensions>=4.10.0 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from torch) (4.15.0)\n",
      "Requirement already satisfied: setuptools<82 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from torch) (81.0.0)\n",
      "Requirement already satisfied: sympy>=1.13.3 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from torch) (1.14.0)\n",
      "Requirement already satisfied: networkx>=2.5.1 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from torch) (3.6.1)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from torch) (3.1.6)\n",
      "Requirement already satisfied: fsspec>=0.8.5 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from torch) (2026.3.0)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: tzdata in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from pandas) (2026.1)\n",
      "Requirement already satisfied: hf-xet<2.0.0,>=1.4.3 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from huggingface-hub<2.0,>=1.5.0->transformers) (1.4.3)\n",
      "Collecting httpx<1,>=0.23.0 (from huggingface-hub<2.0,>=1.5.0->transformers)\n",
      "  Using cached httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
      "Requirement already satisfied: mpmath<1.4,>=1.1.0 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from sympy>=1.13.3->torch) (1.3.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from tqdm>=4.27->transformers) (0.4.6)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from jinja2->torch) (3.0.3)\n",
      "Requirement already satisfied: click>=8.2.1 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from typer->transformers) (8.3.2)\n",
      "Requirement already satisfied: shellingham>=1.3.0 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from typer->transformers) (1.5.4)\n",
      "Collecting rich>=12.3.0 (from typer->transformers)\n",
      "  Using cached rich-15.0.0-py3-none-any.whl.metadata (18 kB)\n",
      "Requirement already satisfied: annotated-doc>=0.0.2 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from typer->transformers) (0.0.4)\n",
      "Requirement already satisfied: anyio in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (4.13.0)\n",
      "Requirement already satisfied: certifi in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (2026.2.25)\n",
      "Requirement already satisfied: httpcore==1.* in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (1.0.9)\n",
      "Requirement already satisfied: idna in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (3.11)\n",
      "Requirement already satisfied: h11>=0.16 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from httpcore==1.*->httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (0.16.0)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from rich>=12.3.0->typer->transformers) (4.0.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from rich>=12.3.0->typer->transformers) (2.20.0)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from markdown-it-py>=2.2.0->rich>=12.3.0->typer->transformers) (0.1.2)\n",
      "Using cached transformers-5.5.4-py3-none-any.whl (10.2 MB)\n",
      "Using cached torch-2.11.0-cp313-cp313-win_amd64.whl (114.6 MB)\n",
      "Using cached pandas-3.0.2-cp313-cp313-win_amd64.whl (9.7 MB)\n",
      "Using cached huggingface_hub-1.11.0-py3-none-any.whl (645 kB)\n",
      "Using cached tokenizers-0.22.2-cp39-abi3-win_amd64.whl (2.7 MB)\n",
      "Using cached typer-0.24.1-py3-none-any.whl (56 kB)\n",
      "Using cached httpx-0.28.1-py3-none-any.whl (73 kB)\n",
      "Using cached rich-15.0.0-py3-none-any.whl (310 kB)\n",
      "Installing collected packages: torch, rich, pandas, httpx, typer, huggingface-hub, tokenizers, transformers\n",
      "Successfully installed httpx-0.28.1 huggingface-hub-1.11.0 pandas-3.0.2 rich-15.0.0 tokenizers-0.22.2 torch-2.11.0 transformers-5.5.4 typer-0.24.1\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 25.0.1 -> 26.0.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "%pip install transformers torch pandas numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f72c351",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: transformers in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (5.5.4)\n",
      "Requirement already satisfied: tokenizers in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (0.22.2)\n",
      "Requirement already satisfied: huggingface-hub<2.0,>=1.5.0 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from transformers) (1.11.0)\n",
      "Requirement already satisfied: numpy>=1.17 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from transformers) (2.4.4)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from transformers) (26.1)\n",
      "Requirement already satisfied: pyyaml>=5.1 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from transformers) (6.0.3)\n",
      "Requirement already satisfied: regex>=2025.10.22 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from transformers) (2026.4.4)\n",
      "Requirement already satisfied: typer in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from transformers) (0.24.1)\n",
      "Requirement already satisfied: safetensors>=0.4.3 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from transformers) (0.7.0)\n",
      "Requirement already satisfied: tqdm>=4.27 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from transformers) (4.67.3)\n",
      "Requirement already satisfied: filelock>=3.10.0 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from huggingface-hub<2.0,>=1.5.0->transformers) (3.28.0)\n",
      "Requirement already satisfied: fsspec>=2023.5.0 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from huggingface-hub<2.0,>=1.5.0->transformers) (2026.3.0)\n",
      "Requirement already satisfied: hf-xet<2.0.0,>=1.4.3 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from huggingface-hub<2.0,>=1.5.0->transformers) (1.4.3)\n",
      "Requirement already satisfied: httpx<1,>=0.23.0 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from huggingface-hub<2.0,>=1.5.0->transformers) (0.28.1)\n",
      "Requirement already satisfied: typing-extensions>=4.1.0 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from huggingface-hub<2.0,>=1.5.0->transformers) (4.15.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from tqdm>=4.27->transformers) (0.4.6)\n",
      "Requirement already satisfied: click>=8.2.1 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from typer->transformers) (8.3.2)\n",
      "Requirement already satisfied: shellingham>=1.3.0 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from typer->transformers) (1.5.4)\n",
      "Requirement already satisfied: rich>=12.3.0 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from typer->transformers) (15.0.0)\n",
      "Requirement already satisfied: annotated-doc>=0.0.2 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from typer->transformers) (0.0.4)\n",
      "Requirement already satisfied: anyio in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (4.13.0)\n",
      "Requirement already satisfied: certifi in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (2026.2.25)\n",
      "Requirement already satisfied: httpcore==1.* in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (1.0.9)\n",
      "Requirement already satisfied: idna in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (3.11)\n",
      "Requirement already satisfied: h11>=0.16 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from httpcore==1.*->httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (0.16.0)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from rich>=12.3.0->typer->transformers) (4.0.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from rich>=12.3.0->typer->transformers) (2.20.0)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\sk\\onedrive\\desktop\\emotions\\ai_env\\lib\\site-packages (from markdown-it-py>=2.2.0->rich>=12.3.0->typer->transformers) (0.1.2)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 25.0.1 -> 26.0.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "%pip install --upgrade transformers tokenizers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "de9a998a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\Users\\SK\\OneDrive\\Desktop\\emotions\\ai_env\\Lib\\site-packages\\tqdm\\auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html\n",
      "  from .autonotebook import tqdm as notebook_tqdm\n",
      "Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.\n",
      "c:\\Users\\SK\\OneDrive\\Desktop\\emotions\\ai_env\\Lib\\site-packages\\huggingface_hub\\file_download.py:138: UserWarning: `huggingface_hub` cache-system uses symlinks by default to efficiently store duplicated files but your machine does not support them in C:\\Users\\SK\\.cache\\huggingface\\hub\\models--bhadresh-savani--bert-base-uncased-emotion. Caching files will still work but in a degraded version that might require more space on your disk. This warning can be disabled by setting the `HF_HUB_DISABLE_SYMLINKS_WARNING` environment variable. For more details, see https://huggingface.co/docs/huggingface_hub/how-to-cache#limitations.\n",
      "To support symlinks on Windows, you either need to activate Developer Mode or to run Python as an administrator. In order to activate developer mode, see this article: https://docs.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development\n",
      "  warnings.warn(message)\n",
      "Loading weights: 100%|██████████| 201/201 [00:00<00:00, 2754.65it/s]\n",
      "\u001b[1mBertForSequenceClassification LOAD REPORT\u001b[0m from: bhadresh-savani/bert-base-uncased-emotion\n",
      "Key                          | Status     |  | \n",
      "-----------------------------+------------+--+-\n",
      "bert.embeddings.position_ids | UNEXPECTED |  | \n",
      "\n",
      "Notes:\n",
      "- UNEXPECTED:\tcan be ignored when loading from different task/architecture; not ok if you expect identical arch.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model loaded successfully!\n",
      "      label     score\n",
      "0       joy  0.998776\n",
      "1      love  0.000394\n",
      "2   sadness  0.000332\n",
      "3  surprise  0.000232\n",
      "4     anger  0.000178\n",
      "5      fear  0.000087\n"
     ]
    }
   ],
   "source": [
    "from transformers import pipeline\n",
    "import pandas as pd\n",
    "\n",
    "# 'return_all_scores' ki jagah 'top_k=None' use karein\n",
    "classifier = pipeline(\n",
    "    \"text-classification\", \n",
    "    model=\"bhadresh-savani/bert-base-uncased-emotion\", \n",
    "    top_k=None\n",
    ")\n",
    "\n",
    "print(\"Model loaded successfully!\")\n",
    "\n",
    "# Test karne ke liye ek sample text\n",
    "text = \"I am so happy to learn AI today!\"\n",
    "results = classifier(text)\n",
    "\n",
    "# Results ko sundar dikhane ke liye DataFrame ka use karein\n",
    "df = pd.DataFrame(results[0])\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "45ee7c14",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: I am so excited about this new project, but a little nervous too!\n",
      "Top Emotion: joy (Confidence: 0.59)\n"
     ]
    }
   ],
   "source": [
    "def detect_emotion(text):\n",
    "    results = classifier(text)\n",
    "    \n",
    "    # Sort results by score in descending order\n",
    "    sorted_results = sorted(results[0], key=lambda x: x['score'], reverse=True)\n",
    "    \n",
    "    return sorted_results\n",
    "\n",
    "# Quick Test\n",
    "sample_text = \"I am so excited about this new project, but a little nervous too!\"\n",
    "predictions = detect_emotion(sample_text)\n",
    "\n",
    "print(f\"Text: {sample_text}\")\n",
    "print(f\"Top Emotion: {predictions[0]['label']} (Confidence: {predictions[0]['score']:.2f})\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4b6e7034",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Text</th>\n",
       "      <th>Emotion</th>\n",
       "      <th>Confidence</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>I love spending time with my family.</td>\n",
       "      <td>joy</td>\n",
       "      <td>0.9753</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>The traffic today was absolutely frustrating.</td>\n",
       "      <td>anger</td>\n",
       "      <td>0.7557</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>I'm worried about the upcoming exam.</td>\n",
       "      <td>fear</td>\n",
       "      <td>0.9910</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Wow, I didn't expect that to happen!</td>\n",
       "      <td>joy</td>\n",
       "      <td>0.7298</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                            Text Emotion  Confidence\n",
       "0           I love spending time with my family.     joy      0.9753\n",
       "1  The traffic today was absolutely frustrating.   anger      0.7557\n",
       "2           I'm worried about the upcoming exam.    fear      0.9910\n",
       "3           Wow, I didn't expect that to happen!     joy      0.7298"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = [\n",
    "    \"I love spending time with my family.\",\n",
    "    \"The traffic today was absolutely frustrating.\",\n",
    "    \"I'm worried about the upcoming exam.\",\n",
    "    \"Wow, I didn't expect that to happen!\"\n",
    "]\n",
    "\n",
    "results_list = []\n",
    "\n",
    "for text in data:\n",
    "    top_emotion = detect_emotion(text)[0]\n",
    "    results_list.append({\n",
    "        \"Text\": text,\n",
    "        \"Emotion\": top_emotion['label'],\n",
    "        \"Confidence\": round(top_emotion['score'], 4)\n",
    "    })\n",
    "\n",
    "df = pd.DataFrame(results_list)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "ai_env (3.13.3)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
