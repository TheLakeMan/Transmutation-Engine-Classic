import random
import re
from collections import Counter
import numpy as np

class Transmutator:
    def __init__(self, cycles=5, entropy=1.5, stabilization=0.3):
        self.cycles = cycles
        self.entropy = entropy          # 0.1 = low chaos, 1.5 = high chaos
        self.stabilization = stabilization  # 0.1 = almost no damping, 0.8 = strong logic

    def mutate_prompt(self, prompt: str, cycle: int, is_entropy_phase: bool = True) -> str:
        """Local mutation without any external API"""
        lines = prompt.split('\n')
        
        if is_entropy_phase:
            # High entropy = wild poetic / cosmic mutation
            chaos = int(self.entropy * 8)  # more entropy = more changes
            for _ in range(chaos):
                if random.random() < 0.6:
                    # Replace words with cosmic synonyms
                    cosmic_words = ["quantum", "cosmic", "primordial", "aetheric", "void", "singularity", 
                                  "entropic", "ontic", "gnosis", "akasha", "fractal", "resonance"]
                    idx = random.randint(0, len(lines)-1)
                    if lines[idx].strip():
                        words = lines[idx].split()
                        if words:
                            pos = random.randint(0, len(words)-1)
                            words[pos] = random.choice(cosmic_words)
                            lines[idx] = ' '.join(words)
                else:
                    # Add poetic prefix/suffix
                    prefixes = ["Behold, ", "From the void emerges: ", "In the quantum foam: ", "The singularity whispers: "]
                    lines.insert(random.randint(0, len(lines)), random.choice(prefixes))
        else:
            # Stabilization phase — try to make it more logical/coherent
            damp = self.stabilization
            for i in range(len(lines)):
                if random.random() < damp:
                    # Remove excessive cosmic fluff
                    lines[i] = re.sub(r'\b(quantum|cosmic|primordial|aetheric|void|singularity)\b', '', lines[i])
                    lines[i] = re.sub(r'\s+', ' ', lines[i]).strip()
        
        return '\n'.join(lines)

    def run_transmutation(self, source_anchor: str):
        current = source_anchor
        report = {"cycles": []}

        for cycle in range(1, self.cycles + 1):
            entropy_mut = self.mutate_prompt(current, cycle, is_entropy_phase=True)
            stabilized = self.mutate_prompt(entropy_mut, cycle, is_entropy_phase=False)

            report["cycles"].append({
                "cycle": cycle,
                "entropy_phase": entropy_mut,
                "stabilization_phase": stabilized
            })
            current = stabilized

        report["final"] = current
        return report

    def validate_autogram(self, sentence: str) -> dict:
        """Strict autogram validator"""
        sentence = re.sub(r'[^\w\s]', ' ', sentence.lower())
        sentence = re.sub(r'\band\b', ' ', sentence)
        sentence = re.sub(r'\s+', ' ', sentence).strip()

        claimed = {}
        parts = sentence.split()
        i = 0
        while i < len(parts) - 1:
            num_word = parts[i]
            letter = parts[i + 1].strip('-')
            num_map = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5,
                       "six":6, "seven":7, "eight":8, "nine":9, "ten":10}
            if num_word in num_map and letter.isalpha() and len(letter) == 1:
                claimed[letter] = num_map[num_word]
            i += 2

        actual = Counter(c for c in sentence if c.isalpha())

        report = {let: {"claimed": claimed.get(let, 0), "actual": actual.get(let, 0)}
                  for let in 'abcdefghijklmnopqrstuvwxyz'}
        valid = all(r["claimed"] == r["actual"] for r in report.values())
        return {"valid": valid, "report": report}
