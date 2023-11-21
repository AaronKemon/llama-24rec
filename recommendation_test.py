# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

from typing import List, Optional

import fire

from llama import Llama, Dialog


def main(
    ckpt_dir: str,
    tokenizer_path: str,
    temperature: float = 0.6,
    top_p: float = 0.9,
    max_seq_len: int = 512,
    max_batch_size: int = 8,
    max_gen_len: Optional[int] = None,
):
    """
    Entry point of the program for generating text using a pretrained model.

    Args:
        ckpt_dir (str): The directory containing checkpoint files for the pretrained model.
        tokenizer_path (str): The path to the tokenizer model used for text encoding/decoding.
        temperature (float, optional): The temperature value for controlling randomness in generation.
            Defaults to 0.6.
        top_p (float, optional): The top-p sampling parameter for controlling diversity in generation.
            Defaults to 0.9.
        max_seq_len (int, optional): The maximum sequence length for input prompts. Defaults to 512.
        max_batch_size (int, optional): The maximum batch size for generating sequences. Defaults to 8.
        max_gen_len (int, optional): The maximum length of generated sequences. If None, it will be
            set to the model's max sequence length. Defaults to None.
    """
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )

    dialogs: List[Dialog] = [
        #[
            #{"role": "system", "content": "Always answer with ratings ranging from 1 to 5 stars, after providing the list of ranking, explain why you have this result"},
            #{"role": "user", "content": "I am a scientist, I want to watch 3 movies, they are Matrix, Avatar, and Forest Gamp, what maybe the ratings from me?"},
        #],
        [{"role": "user", "content": "Make recommendations for me. I'm new to classic literature. Can you recommend a few timeless novels that are essential for someone just starting in this genre? The recommendations should include the following subsections: Introductions of items, recommending relativity, target users, diversity. Each sections should be within 100 words."}],
         [{"role": "user", "content": "Make recommendations for me. As a new music enthusiast, could you suggest some iconic albums and artists from different decades and genres to help me explore and expand my musical taste? The recommendations should include the following subsections: Introductions of items, recommending relativity, target users, diversity. Each sections should be within 100 words."}],
        #[{"role": "user", "content": "Make recommendations for me. I've recently become interested in cooking. What are some beginner-friendly cookbooks or online cooking courses you'd recommend for a novice like me? The recommendations should include the following subsections: Introductions of items, recommending relativity, target users, diversity. Each sections should be within 100 words."}],
        #[{"role": "user", "content": "Make recommendations for me. I'm planning a weekend getaway in a scenic location. What are some picturesque destinations or travel experiences that are perfect for first-time travelers? The recommendations should include the following subsections: Introductions of items, recommending relativity, target users, diversity. Each sections should be within 100 words."}],
        #[{"role": "user", "content": 'Make recommendations for me. I want to start learning a new language. Which language-learning apps or resources would you suggest for a beginner? The recommendations should include the following subsections: Introductions of items, recommending relativity, target users, diversity. Each sections should be within 100 words.'}],
        
        #[{"role": "user", "content": "Make recommendations for me. I've just started a small vegetable garden. What are some easy-to-grow vegetables and herbs that I can cultivate successfully The recommendations should include the following subsections: Introductions of items, recommending relativity, target users, diversity. Each sections should be within 100 words."}],
        #[{"role": "user", "content": "Make recommendations for me. I'm looking for recommendations on introductory online courses for understanding basic concepts in data science. What are some beginner-level courses or platforms you'd recommend? The recommendations should include the following subsections: Introductions of items, recommending relativity, target users, diversity. Each sections should be within 100 words."}],
        #[{"role": "user", "content": "Make recommendations for me. I'm a beginner in the world of photography. Can you suggest some entry-level camera models and photography techniques to help me get started? The recommendations should include the following subsections: Introductions of items, recommending relativity, target users, diversity. Each sections should be within 100 words."}],
        #[{"role": "user", "content": "Make recommendations for me. I'm new to fitness and want to establish a workout routine. What are some beginner-friendly exercises and workout plans that I can follow to improve my fitness? The recommendations should include the following subsections: Introductions of items, recommending relativity, target users, diversity. Each sections should be within 100 words."}],
        #[{"role": "user", "content": "Make recommendations for me. I've recently discovered an interest in art and would like to explore famous artworks. Can you recommend art museums or online galleries where I can start my art journey? The recommendations should include the following subsections: Introductions of items, recommending relativity, target users, diversity. Each sections should be within 100 words."}],

    ]
    results = generator.chat_completion(
        dialogs,  # type: ignore
        max_gen_len=max_gen_len,
        temperature=temperature,
        top_p=top_p,
    )

    for dialog, result in zip(dialogs, results):
        for msg in dialog:
            print(f"{msg['role'].capitalize()}: {msg['content']}\n")
        print(
            f"> {result['generation']['role'].capitalize()}: {result['generation']['content']}"
        )
        print("\n==================================\n")


if __name__ == "__main__":
    fire.Fire(main)
