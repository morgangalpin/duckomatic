import { Injectable } from "@angular/core";

import { SocketService } from "../shared";

@Injectable()
export class RudderService {

    namespace:string = 'rudder';
    rudderEvent:string = 'update';

    constructor(
        private socketService: SocketService
    ) {
        // console.log('RudderService.constructor()');
        this.socketService.connect(this.namespace, 'RudderService.socketService');
    }

    setRudder(value:number): void {
        // console.log('RudderService.setRudder(' + value + ')');
        this.socketService.socket.emit(this.rudderEvent, { rudder: value });
    }
}