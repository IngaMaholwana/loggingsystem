class User(Base):
    __tablename__ = "users"
    
    id: int
    username: str
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool