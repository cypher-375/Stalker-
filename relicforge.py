import random

class RelicForge:
    def __init__(self, info_file=None):
        self.general = []
        self.higher_chance = []
        self.target_data = self.load_target_data(info_file)

    def load_target_data(self, path):
        data = {}
        if path:
            try:
                with open(path, "r") as f:
                    for line in f:
                        if "=" in line:
                            key, value = line.strip().split("=", 1)
                            data[key.strip()] = value.strip()
            except Exception as e:
                print(f"[!] Failed to load info file: {e}")
        return data

    def generate_passlists(self, count, length_range, style="random"):
        self.generate_higher_chance_passes()
        for _ in range(count):
            length = random.randint(*length_range)
            if style == "human":
                self.general.append(self.generate_human_pass(length))
            else:
                self.general.append(self.generate_general_pass(length))

    def generate_higher_chance_passes(self):
        combos = []
        values = [str(v) for v in self.target_data.values()]
        for val in values:
            combos.extend([
                val + "123", val + "!", val + "@2025", val.capitalize() + "!", val[::-1] + "99"
            ])
        self.higher_chance.extend(combos)

    def generate_general_pass(self, length):
        charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{};:,.<>?"
        return ''.join(random.choices(charset, k=length))

    def generate_human_pass(self, length):
        words = ["queen", "march", "shadow", "ruby", "black", "dps"]
        separators = ["_", ".", "-", ""]
        suffixes = ["99", "21", "88", "2025"]
        word = random.choice(words)
        sep = random.choice(separators)
        suffix = random.choice(suffixes)
        base = f"{word}{sep}{suffix}"
        if len(base) < length:
            pad = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=length - len(base)))
            return base + pad
        return base[:length]

    def save_passlists(self, format="txt"):
        if format == "txt":
            with open("higher_chance_passlist.txt", "w") as f:
                f.write("\n".join(self.higher_chance))
            with open("general_passlist.txt", "w") as f:
                f.write("\n".join(self.general))
