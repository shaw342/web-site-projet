import sys

sys.path.append("models")

from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
from product import Product, Base
from users import User

client = FaunaClient(secret="fnAFNAjjZsAAzcxXOiKy6hcr8WiJQ6j9-DtnTzpp",domain="db.eu.fauna.com")
user = User(username='shawan',email ="1234bd@gmail.com",password="12345678SBSB")
result = client.query(
    q.create(
        q.collection("my_collection"),
        {"data": {"surname": user.username, "email": user.email}}
    )
)
