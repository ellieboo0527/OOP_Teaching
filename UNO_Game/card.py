# This class represents one UNO card

class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def can_play_on(self, top_card):
        return self.color == top_card.color or self.value == top_card.value

    def get_color_code(self):
        if self.color == "Red":
            return "\033[31m"
        elif self.color == "blue":
            return "\033[34m"
        elif self.color == "Green":
            return "\033[32m"
        elif self.color == "Yellow":
            return "\033[33m"
        else:
            return "\033[0m"

    def __str__(self):
        color_code = self.get_color_code()
        reset_code = "\033[0m"

        color_text = str(self.color).upper()
        value_text = str(self.value).upper()

        card_text = (
            "╭───────────╮\n"
            f"│ {color_text:<9} │\n"
            "│           │\n"
            f"│ {value_text:^9} │\n"
            "│           │\n"
            f"│ {color_text:>9} │\n"
            "╰───────────╯"
        )

        return color_code + card_text + reset_code