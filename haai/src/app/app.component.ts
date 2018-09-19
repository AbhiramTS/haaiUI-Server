import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  public pin: string;
  listOfPins = ['PinD0', 'PinD1', 'PinD2', 'PinD3'];

  title = 'haai';
}
