import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { ServerRequestService } from './server-request.service';
import { PushButtonComponent } from './push-button/push-button.component';
import { SensorComponent } from './sensor/sensor.component'

@NgModule({
  declarations: [
    AppComponent,
    PushButtonComponent,
    SensorComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    HttpClientModule
  ],
  providers: [ServerRequestService],
  bootstrap: [AppComponent]
})
export class AppModule { }
