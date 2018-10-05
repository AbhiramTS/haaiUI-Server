import { Component, OnInit } from '@angular/core';
import { Observable, interval } from 'rxjs';
import {HttpClient, HttpParams} from "@angular/common/http";

@Component({
  selector: 'app-sensor',
  templateUrl: './sensor.component.html',
  styleUrls: ['./sensor.component.scss']
})
export class SensorComponent implements OnInit {

  host: string = "192.168.1.200";
  port: string = "5000";
  sensorrequest: string = "http://"+ this.host + ':' + this.port + '/sensor';

  temp: string;
  humidity: string;
  light: string;
  motion: string;

  count:integer = 0;


  constructor(private client: HttpClient) { }

  ngOnInit() {
    this.getData();
    this.moniter();
  }

  moniter(){
    Observable.interval(2000 * 60).subscribe(x => {

      this.getData();
    });
  }

  getData(){
    this.sensor(this.sensorrequest, "t").subscribe(res =>{
      console.log("returning recieved data");
      console.log(res);
      this.temp = `${res.value}C`;
    },(err) => {
      console.log(err);
    })
    // *************************************
    this.sensor(this.sensorrequest, "h").subscribe(res =>{
      console.log("returning recieved data");
      console.log(res);
      this.humidity = `${res.value}%`;
    },(err) => {
      console.log(err);
    })
    // *************************************
    this.sensor(this.sensorrequest, "l").subscribe(res =>{
      console.log("returning recieved data");
      console.log(res);
      this.light = `${res.value}%`;
    },(err) => {
      console.log(err);
    })
    // *************************************
    this.sensor(this.sensorrequest, "m").subscribe(res =>{
      console.log("returning recieved data");
      console.log(res);
      const flag = res.value;
      if (flag === 1) {
        this.motion = "Motion Ditected"
      }
      else{
        this.motion = "No Motion Ditected"
      }
    },(err) => {
      console.log(err);
    })
    // *************************************
  }

  private sensor(url: string, parameater): Observable<any>{
    let params = new HttpParams().set('sensor', parameater);
    console.log(`Sending request to ${ this.sensorrequest }  ${params}`);
    return this.client.get(url, {params});
  }

}
