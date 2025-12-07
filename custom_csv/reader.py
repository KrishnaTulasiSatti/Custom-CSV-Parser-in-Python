class CustomCSVReader:
    """
    Custom CSV Reader that:
    - Parses CSV character-by-character
    - Handles quoted fields, escaped quotes, and embedded newlines
    - Streams the file (does not load entire file into memory)
    - Works as an iterator (like csv.reader)
    - Also supports custom delimiter
    """

    def __init__(self, filepath, delimiter=",", encoding="utf-8"):
        self.file = open(filepath, "r", encoding=encoding)
        self.delimiter = delimiter
        self.buffer = ""
        self.row = []
        self.in_quotes = False
        self.end_of_file = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.end_of_file:
            raise StopIteration

        self.buffer = ""
        self.row = []
        self.in_quotes = False

        while True:
            char = self.file.read(1)

            if char == "":
                if self.buffer or self.row:
                    self.row.append(self._clean_field(self.buffer))
                    return self.row
                self.end_of_file = True
                self.file.close()
                raise StopIteration

            # Handle quoted fields
            if char == '"':
                if not self.in_quotes:
                    self.in_quotes = True
                    self.buffer += char # Add opening quote to buffer 
                    continue
                else:
                    next_char = self.file.read(1)
                    if next_char == '"':  # escaped quote: "" -> "
                        self.buffer += '""' # Add both quotes to buffer 
                        continue
                    else:  # Closing quote: " followed by delimiter or newline
                        self.buffer += char # Add closing quote to buffer 
                        self.in_quotes = False # End of quoted field
                        
                        if next_char == "": # EOF after closing quote
                            char = next_char
                        elif next_char in ("\n", "\r"): # Newline after closing quote
                            char = next_char
                        elif next_char == self.delimiter: # Delimiter after closing quote
                            char = next_char
                        else: 
                            self.buffer += next_char
                            continue # Continue reading the rest of the field

            # Handle delimiter
            if char == self.delimiter and not self.in_quotes:
                self.row.append(self._clean_field(self.buffer))
                self.buffer = ""
                continue

            # Handle newlines
            if char in ("\n", "\r") and not self.in_quotes:
                # Handle empty line
                if not self.buffer and not self.row:
                    continue
                # Handle field ending with newline
                self.row.append(self._clean_field(self.buffer))
                return self.row

            # Append character to buffer (if not handled by continue)
            self.buffer += char

    def _clean_field(self, field):
        """Remove surrounding quotes and convert escaped quotes to single quote"""
        field = field.strip()
        if len(field) >= 2 and field[0] == '"' and field[-1] == '"':
            field = field[1:-1].replace('""', '"')
        return field