import threading
from waitress import serve

from apis import app
# from core import start
from configs import ServerConfig

# I think I'll not do this one because it involves using
# a logger which honestly I don't completely understand
#def main():
#    start()

def start_server():
    serve(app, port=ServerConfig.port)

if __name__ == "__main__":
    # server_thread = threading.Thread(target=start_server)
    # server_thread.start()

    #main()

    # we get the app from apis, and we run it
    app.run(host="localhost", port=5000, debug=True) # get rid of host if you want it live





"""
Ok
So like
Here's how I would do this

AND THIS IS SUPPOSED TO BE APP.PY
OR RATHER, THE VERSION OF THIS THAT'S IN APIS

@route.app(root_api_url + "clickup/list/<list_id>")
def getList(list_id):
    Use the header and auth which should be in the ClickUp config
    Make a call to clickup
    Which usually goes like
    response = send....(bla bla)

    Then, let's process the response
    Get lists from ID
    Do some processing
    return csv

That's it
Bwahahahah!

Let's rewrite based on the example

NEXT STEPS
Put this in the ClickUp api
And then test running it before writing the logic






"""