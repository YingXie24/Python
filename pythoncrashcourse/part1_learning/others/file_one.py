#  Module to understand __name__ = "__main__" idiom

import file_two

print(f"File one __name__ is set to: {__name__}")

if __name__ == "__main__":
    print("File one executed when run directly.")
else: 
    print("File one executed when imported.")