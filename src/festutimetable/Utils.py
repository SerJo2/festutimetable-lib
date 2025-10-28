class Utils:
    @staticmethod
    def delete_redundant_chars(text: str):
        """Remove whitespace and newline characters from text

        Removes leading/trailing whitespace and all newline characters
        from the input text.

        Args:
            text: Input text to clean

        Returns:
            str: Cleaned text without extra whitespace or newlines
        """
        text = text.strip().rstrip().replace("\n", "")
        return text
