import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { DailyProduction } from 'src/app/models/interfaces/daily-production';

@Injectable({
  providedIn: 'root'
})
export class DataServiceService {

  constructor(private http: HttpClient) {}
  
  public getJSON(): Observable<DailyProduction[]> {
    return this.http.get<DailyProduction[]>("./assets/SolarPanel-MaxDailyProduction.json");
  }
}
