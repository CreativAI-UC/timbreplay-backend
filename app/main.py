from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse
from starlette.responses import FileResponse


async def homepage(request):
    return JSONResponse({"message": "Hello World!"})


async def generate_midi(request):
    return FileResponse('midi/file_example_WAV_10MG.wav')


app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/generate', generate_midi),
])
