Week 4: Intro to LLMs
Summary
I dove deeper into LLMs this week, exploring embeddings, tokenization, and prompt engineering. To truly grasp next-token prediction, I built a toy tokenizer and a simple n-gram model from scratch. Next up: testing actual LLM APIs!

Resources I Used

Intro to LLM Video: Re-watched this just to refresh my memory on the core concepts.

LLM Tutorial Video: Focused heavily on the practical side of things, specifically tokenization, embeddings, and how prompting and fine-tuning actually work in the real world.

What I Got Done

Going Deeper into LLMs: I recapped tokens and self-attention, then dug into embeddings (how words are converted into dense vectors so similar words group together) and context windows.

Prompting vs. Fine-Tuning: Figured out the difference between tweaking a model's weights (fine-tuning) versus just giving a frozen model better instructions (zero-shot/few-shot prompting). I also looked into model limitations, like hallucinations and prompt sensitivity. All my detailed notes are in notes_llm_basics.md.

The Full Pipeline: I mapped out exactly how text flows through the system: tokenization → embeddings → model → output tokens → decoded text. I saved these walkthrough notes in llm_tutorial_notes.md.

Hands-on Practice
Since I learn best by doing, I built a simple n-gram language model from scratch. It really helped me get an intuitive feel for "next-token prediction" without getting lost in all the Transformer complexity. I also wrote a basic toy tokenizer to see exactly how raw text gets chopped up before hitting the model. All of this code is in ngram_language_model_demo.py.
