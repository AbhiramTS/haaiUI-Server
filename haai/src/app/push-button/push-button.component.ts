import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { ServerRequestService } from '../server-request.service'

let clicked: boolean;

@Component({
  selector: 'app-push-button',
  templateUrl: './push-button.component.html',
  styleUrls: ['./push-button.component.scss']
})
export class PushButtonComponent implements OnInit {
  @Input() public id: string;


  constructor(private request: ServerRequestService) { }

  ngOnInit() {
  }

  handleClick() {
    console.log('hey I am  clicked in child');
    console.log(this.id);
    this.request.mqttResponce(this.id);
  }

}
