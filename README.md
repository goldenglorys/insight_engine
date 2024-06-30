<h1 align="center">
📖 Insight Engine: Your Local AI Document Whisperer
</h1>

## 🚀 Welcome to the Document Interrogation Party!

Ever wished you could grill your documents like a seasoned detective? Well, grab your magnifying glass and your favorite beverage, because Insight Engine is here to turn you into the Sherlock Holmes of your digital library!

## 🎭 What's This Magic All About?

Insight Engine is your personal document confidant, powered by the mystical LLAMA3 (running on [Ollama](https://ollama.com/), because we like our LLAMAs local and caffeinated). It's here to help you uncover the secrets hidden in your PDFs, DOCXs, and TXTs faster than you can say "elementary, my dear Watson!"

### 🔑 Key Features (aka Why You'll Love It)

- 📁 Document Whispering: Upload PDFs, DOCXs, and TXTs. It doesn't discriminate against file types (yet).
- 💬 Question Time: Ask your documents anything. They've been dying to spill their secrets!
- 📚 Instant Citations: It don't just give answers, it show the work. Your high school teachers would be proud.
- 🔍 Semantic Sorcery: The search is so smart, it probably aced its SATs.
- 🦙 LLAMA3 on Ollama: All the power of AI, none of the cloud-based trust issues. Your data stays at home, like a good little secret.

## 🧠 How It Tickle Your Documents' Brain Cells

1. **Chunk-a-licious**: It slice and dice your docs into bite-sized pieces. Yum!
2. **Vector Voodoo**: These chunks get turned into magic numbers (vectors) and stored in a super-secret clubhouse (index).
3. **Question Quests**: Your burning questions get the same vector treatment.
4. **Matchmaking**: It play matchmaker between your question and the most relevant document chunks.
5. **LLAMA Time**: Your local LLAMA3 (on Ollama) works its magic, turning those chunks into coherent answers.
6. **Show and Tell**: It don't just give you answers, it show you where it found them. Trust issues? It's got you covered!

## 🏗️ Setting Up Your Own Document Interrogation Chamber

### 🧰 Prerequisites (aka What You Need to Join The Club)

- Python 3.8+ (because we're not savages)
- [Poetry](https://python-poetry.org/) (for corralling our dependencies like a boss)
- [Ollama](https://ollama.com/)  - and pull llama(x) model (because we like our LLAMAs local and free-range)

### 🔧 Installation (Don't Worry, No Assembly Required)

1. Clone the repository 📂

```bash
git clone https://github.com/goldenglorys/insight_engine
cd insight_engine
```

2. Let Poetry work its magic 🔨

```bash
poetry install
poetry shell
```

3. Run the Streamlit server 🚀

```bash
cd engine
streamlit run main.py
```

4. Point your favorite browser to http://localhost:8501 and watch the fireworks!

5. Upload a document, ask it your deepest, darkest questions, and prepare to be amazed!


## 🚀 Coming Soon to a Repository Near You

- 🕸️ Web page support (because PDFs shouldn't have all the fun)
- 📊 PPTX parsing (death by PowerPoint, no more!)
- 🔦 Citation highlighting (like a textual disco ball)
- 📝 OCR powers (because sometimes PDFs are just glorified images)
- 🔗 Mix and match your own AI cocktail (chain types for the adventurous)
- 📏 Adjustable chunk sizes (for those who like their information bite-sized or super-sized)
- 🦙 Model Menagerie: Choose your AI companion! Whether you prefer your Llama extra fluffy (70B), 
  bite-sized (7B), or with a side of Alpaca, we've got you covered. Soon you'll be able to swap 
  models faster than a chameleon changes colors. Fancy a chat with Mistral? Or perhaps you're in 
  the mood for some Orca-stration? Your wish is our command! Remember, in the world of Ollama, 
  variety is the spice of AI life. Just don't expect them to do your laundry... yet.

## 📜 License to Thrill
This project is licensed under the MIT License - see the LICENSE file for the legal mumbo-jumbo.

## 🎩 Tip of the Hat

- Built on the shoulders of [Streamlit](https://streamlit.io/) giants
- Powered by [LLAMA3](https://github.com/meta-llama/llama3) (the AI, not the animal)
- Inspired by every student who's ever said, "I don't want to read the whole thing!"
- A nod to our knowledge-hungry cousin, [KnowledgeGPT](https://github.com/mmz-001/knowledge_gpt/) 

Remember, imitation is the sincerest form of flattery, but we've added our own secret sauce. 
It's like we took their recipe, added some local Llama spice, and voila! A whole new dish. 
Bon appétit, knowledge seekers!