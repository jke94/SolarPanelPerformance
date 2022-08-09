import { Component, OnInit } from '@angular/core';
import { MatDatepickerInputEvent } from '@angular/material/datepicker';
import { DatesDatepickerService } from '../../services/dates-datepicker/dates-datepicker-service.service'

@Component({
  selector: 'app-dates-datepicker',
  templateUrl: './dates-datepicker.component.html',
  styleUrls: ['./dates-datepicker.component.css']
})

export class DatesDatepickerComponent implements OnInit {

  dateFrom!: Date
  dateTo!: Date

  constructor(
    private datesDatepickerService: DatesDatepickerService) {

  }

  ngOnInit(): void {
  }

  getDateFrom(event: MatDatepickerInputEvent<Date>) {
    if (event.value != null) {
      this.datesDatepickerService.dateFrom = event.value
      this.dateFrom = event.value
      console.log(`dateFrom: ${event.value}`)
    }
  }
  getDateTo(event: MatDatepickerInputEvent<Date>) {
    if (event.value != null) {
      this.datesDatepickerService.dateTo = event.value
      this.dateTo = event.value
      console.log(`dateTo: ${event.value}`)
    }
  }
}
