import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DatesDatepickerService {

  dateFrom!:Date
  dateTo!:Date

  constructor() { }
}
