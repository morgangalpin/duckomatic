import { Injectable } from "@angular/core";

import { SocketService } from "../shared";

@Injectable()
export class CameraService {

    namespace:string = 'camera';
    cameraEvent:string = 'feed';
    // namespace:string = 'test';
    // cameraEvent:string = 'my_response';
    // socket: SocketIOClient.Socket;

    constructor(
        private socketService: SocketService
    ) {
        console.log('CameraService.constructor()');
        this.socketService.connect(this.namespace, 'CameraService.socketService');
    }

    onProcessCameraEvent(callback) : void {
        console.log('CameraService.onProcessCameraEvent("%s")', this.cameraEvent);
        this.socketService.on(this.cameraEvent, callback);
    }

    processEvent(currentCamera:number): void {
    }
}