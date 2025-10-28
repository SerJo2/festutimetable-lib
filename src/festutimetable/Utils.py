class Utils:
    @staticmethod
    def delete_redundant_chars(text: str):
        text = text.strip().rstrip().replace("\n", "")
        return text
