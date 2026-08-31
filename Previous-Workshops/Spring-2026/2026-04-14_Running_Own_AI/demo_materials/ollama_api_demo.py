#!/usr/bin/env python3
"""
Demo 6: Local API Integration — Batch-process abstracts with Ollama

This script demonstrates calling Ollama's local REST API from Python.
No API keys needed — the model runs on your machine.

Requirements:
    pip install requests
    # Ollama must be running: ollama serve

Usage:
    python ollama_api_demo.py
"""

import requests
import json
import sys
import time


def ask_ollama(prompt, model="llama3.2:3b", temperature=0.7):
    """Send a prompt to the local Ollama server and get a response."""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "options": {"temperature": temperature},
            },
            timeout=120,
        )
        response.raise_for_status()
        data = response.json()
        return data["response"]
    except requests.exceptions.ConnectionError:
        return "[ERROR] Cannot connect to Ollama. Is it running? (ollama serve)"
    except Exception as e:
        return f"[ERROR] {e}"


def demo_basic():
    """Part 1: Basic API call."""
    print("=" * 60)
    print("PART 1: Basic API Call")
    print("=" * 60)
    result = ask_ollama("What is the Berry phase? One sentence.")
    print(f"\nQ: What is the Berry phase?\nA: {result}\n")


def demo_batch_review():
    """Part 2: Batch-check abstract sentences for informality."""
    print("=" * 60)
    print("PART 2: Batch Abstract Quality Check")
    print("=" * 60)

    abstracts = [
        "We show that the system exhibits a pretty large gap of 0.5 eV.",
        "Our calculations demonstrate that spin-orbit coupling plays a crucial role.",
        "Basically, we found three distinct phases in the phase diagram.",
        "The results indicate a topological phase transition at critical strain.",
        "We think the Chern number changes from 1 to 0 at the transition.",
    ]

    REVIEW_PROMPT = """You are a journal editor for Physical Review B. Check this
abstract sentence for informality or vague language. If it's fine, say "OK".
If not, quote the problematic phrase and suggest a replacement.
Be concise (1-2 sentences max).

Sentence: {sentence}"""

    for i, sentence in enumerate(abstracts, 1):
        result = ask_ollama(
            REVIEW_PROMPT.format(sentence=sentence),
            temperature=0.0,  # deterministic for consistency
        )
        status = "OK" if "ok" in result[:20].lower() else "FIX"
        print(f"\n[{status}] Sentence {i}: {sentence[:65]}...")
        print(f"  Review: {result.strip()[:200]}")


def demo_temperature():
    """Part 3: Show temperature effects."""
    print("\n" + "=" * 60)
    print("PART 3: Temperature Effects")
    print("=" * 60)

    prompt = "Write one sentence about superconductivity in magic-angle graphene."

    for temp in [0.0, 0.7, 1.5]:
        print(f"\n--- Temperature {temp} ---")
        result = ask_ollama(prompt, temperature=temp)
        print(f"  {result.strip()[:200]}")


if __name__ == "__main__":
    print("\nOllama Local API Demo")
    print("D-Lab AI Pulse Workshop — Session 7\n")

    # Check if Ollama is running
    try:
        requests.get("http://localhost:11434/api/tags", timeout=5)
        print("✓ Ollama is running\n")
    except requests.exceptions.ConnectionError:
        print("✗ Ollama is not running. Start it with: ollama serve")
        sys.exit(1)

    demo_basic()
    demo_batch_review()
    demo_temperature()

    print("\n" + "=" * 60)
    print("Done! All processing happened locally — no data left your machine.")
    print("=" * 60)
