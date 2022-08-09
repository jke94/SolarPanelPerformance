import { Component, OnInit, ViewChild } from '@angular/core';
import { ChartData } from 'chart.js';
import { ChartOptions } from 'chart.js';
import { DailyProduction } from 'src/app/models/interfaces/daily-production';
import { DataServiceService } from 'src/app/services/data-service/data-service.service';
import { DatesDatepickerService } from '../../services/dates-datepicker/dates-datepicker-service.service'

import { BaseChartDirective } from 'ng2-charts';

@Component({
  selector: 'app-verticalbar',
  templateUrl: './verticalbar.component.html',
  styleUrls: ['./verticalbar.component.css']
})
export class VerticalbarComponent implements OnInit {

  data!: DailyProduction[];
  elements!: DailyProduction[];
  myValue!: Array<number>;

  dateA!: Date;
  dateB!: Date;

  salesData!: ChartData<'bar'>
  chartOptions: ChartOptions = {
    responsive: true,
    plugins: {
      title: {
        display: true
      },
    },
  };

  @ViewChild(BaseChartDirective) chart?: BaseChartDirective;

  constructor(
    private dataServiceService: DataServiceService,
    private datesDatepickerService: DatesDatepickerService) {

  }

  getData() {
    var dateA = this.datesDatepickerService.dateFrom;
    var dateB = this.datesDatepickerService.dateTo;

    this.dataServiceService.getJSON()
      .subscribe(data => {
        var tmp = data as DailyProduction[];

        this.elements = tmp.filter(function (item) {
          var itemTime = new Date(item.Date).getTime()
          return itemTime >= dateA.getTime() && itemTime <= dateB.getTime();
        })

        this.myValue = Array.from({ length: this.elements.length }, (value, key) => key + 1)

        this.salesData = {
          labels: this.elements.map(i => i.Date),
          datasets: [
            { label: 'Production (kWh)', data: this.elements.map(i => i.MaxDailyProduction) }
          ],
        };
      });

    this.chart?.update()
  }

  ngOnInit(): void {

  }
}
