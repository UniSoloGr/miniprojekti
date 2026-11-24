class Source:
    def __init__(self, id, content):
        self.id = id
        self.content = content
        self.fields = self.parse_content(content)
    
    @staticmethod
    def parse_content(content: str) -> list[tuple[str, str]]:
        return [
            (name.strip(), value.strip())
            for line in content.splitlines()
            if ":" in line
            for name, value in [line.split(":", 1)]
        ]
        
    def __str__(self):
        return f"{self.content}"