from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse
from starlette.responses import FileResponse
from TimbreNet.timbrenet_generate_chord import generate_chord_from_trained_model
from TimbreNet.lib.specgrams_helper import SpecgramsHelper
from TimbreNet.lib.model import CVAE as Model
from starlette.middleware import Middleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.background import BackgroundTask
import random
import os 

spec_helper = SpecgramsHelper(audio_length=64000,
                              spec_shape=(128, 1024),
                              overlap=0.75,
                              sample_rate=16000,
                              mel_downscale=1)

#Select trained model path
trained_model_path = './TimbreNet/trained_models/450_piano_chords/latent_2_lr_3e-05_epoch_385_of_501'
#trained_model_path = './trained_models/450_piano_chords/latent_8_lr_3e-05_epoch_141_of_501'

#Select latent dimension
latent_dim = 2
#latent_dim = 8

model = Model(latent_dim)
print('\n\nLoading Trained Model...')
model.load_weights(trained_model_path)
print('Success Loading Trained Model!\n')

async def home(request):
    return JSONResponse({"message":"Hi there! the server is up"})


async def sample(request):
    return FileResponse('midi/file_example_WAV_10MG.wav')


async def generate_midi(request):

    try:
        x = request.query_params['x']
        y = request.query_params['y']

        sample_points = [[float(x), float(y)]]
    except KeyError:
        return JSONResponse({"reason": "Expecting X and Y on query params"}, status_code=400)
    except ValueError:
        return JSONResponse({"reason": "Expecting a number for X and Y coordinates"}, status_code=400)


    #Select path for saving chords
    chord_saving_path = './midi/'

    filename=generate_chord_from_trained_model(trained_model_path,
                                      latent_dim,
                                      sample_points,
                                      chord_saving_path,model,spec_helper)

    deleteTask = BackgroundTask(remove_file, filename=filename)
    return FileResponse(filename,background=deleteTask)


async def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    wav_name=filename.replace(".mp3",".wav")
    if os.path.exists(wav_name):
        os.remove(wav_name)
    
middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'], 
    allow_methods=["GET","OPTIONS"],
    allow_headers=["*"]),
    Middleware(GZipMiddleware, minimum_size=400),
]

app = Starlette(debug=False, routes=[
    Route('/', home),
    Route('/sample', sample),
    Route('/generate', generate_midi),
    ],
    middleware=middleware
)
