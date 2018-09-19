import { HttpClient } from '@angular/common/http'
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import {HttpParams} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class ServerRequestService {
  host: string = "192.168.1.200";
  port: string = "5000";

  mqttrequest: string = "http://"+ this.host + ':' + this.port;

  constructor(private client: HttpClient) { }

  private get(url: string, parameater): Observable<any>{
    let params = new HttpParams().set('_pin', parameater);
    console.log(`Sending request to ${ this.mqttrequest }  ${params}`);
    return this.client.get(url, {params});
  }

  public mqttResponce(pin){

      const data = this.get(this.mqttrequest, pin).subscribe(res =>{
      console.log("returning recieved data");
      return res;
    },(err) => {
      console.log(err);
    })
  }
}
