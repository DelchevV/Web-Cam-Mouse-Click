import asyncio
import websockets
from aiohttp import web
from mouse_reader import get_mouse_coordinates
from webcam_capture import capture_webcam_image
from database import save_to_database

async def handle(request):
    return web.Response(text=open('index.html').read(), content_type='text/html')

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    while True:
        mouse_coords = get_mouse_coordinates()
        image_data = capture_webcam_image()

        await ws.send_str(f"Mouse Coordinates: {mouse_coords}")

        await asyncio.sleep(1)

app = web.Application()
app.add_routes([web.get('/', handle), web.get('/ws', websocket_handler)])

if __name__ == '__main__':
    web.run_app(app)
