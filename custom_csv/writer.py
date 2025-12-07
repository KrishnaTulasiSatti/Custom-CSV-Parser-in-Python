class CustomCSVWriter:
    def __init__(self, filepath, encoding="utf-8", delimiter=","):
        self.filepath = filepath
        self.encoding = encoding
        self.delimiter = delimiter
        self.file = open(filepath, "w", encoding=encoding, newline="")

    def _escape_field(self, field):
        field_str = str(field)

        # Needs quoting if special chars exist
        if any(c in field_str for c in [self.delimiter, '"', '\n']):
            field_str = field_str.replace('"', '""')  # escape double quotes
            field_str = f'"{field_str}"'
        return field_str

    def write_row(self, row):
        """Write a single row."""
        escaped_row = [self._escape_field(field) for field in row]
        line = self.delimiter.join(escaped_row) + "\n"
        self.file.write(line)

    def write_rows(self, rows):
        """Write multiple rows."""
        for row in rows:
            self.write_row(row)

    def close(self):
        """Close file manually."""
        self.file.close()