def SocketHandler(sio):
    @sio.event
    
    def event(message,payload):
        sio.emit(message,payload)


    @sio.on('connect')
    def connect():
            sio.emit('connect')

