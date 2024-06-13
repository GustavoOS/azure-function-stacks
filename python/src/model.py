from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Base(DeclarativeBase):
    pass


class Content(Base):
    __tablename__ = "content"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    color: Mapped[str] = mapped_column(String(7))
    title: Mapped[str] = mapped_column(String(25))

    def __repr__(self) -> str:
        return f"Content(id={self.id!r}, title={self.title!r}, color={self.color!r})"


# Create the engine
