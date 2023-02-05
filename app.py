import datetime, os
from flask import Flask
from mongoengine import DateTimeField, Document, IntField, StringField, connect
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv(override=True)

mongo_host = os.getenv("DB_HOST")
mongo_db = os.getenv("DB")
mongo_user = os.getenv("DB_USER")
mongo_password = os.getenv("DB_PASSWORD")
sleep_time = os.getenv("SLEEP_TIME", default=0)

print(f"Connecting to {mongo_host} as {mongo_user}")
connect(
    db=mongo_db,
    host=mongo_host,
    username=mongo_user,
    password=mongo_password,
    retryWrites=False,
)


class CatBreed(Document):
    breed = StringField(required=True, max_length=64)
    style = StringField(max_length=255)
    sub_species_count = IntField()
    last_updated = DateTimeField()


@app.route("/", methods=["GET"])
def get_index():
    return {}


@app.route("/create", methods=["GET"])
def create_cat():
    cat = CatBreed(
        breed="Siamese",
        style="Sassy",
        last_updated=datetime.datetime.now(datetime.timezone.utc),
        sub_species_count=5,
    )
    cat.save()
    return_cat = cat.to_mongo().to_dict()
    return_cat["id"] = str(cat.id)
    return_cat.pop("_id")
    return return_cat