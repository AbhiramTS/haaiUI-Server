import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  public pin: string;
  pinName = ['PinD0', 'PinD1', 'PinD2', 'PinD3'];
  listOfPins:string[][] =[];
  
  ngOnInit() {
    while(this.pinName.length > 0){
      this.listOfPins.push(this.pinName.splice(0, 2));
    }
    console.log("listOfPins", this.listOfPins);
  }

  title = 'haai';
}
