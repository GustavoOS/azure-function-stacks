import os
import traceback
from venv import logger
import azure.functions as func
import logging
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
from sqlalchemy import create_engine, select

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy.exc import NoResultFound
import json


#  database connection
load_dotenv()

url = os.getenv("DATABASE_URL").replace("postgres://", "postgresql://")
if url is None or url == "":
    raise ValueError("DATABASE_URL is not set")

engine = create_engine(url)

# Create a session factory
Session = sessionmaker(bind=engine)

# # Create a session
session = Session()

# # Model


class Base(DeclarativeBase):
    pass


class Content(Base):
    __tablename__ = "content"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    color: Mapped[str] = mapped_column(String(7))
    title: Mapped[str] = mapped_column(String(25))

    def __repr__(self) -> str:
        return f"Content(id={self.id!r}, title={self.title!r}, color={self.color!r})"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# Functions
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="hello", methods=["GET"])
def hello(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(f"Hello, World!")


@app.route(route="content", methods=["GET"])
def content(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        id = int(req.params.get('id', "s"))
        stmt = select(Content).filter_by(id=id)
        res = session.execute(stmt).scalar_one()
        json_res = json.dumps(res.as_dict())
        return func.HttpResponse(json_res, status_code=200)
    except ValueError:
        return func.HttpResponse("Invalid id", status_code=400)
    except NoResultFound:
        return func.HttpResponse("Not found", status_code=404)
    except Exception as e:
        logger.error(e)
        traceback.print_exc()
        return func.HttpResponse("", status_code=500)


@app.route(route="content", methods=["POST"])
def create(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        body = req.get_json()
        content = Content(color=body['color'], title=body['title'])
        session.add(content)
        session.commit()
        return func.HttpResponse(json.dumps(content.as_dict()), status_code=201)
    except KeyError:
        return func.HttpResponse("Missing parameters", status_code=400)
    except Exception as e:
        traceback.print_exc()
        logger.error(e)
        return func.HttpResponse("", status_code=500)


@app.route(route="content", methods=["PUT"])
def update(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        id = int(req.params.get('id', "s"))
        body = req.get_json()
        color = body['color']
        title = body['title']
        stmt = select(Content).filter_by(id=id)
        content = session.execute(stmt).scalar_one()
        content.color = color
        content.title = title
        session.commit()
        return func.HttpResponse(json.dumps(content.as_dict()), status_code=200)
    except ValueError:
        return func.HttpResponse("Invalid id", status_code=400)
    except NoResultFound:
        return func.HttpResponse("Not found", status_code=404)
    except KeyError:
        return func.HttpResponse("Missing parameters", status_code=400)
    except Exception as e:
        logger.error(e)
        traceback.print_exc()
        return func.HttpResponse("", status_code=500)


@app.route(route="content", methods=["DELETE"])
def delete(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        id = int(req.params.get('id', "s"))
        content = session.get(Content, id)
        session.delete(content)
        session.commit()
        return func.HttpResponse("Deleted", status_code=200)
    except ValueError:
        return func.HttpResponse("Invalid id", status_code=400)
    except NoResultFound:
        return func.HttpResponse("Not found", status_code=404)
    except Exception as e:
        logger.error(e)
        traceback.print_exc()
        return func.HttpResponse("", status_code=500)
