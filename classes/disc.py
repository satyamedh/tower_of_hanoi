class Disc:
    def __init__(self, size: int) -> None:
        self.size = size
    
    def __gt__(self, other) -> bool:
        assert isinstance(other, Disc)
        return self.size > other.size
    
    def __lt__(self, other) -> bool:
        assert isinstance(other, Disc)
        return self.size < other.size
    
    def __ge__(self, other) -> bool:
        assert isinstance(other, Disc)
        return self.size >= other.size
    
    def __le__(self, other) -> bool:
        assert isinstance(other, Disc)
        return self.size >= other.size
    
    def __eq__(self, other) -> bool:
        assert isinstance(other, Disc)
        return self.size == other.size
    
    def __ne__(self, other) -> bool:
        assert isinstance(other, Disc)
        return self.size != other.size  
    
    def __str__(self) -> str:
        return str(self.size)
