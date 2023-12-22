try: 
    import pyperclip
    def clippy(message):
        """
        Copies the given message to the clipboard and prints it.

        Args:
            message (str): The message to be copied to the clipboard.

        Returns:
            None
        """
        pyperclip.copy(message)
        print(f'{message} \n\n📎OK')
except ImportError:
    def clippy(message):
        """Prints the message to the console."""
        print(message)

ask = clippy