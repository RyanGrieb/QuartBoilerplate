from quart import (
    Quart,
    render_template,
)
from quart_session import Session


# Configure quart
server = Quart(__name__)
server.secret_key = "opnqpwefqewpfqweu32134j32p4n1234d"

Session(server)


@server.route("/", methods=["GET"])
async def home():
    return await render_template("index.html")


if __name__ == "__main__":
    server.run()
