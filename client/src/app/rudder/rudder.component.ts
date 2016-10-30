import { Component, OnInit } from '@angular/core';

import { RudderService } from './rudder.service';

@Component({
    selector: 'app-rudder',
    templateUrl: './rudder.component.html',
    styleUrls: ['./rudder.component.css']
})
export class RudderComponent implements OnInit {

    currentRudder: number;

    constructor(
        private rudderService: RudderService
    ) {}

    setRudder(value: number) {
        if (value != this.currentRudder) {
            console.log("Changing rudder value from: " + this.currentRudder + " to " + value)
            this.currentRudder = value;
            this.rudderService.setRudder(value);
        }
    }

    ngOnInit() {
        this.currentRudder = 0;
    }
}
