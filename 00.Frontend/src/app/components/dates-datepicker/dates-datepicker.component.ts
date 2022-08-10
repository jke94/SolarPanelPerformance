import { Component, OnInit } from '@angular/core';
import { MatDatepickerInputEvent } from '@angular/material/datepicker';
import { DatesDatepickerService } from '../../services/dates-datepicker/dates-datepicker-service.service'
import { DatePipe } from '@angular/common';
@Component({
  selector: 'app-dates-datepicker',
  templateUrl: './dates-datepicker.component.html',
  styleUrls: ['./dates-datepicker.component.css']
})

export class DatesDatepickerComponent implements OnInit {

  dateFrom!: string
  dateTo!: string
  numberOfDays!:number

  constructor(
    private datesDatepickerService: DatesDatepickerService) {

  }

  ngOnInit(): void {
    this.dateFrom = '-'
    this.dateTo = '-'
    this.numberOfDays = 0
  }

  getDateFrom(event: MatDatepickerInputEvent<Date>) {
    if (event.value != null) {
      this.datesDatepickerService.dateFrom = event.value
      this.dateFrom = this.convertDate(event.value)
    }
  }
  getDateTo(event: MatDatepickerInputEvent<Date>) {
    if (event.value != null) {
      this.datesDatepickerService.dateTo = event.value
      this.dateTo = this.convertDate(event.value)
    }
  }

  private convertDate(date: Date) : string {
    const datepipe: DatePipe = new DatePipe('en-US')
    let formattedDate = 'None'
    formattedDate = datepipe.transform(date, 'dd-MM-yy')!
    return formattedDate;
  }
}
