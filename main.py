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
    print(request)

    x = request.query_params['x']
    y = request.query_params['y']
    #Select sample points
    sample_points = [[float(x), float(y)]]
    # make sure mapings between d3 and latent map match
    # sample_points = [[7, 8]]
    # sample_points = [[7, 8], [18, -18],
                    #  [18, -7], [7, -30], [39, -10], [17, 10]]
    '''
    sample_points = [[11.7 , 8.9, 12.8, 16.2,- 2.6,- 4.3,- 9.1, 21.0],
                    [- 8.0 , 9.6,-23.6, 20.0, 13.5,  8.0,-14.6,  3.1],
                    [-11.6 , 5.9,- 9.0,- 0.5,-25.4,-15.3,  3.1,  4.9],
                    [  6.3 , 3.9,  2.1,  9.1,-16.4,-13.8,- 1.8, 10.9]]
                    '''

    #Select path for saving chords
    chord_saving_path = './midi/new'

    filename=generate_chord_from_trained_model(trained_model_path,
                                      latent_dim,
                                      sample_points,
                                      chord_saving_path,model,spec_helper)

    return FileResponse(filename)

middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'], 
    allow_methods=["GET","OPTIONS"],
    allow_headers=["*"]),
    Middleware(GZipMiddleware, minimum_size=1000),
]

app = Starlette(debug=True, routes=[
    Route('/', home),
    Route('/sample', sample),
    Route('/generate', generate_midi),
    ],
    middleware=middleware
)
