from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
from models.product import Product,Base

client = FaunaClient(secret="fnAFNAjjZsAAzcxXOiKy6hcr8WiJQ6j9-DtnTzpp",domain="db.eu.fauna.com")

result = client.query(
    q.create(
        q.collection("my_collection"),
        {"data":{"name":"Jane","age":134}}
    )
)