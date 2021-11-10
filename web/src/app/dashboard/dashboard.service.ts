import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { OBD } from './dashboard.type';

@Injectable({
  providedIn: 'root'
})
export class DashboardService {

  constructor(private httpClient: HttpClient) { }

  public getOBD(): Observable<OBD> {
    if(!environment.production)
      return new Observable<OBD>((observer) => {
        observer.next({
          speed: 50.5,
          rpm: 2800,
          throttlePos: 18.442556,
          engineLoad: 0.5,
          coolantTemp: 90
        });
      });

    return this.httpClient.get<OBD>(`${environment.apiUrl}json`);
  }
}
