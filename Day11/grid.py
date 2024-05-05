class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def print_grid(self):
        for row in self.rows:
            print(row)

    @classmethod
    def from_text(cls, values):
        rows = [list(map(str, line.split())) for line in values.split('\n')]
        columns = len(rows[0]) if rows else 0
        return cls(rows, columns)